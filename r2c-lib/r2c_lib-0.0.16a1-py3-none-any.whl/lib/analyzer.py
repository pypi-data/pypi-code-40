#!/usr/bin/env python3
import abc
import json
import logging
import os
import pathlib
import shutil
import subprocess
import sys
import tarfile
import threading
from datetime import datetime
from typing import Any, Dict, List, NewType, Optional, Tuple, Union, cast

import docker
import jsonschema

from r2c.lib.constants import DEFAULT_ANALYSIS_WORKING_TEMPDIR_SUFFIX
from r2c.lib.errors import AnalyzerOutputNotFound
from r2c.lib.filestore import FileStore
from r2c.lib.input import AnalyzerInput, GitRepoCommit
from r2c.lib.manifest import AnalyzerManifest, AnalyzerOutputType
from r2c.lib.registry import RegistryData
from r2c.lib.specified_analyzer import SpecifiedAnalyzer
from r2c.lib.util import Timeout, get_tmp_dir, handle_readonly_fix
from r2c.lib.versioned_analyzer import VersionedAnalyzer

MEMORY_LIMIT = (
    "1536m"
)  # clean t2.small with unbuntu 18.04 has Mem:           1991          92        1514           0         385        1752

# We need a very small Linux image so we can do some filesystem stuff through
# Docker.
ALPINE_IMAGE = "alpine:3.9"

ContainerLog = NewType("ContainerLog", str)
ContainerStats = NewType("ContainerStats", List[Any])
VOLUME_MOUNT_IN_DOCKER = "/analysis"


def watch_log(stream, is_stdout):
    """Helper function that we run in a thread to preserve stdout/stderr distinction from the docker container
    """
    for line in stream:
        if is_stdout:
            sys.stdout.write(line.decode("utf-8"))
        else:
            sys.stderr.write(line.decode("utf-8"))


class AnalyzerNonZeroExitError(Exception):
    """
        Thrown when analyzer docker container exists with non-zero exit code
    """

    def __init__(self, status_code, log, stats, versioned_analyzer=None):
        self._status_code = status_code
        self._log = log
        self._stats = stats
        self._versioned_analyzer = versioned_analyzer

    @property
    def log(self):
        return self._log

    @property
    def stats(self):
        return self._stats

    @property
    def status_code(self):
        return self._status_code

    @property
    def versioned_analyzer(self):
        return self._versioned_analyzer

    def __str__(self):
        analyzer = self._versioned_analyzer if self._versioned_analyzer else "unknown"
        return f"Analyzer {analyzer} finished with non-zero exit code: {self._status_code}.\n Container log:\n {self._log}"


class AnalyzerImagePullFail(Exception):
    """
        Thrown when analyzer image fails to pull
    """


class UnsupportedAnalyzerType(Exception):
    """
        Thrown when unsupported analyzer type is encountered
    """


class InvalidAnalyzerOutput(Exception):
    """Thrown when the analyzer's output doesn't conform to its schema."""

    def __init__(
        self, inner: Union[jsonschema.ValidationError, json.JSONDecodeError]
    ) -> None:
        self.inner = inner


class InvalidAnalyzerIntegrationTestDefinition(Exception):
    """Thrown when the analyzer's integration test doesn't conform to its schema."""

    def __init__(
        self, inner: Union[jsonschema.ValidationError, json.JSONDecodeError]
    ) -> None:
        self.inner = inner


def get_default_analyzer_working_dir():
    return os.path.join(get_tmp_dir(), DEFAULT_ANALYSIS_WORKING_TEMPDIR_SUFFIX)


class Analyzer:
    def __init__(
        self,
        registry_data: RegistryData,
        json_output_store: FileStore,
        filesystem_output_store: FileStore,
        log_store: FileStore,
        stats_store: FileStore,
        localrun: bool = False,
        timeout: int = 1200,
        workdir: str = get_default_analyzer_working_dir(),
    ) -> None:
        self._registry_data = registry_data
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.INFO)
        self._docker_client = docker.from_env()
        self._timeout = timeout

        self._json_output_store = json_output_store
        self._filesystem_output_store = filesystem_output_store
        self._log_store = log_store
        self._stats_store = stats_store

        # TODO remove once cloner analyzer doesn't need to checkout
        self._localrun = localrun

        # Local run working dir. For analyzer use only.
        # THE CONTENTS OF THIS DIRECTORY MAY BE ERASED OR MODIFIED WITHOUT WARNING
        self._workdir = workdir
        self._registry_data = registry_data

    def reset_registry_data(self, registry_data: RegistryData) -> None:
        self._registry_data = registry_data

    @staticmethod
    def _get_analyzer_output_extension(output_type: AnalyzerOutputType) -> str:
        """For an analyzer of this output type, what is the file extension of the single-file output?

        """

        if output_type == AnalyzerOutputType.json:
            return ".json"
        elif output_type == AnalyzerOutputType.filesystem:
            return ".tar.gz"
        elif output_type == AnalyzerOutputType.both:
            return ""
        else:
            raise RuntimeError(
                f"non-implemented; don't know filename extension for analyzer with output type: {output_type}"
            )

    @staticmethod
    def get_analyzer_output_path(
        mount_folder: str, output_type: AnalyzerOutputType
    ) -> str:
        """For an analyzer of this output type, where does the single-file output live?

        """
        BASE_DIR = "output"
        if output_type == AnalyzerOutputType.json:
            return os.path.join(
                mount_folder,
                BASE_DIR,
                "output" + Analyzer._get_analyzer_output_extension(output_type),
            )
        elif output_type == AnalyzerOutputType.filesystem:
            return os.path.join(
                mount_folder,
                BASE_DIR,
                "fs" + Analyzer._get_analyzer_output_extension(output_type),
            )
        else:
            raise RuntimeError(
                f"non-implemented; don't know where to find output for analyzer with output type: {output_type}"
            )

    def full_analyze_request(
        self,
        analyzer_input: AnalyzerInput,
        specified_analyzer: SpecifiedAnalyzer,
        force: bool,
        pass_analyzer_output: bool,
        interactive_index: Optional[int] = None,
        interactive_name: Optional[str] = None,
        memory_limit: Optional[str] = None,
        env_args_dict: Optional[dict] = None,
    ) -> dict:
        """
            Handle an analysis request and uploading output.

            Args:
                specified_analyzer: unique identifier for analyzer container to run w/ parameter
                analyzed_input: input to analyze
                force: if true, the analysis will proceed even if there is already a cached result for this request.
                interactive_index: if set, the analyzer in the execution graph (defaults to last if interactive_index not specified)  will drop into shell rather than running automatically.
                pass_analyzer_output: if true, the analyzer's stdout and stderr will be passed to the current process stdout and stderr, respectively

            Returns:
                A dict with information about the final output last analyzer in the dependency graph to run.
        """

        skipped = True

        execution_order = self._registry_data.sorted_deps(specified_analyzer)

        analyzer_execution_str = "".join(
            [f"\n\t{i}: {analyzer}" for i, analyzer in enumerate(execution_order)]
        )
        self._logger.info(
            f"All analyzers that will be run, in order: {analyzer_execution_str }"
        )

        container_output_path = ""
        for dependency_index, specified_dependency in enumerate(execution_order):
            if interactive_index or interactive_index == 0:
                try:
                    is_interactive_dependency = (
                        execution_order[interactive_index] == specified_dependency
                    )

                except IndexError:
                    self._logger.error(
                        f"{interactive_index} could not be used as interactive shell index. Stopping Analysis."
                    )
                    raise Exception(
                        f"Could not create interactive shell into dependency at {interactive_index}."
                    )
            elif (
                interactive_name
                and interactive_name in specified_dependency.versioned_analyzer.name
            ):
                is_interactive_dependency = True
            else:
                is_interactive_dependency = False

            if is_interactive_dependency:
                print(
                    f"Calling `docker exec` into analyzer with name {specified_dependency}"
                )

            dependency = specified_dependency.versioned_analyzer

            output_type = self._registry_data.manifest_for(
                specified_dependency.versioned_analyzer
            ).output_type

            if output_type == AnalyzerOutputType.both:
                json_exists = self._json_output_store.contains(
                    analyzer_input, specified_dependency
                )
                filesystem_exists = self._filesystem_output_store.contains(
                    analyzer_input, specified_dependency
                )
                dependency_exists = json_exists and filesystem_exists
            elif output_type == AnalyzerOutputType.json:
                dependency_exists = self._json_output_store.contains(
                    analyzer_input, specified_dependency
                )
            elif output_type == AnalyzerOutputType.filesystem:
                dependency_exists = self._filesystem_output_store.contains(
                    analyzer_input, specified_dependency
                )
            else:
                raise Exception()

            if (
                # TODO check freshness here
                dependency_exists
                and not force
                and not is_interactive_dependency
            ):
                # use cache when non-interactive, non-forcing, dependency
                self._logger.info(
                    f"Analysis for {analyzer_input.to_json()} {specified_dependency} already exists. Keeping old analysis report"
                )
            else:
                self._logger.info(
                    f"Running: {dependency.name}, {dependency.version}..."
                )

                try:
                    mount_folder, container_log, stats = self._analyze(
                        specified_dependency,
                        analyzer_input,
                        interactive=is_interactive_dependency,
                        pass_analyzer_output=pass_analyzer_output,
                        memory_limit=memory_limit,
                        env_args_dict=env_args_dict,
                    )
                except AnalyzerNonZeroExitError as e:
                    container_log = e.log
                    stats = e.stats
                    self._log_store.write(
                        analyzer_input, specified_dependency, container_log
                    )
                    self._logger.info(f"Uploading analyzer stats: {len(stats)}")
                    self._stats_store.write(
                        analyzer_input, specified_dependency, json.dumps(stats)
                    )
                    raise e

                self._logger.info("Analyzer finished running.")
                self._logger.info("Uploading analyzer log")
                self._log_store.write(
                    analyzer_input, specified_dependency, container_log
                )
                self._logger.info(f"Uploading analyzer stats: {len(stats)}")
                self._stats_store.write(
                    analyzer_input, specified_dependency, json.dumps(stats)
                )

                self._logger.info("Uploading analyzer output")
                try:
                    container_output_path = self.upload_output(
                        specified_dependency, analyzer_input, mount_folder
                    )
                except FileNotFoundError:
                    output_path = self.get_analyzer_output_path(
                        VOLUME_MOUNT_IN_DOCKER, output_type
                    )
                    raise AnalyzerOutputNotFound(output_path=output_path)

                self._logger.info(f"Deleting {mount_folder}")
                shutil.rmtree(mount_folder, onerror=handle_readonly_fix)
                skipped = False

        return {
            "skipped": skipped,
            "container_output_path": container_output_path,
            "output_type": output_type.name,
        }

    def _validate_output(self, manifest: AnalyzerManifest, mount_folder: str) -> None:
        """Validates the output, then migrates it to the latest schema.

        Note that if the analyzer's output is not JSON, this does nothing since
        we don't have a way to validate non-JSON outputs.

        Throws:
            InvalidAnalyzerOutput: If validation fails.

        """
        if manifest.output_type != AnalyzerOutputType.json:
            return

        path = self.get_analyzer_output_path(mount_folder, manifest.output_type)
        with open(path) as f:
            try:
                output = json.load(f)
            except json.JSONDecodeError as err:
                raise InvalidAnalyzerOutput(err)

        try:
            manifest.output.validator(output).validate(output)
        except jsonschema.ValidationError as err:
            raise InvalidAnalyzerOutput(err) from err
        except Exception as err:
            raise RuntimeError(
                f"There was an error validating your output. Please check that you're outputing a valid output and try again: {err}"
            )

    def upload_output(
        self,
        specified_analyzer: SpecifiedAnalyzer,
        analyzer_input: AnalyzerInput,
        mount_folder: str,
    ) -> str:
        """
            Upload analyzer results

            Args:
                specified_analyzer: uniquely identifies analyzer container w/ parameters
                analyzer_input: the input that was analyzed
                mount_folder: volume mounted during analysis. Assumes output lives in
                mount_folder/output/output.json or mount_folder/output/fs

            Returns:
                The inside-container path to the analyzer output that was uploaded.

            Raises:
                InvalidAnalyzerOutput: if output fails to validate
                                       note that output is still uploaded
        """
        manifest = self._registry_data.manifest_for(
            specified_analyzer.versioned_analyzer
        )
        output_type = manifest.output_type
        if output_type == AnalyzerOutputType.json:
            output_file_path = self.get_analyzer_output_path(mount_folder, output_type)
            self._logger.info(f"Caching {output_file_path}")
            self._json_output_store.put(
                analyzer_input, specified_analyzer, output_file_path
            )
        elif output_type == AnalyzerOutputType.filesystem:
            output_file_path = self.get_analyzer_output_path(mount_folder, output_type)
            self._logger.info("Filesystem output type. Tarring output for uploading...")
            with tarfile.open(output_file_path, "w:gz") as tar:
                tar.add(
                    mount_folder + "/output/fs",
                    arcname=specified_analyzer.versioned_analyzer.name,
                )
            self._logger.info(f"Caching {output_file_path}")
            self._filesystem_output_store.put(
                analyzer_input, specified_analyzer, output_file_path
            )
        elif output_type == AnalyzerOutputType.both:
            filesystem_output_file_path = self.get_analyzer_output_path(
                mount_folder, AnalyzerOutputType.filesystem
            )
            self._logger.info("Both output type. Tarring output for uploading...")
            with tarfile.open(filesystem_output_file_path, "w:gz") as tar:
                tar.add(
                    mount_folder + "/output/fs",
                    arcname=specified_analyzer.versioned_analyzer.name,
                )
            json_output_file_path = self.get_analyzer_output_path(
                mount_folder, AnalyzerOutputType.json
            )
            self._logger.info(f"Caching {json_output_file_path}")
            self._json_output_store.put(
                analyzer_input, specified_analyzer, json_output_file_path
            )

            self._logger.info(f"Caching {filesystem_output_file_path}")
            self._filesystem_output_store.put(
                analyzer_input, specified_analyzer, filesystem_output_file_path
            )

            output_file_path = json_output_file_path
        else:
            raise RuntimeError(
                f"non-implemented analyzer output handler for output type: {output_type}"
            )

        # Invalid outputs should still be uploaded, but we want to
        # count them as failing.
        self._validate_output(manifest, mount_folder)
        return output_file_path

    def prepare_mount_volume(
        self, specified_analyzer: SpecifiedAnalyzer, analyzer_input: AnalyzerInput
    ) -> str:
        """
            Prepares directory to be mounted to docker container IMAGE_ID to
            run analysis on analyzer input. Raises exception when cannot
            prepare directory with necessary dependencies.

            Args:
                specified_analyzer: uniquely identifies analyzer container w/ parameters
                analyzer_input: input to run analysis on

            Returns:
                mount_folder: path to root of volume prepared. For analyzer spec v3 this is
                the parent directory containing inputs/ and output/
        """
        now_ts = datetime.utcnow().isoformat().replace(":", "").replace("-", "")
        image_id = specified_analyzer.versioned_analyzer.image_id
        safe_image_id = image_id.split("/")[-1].replace(":", "__")
        mount_folder = os.path.join(self._workdir, f"{safe_image_id}__{now_ts}")

        self._logger.info("Setting up volumes for analyzer container.")
        self._logger.info(f"Will mount: {mount_folder}")
        if pathlib.Path(mount_folder).exists():
            self._logger.info(f"cleaning up old folder {mount_folder}")
            shutil.rmtree(mount_folder)

        input_dir = os.path.join(mount_folder, "inputs")
        output_dir = os.path.join(mount_folder, "output")
        pathlib.Path(input_dir).mkdir(parents=True, exist_ok=True)
        pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)
        os.chmod(output_dir, 0o777)
        # TODO why should this only be done if we expect fs?
        fs_dir = os.path.join(output_dir, "fs")
        pathlib.Path(fs_dir).mkdir(parents=True, exist_ok=True)
        os.chmod(fs_dir, 0o777)

        # Setup Parameters
        with open(os.path.join(input_dir, "parameters.json"), "w") as parameters_file:
            json.dump(specified_analyzer.parameters, parameters_file)

        dependencies = self._registry_data.get_direct_dependencies(
            specified_analyzer.versioned_analyzer
        )

        with open(os.path.join(input_dir, "target.json"), "w") as target_file:
            arguments = analyzer_input.to_json()
            json.dump(arguments, target_file)
            success = True

        # TODO: remove this after fixing cloner to respect new target file
        if isinstance(analyzer_input, GitRepoCommit):
            repo_commit = cast(GitRepoCommit, analyzer_input)
            with open(os.path.join(input_dir, "cloner-input.json"), "w") as target_file:
                arguments = {
                    "git_url": repo_commit.repo_url,
                    "commit_hash": repo_commit.commit_hash,
                }
                json.dump(arguments, target_file)
                success = True

        self._logger.info(f"Loading dependencies' outputs: {dependencies}")
        for specified_dependency in dependencies:
            self._logger.info(f"Loading output of {specified_dependency}")

            output_type = self._registry_data.manifest_for(
                specified_dependency.versioned_analyzer
            ).output_type
            self._logger.info(
                f"Retrieving dependency output for run of {specified_analyzer} on {analyzer_input}"
            )

            # Ensure Target Location Exists
            pathlib.Path(
                os.path.join(input_dir, specified_dependency.versioned_analyzer.name)
            ).mkdir(parents=True, exist_ok=True)

            if output_type == AnalyzerOutputType.json:
                success = self._json_output_store.get(
                    analyzer_input,
                    specified_dependency,
                    f"{input_dir}/{specified_dependency.versioned_analyzer.name}.json",
                )
            elif output_type == AnalyzerOutputType.filesystem:
                fs_input_tar = os.path.join(input_dir, "output.tar.gz")
                if self._filesystem_output_store.get(
                    analyzer_input, specified_dependency, fs_input_tar
                ):
                    self._logger.info(f"Extracting filesystem dependency")
                    with tarfile.open(fs_input_tar) as tar:
                        tar.extractall(input_dir)
                    os.remove(fs_input_tar)
                    success = True
                else:
                    success = False
            elif output_type == AnalyzerOutputType.both:
                json_success = self._json_output_store.get(
                    analyzer_input,
                    specified_dependency,
                    f"{input_dir}/{specified_dependency.versioned_analyzer.name}.json",
                )

                fs_input_tar = os.path.join(input_dir, "output.tar.gz")
                if self._filesystem_output_store.get(
                    analyzer_input, specified_dependency, fs_input_tar
                ):
                    self._logger.info(f"Extracting filesystem dependency")
                    with tarfile.open(fs_input_tar) as tar:
                        tar.extractall(input_dir)
                    os.remove(fs_input_tar)
                    filesystem_success = True
                else:
                    filesystem_success = False

                success = json_success and filesystem_success

            else:
                raise RuntimeError(
                    f"unimplemented; output extractor for analyzer output type: {output_type}"
                )

            if success:
                self._logger.info(
                    f"Done setting up output of dependency {specified_dependency}."
                )
            else:
                self._logger.error(
                    f"The output of running {analyzer_input} on {specified_dependency} could not be found. Failed to setup dependencies. Stopping Analysis."
                )
                raise Exception(
                    f"Could not prepare dependency: {specified_dependency} does not exist."
                )

        return mount_folder

    def run_image_on_folder(
        self,
        versioned_analyzer: VersionedAnalyzer,
        mount_folder: str,
        interactive: bool,
        pass_analyzer_output: bool,
        memory_limit: Optional[str],
        env_args_dict: Optional[dict] = None,
    ) -> Tuple[ContainerLog, ContainerStats]:
        """
            Mount MOUNT_FOLDER as /analysis in docker container and run IMAGE_ID on it

            Args:
                versioned_analyzer: uniquely identifies docker image, as well as name and version
                mount_folder: path to directory we will mount as /analysis. In analyzer spec v3
                this is the directory that contains inputs/ and output. Assumes this directory is
                properly prepared
                interactive: if true, change the run command so that it drops into bash shell. Useful for debugging.
                memory_limit: memory limit for container, e.g. '2G'
            Raises:
                AnalyzerImagePullFail: if IMAGE_ID is not available and fails to pull
                TimeoutError: on timeout
                AnalyzerNonZeroExitError: when container exits with non-zero exit code
            Returns:
                container_log: stdout and err of container as a string
        """
        image_id = versioned_analyzer.image_id
        if not any(i for i in self._docker_client.images.list() if image_id in i.tags):
            self._logger.info(f"Image {image_id} not found. Pulling.")
            try:
                self._docker_client.images.pull(image_id)
            except Exception as e:
                raise AnalyzerImagePullFail(str(e))
        self._docker_client.images.pull(ALPINE_IMAGE)
        container = None
        stats = []

        VOLUME_MOUNT_IN_DOCKER = "/analysis"

        # we can't use volume mounting with remote docker (for example, on
        # CircleCI), have to docker cp
        is_remote_docker = os.environ.get("DOCKER_HOST") is not None

        if is_remote_docker:
            self._logger.info("Remote docker client; using docker cp")
            manager: AbstractDockerFileManager = RemoteDockerFileManager(
                self._docker_client, mount_folder
            )
        else:
            manager = LocalDockerFileManager(self._docker_client, mount_folder)

        if is_remote_docker and interactive:
            self._logger.error("Wait for start not supported with remote docker client")
            interactive = False

        env_vars = (
            " ".join([f"-e {k}={v}" for k, v in env_args_dict.items()])
            if env_args_dict
            else ""
        )
        self._logger.info(
            f"""Running container {image_id} (memory limit: {memory_limit}): \n\t: debug with docker run {env_vars} --volume "{mount_folder}:{VOLUME_MOUNT_IN_DOCKER}" {image_id}"""
        )

        try:
            with Timeout(self._timeout):
                container = self._docker_client.containers.create(
                    image_id,
                    volumes=manager.volumes(),
                    command="tail -f /dev/null" if interactive else None,
                    mem_limit=memory_limit if memory_limit else None,
                    environment=env_args_dict,
                )

                # Set up the VOLUME_MOUNT_IN_DOCKER.
                manager.copy_input()

                container.start()

                if interactive:
                    self._logger.info(
                        f"\n\nYour container is ready: running \n\tdocker exec -i -t {container.id} /bin/sh"
                    )
                    subprocess.call(
                        f"docker exec -i -t {container.id} /bin/sh", shell=True
                    )
                    sys.exit(1)

                # launch two threads to display stdout and stderr while the container is running
                if pass_analyzer_output:
                    stdout_watch = threading.Thread(
                        target=watch_log,
                        args=(
                            container.logs(stdout=True, stderr=False, stream=True),
                            True,
                        ),
                    )
                    stdout_watch.start()
                try:
                    for stat in container.stats(decode=True, stream=True):
                        if (
                            stat["read"] == "0001-01-01T00:00:00Z"
                        ):  # stats from stopped containers is 0 so read stats until this
                            break
                        stats.append(stat)
                        self._logger.info(f"Collected stat from {container.id}")
                        container.reload()  # refresh from server
                        if container.status != "running":
                            break
                except TimeoutError as e:
                    self._logger.info(
                        "caught TimeoutError in stats collection, re-raising"
                    )
                    raise e  # don't catch timeout errors
                except Exception as e:
                    self._logger.exception("error getting stats")
                    raise e  # TODO Somehow TimeoutErrors are being hidden under other errors. For now just raise everything

                # Block until completion
                # We run with container detached so we can kill on timeout
                status = container.wait()

                # Retrieve status code and logs before removing container
                status_code = status.get("StatusCode")

                # full, merged stdout + stderr log
                container_log = container.logs(stdout=True, stderr=True).decode("utf-8")
                # self._logger.info(f"Container output: {container_log}")

                manager.copy_output()
                manager.teardown()

                container.remove()
                container = None

            if status_code != 0:
                raise AnalyzerNonZeroExitError(
                    status_code, container_log, stats, versioned_analyzer
                )

        except Exception as e:
            # skip AnalyzerNonZeroExitError for debugability
            if isinstance(e, AnalyzerNonZeroExitError):
                raise e

            self._logger.exception(f"There was an error running {image_id}: {e}")

            if container:
                self._logger.info(f"killing container {container.id}")
                try:
                    # Kill and Remove Container as well as associated volumes
                    container.remove(v=True, force=True)
                    self._logger.info(f"successfully killed container {container.id}")
                except Exception:
                    self._logger.exception("error killing container")

            if os.path.exists(mount_folder):
                self._logger.info(f"deleting {mount_folder}")
                manager._set_permissions()

                shutil.rmtree(mount_folder, ignore_errors=True)

            manager.teardown()

            raise e

        return ContainerLog(container_log), ContainerStats(stats)

    def _analyze(
        self,
        specified_analyzer: SpecifiedAnalyzer,
        analyzer_input: AnalyzerInput,
        interactive: bool,
        pass_analyzer_output: bool,
        memory_limit: Optional[str],
        env_args_dict: Optional[dict] = None,
    ) -> Tuple[str, ContainerLog, ContainerStats]:
        """
            Run IMAGE_ID analyzer on ANALYZER_INPUT, retreiving dependencies cache
            as necessary.

            Args:
                specified_analyzer: uniquely identifies docker container to run w/ args
                interactive: See run_image_on_folder
                analyzer_input: object describing input to run on
                pass_analyzer_output: See run_image_on_folder
                memory_limit: See run_image_on_folder
                env_args_dict: See run_image_on_folder

            Returns:
                (mount_folder, container_log):

                mount_folder: path to root of volume mounted. For analyzer spec v3 this is
                the parent directory containing inputs/ and output/

                container_log: str combined output of stdout and stderr of analyzer container

        """
        mount_folder = self.prepare_mount_volume(specified_analyzer, analyzer_input)
        container_log, stats = self.run_image_on_folder(
            versioned_analyzer=specified_analyzer.versioned_analyzer,
            mount_folder=mount_folder,
            interactive=interactive,
            pass_analyzer_output=pass_analyzer_output,
            memory_limit=memory_limit,
            env_args_dict=env_args_dict,
        )
        return (mount_folder, container_log, stats)


class AbstractDockerFileManager(abc.ABC):
    """Base class for helpers for analyzer input/output."""

    @abc.abstractmethod
    def copy_input(self):
        """Copies the input from the host to the container."""

    @abc.abstractmethod
    def copy_output(self):
        """Copies the input from the host to the container."""

    def _set_permissions(self):
        """Makes everything in the volume/bind mount world-readable."""
        self._docker_client.containers.run(
            ALPINE_IMAGE,
            f'chmod -R 0777 "{VOLUME_MOUNT_IN_DOCKER}"',
            volumes=self.volumes(),
        )

    @abc.abstractmethod
    def volumes(self) -> Dict[str, dict]:
        """The volumes to be mounted."""

    @abc.abstractmethod
    def teardown(self):
        """Must be called when we're done with docker."""


class LocalDockerFileManager(AbstractDockerFileManager):
    """Bind-mounts a local file. Fast, but does not work with remote docker."""

    def __init__(self, docker_client, mount_folder):
        """mount_folder is the host folder to be mounted in the container."""
        self._docker_client = docker_client
        self._mount_folder = mount_folder

    # Since we use a bind mount, we don't need to do anything special to copy files.
    def copy_input(self):
        self._set_permissions()

    def copy_output(self):
        self._set_permissions()

    def volumes(self) -> Dict[str, dict]:
        return {self._mount_folder: {"bind": VOLUME_MOUNT_IN_DOCKER, "mode": "rw"}}

    def teardown(self):
        pass


class RemoteDockerFileManager(AbstractDockerFileManager):
    """Explicitly sets up a volume. Slower, but works with remote docker."""

    def __init__(self, docker_client, mount_folder):
        """mount_folder is the host folder to be mounted in the container."""
        self._docker_client = docker_client
        self._mount_folder = mount_folder
        self._volume = self._docker_client.volumes.create()
        # A Docker container that we'll use to copy files in and out.
        self._dummy = self._docker_client.containers.create(
            ALPINE_IMAGE,
            command=f'chmod -R 0777 "{VOLUME_MOUNT_IN_DOCKER}"',
            volumes=self.volumes(),
        )

    def copy_input(self):
        # Weirdly, there doesn't appear to be a nice way to do this
        # from within the Python API.
        subprocess.check_output(
            [
                "docker",
                "cp",
                f"{self._mount_folder}/.",
                f"{self._dummy.id}:{VOLUME_MOUNT_IN_DOCKER}",
            ]
        )
        self._set_permissions()

    def copy_output(self):
        self._set_permissions()
        # Weirdly, there doesn't appear to be a nice way to do this
        # from within the Python API.
        subprocess.check_output(
            [
                "docker",
                "cp",
                f"{self._dummy.id}:{VOLUME_MOUNT_IN_DOCKER}/.",
                f"{self._mount_folder}",
            ]
        )
        self._set_permissions()

    def volumes(self) -> Dict[str, dict]:
        return {self._volume.name: {"bind": VOLUME_MOUNT_IN_DOCKER, "mode": "rw"}}

    def teardown(self):
        self._dummy.remove()
