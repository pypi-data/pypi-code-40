import os
import subprocess
from typing import Dict, Any, Optional

from janis_runner.data.models.schema import TaskMetadata, TaskStatus
from janis_runner.engines.engine import Engine
from janis_runner.utils import Logger


def read_stdout(process):
    for stdout_line in iter(process.stderr.readline, "b"):
        line = stdout_line.decode("utf-8").rstrip()
        if not line.strip():
            continue
        yield line.strip()

    process.stderr.close()
    return_code = process.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, "cmd")


class Toil(Engine):
    def __init__(self, tid, scale=None, loglevel=None):
        super(Toil, self).__init__("toil-" + tid, Engine.EngineType.toil)
        self.tid = tid
        self.scale: Optional[float] = scale
        self.loglevel = loglevel

    def start_engine(self):
        Logger.info(
            "Toil doesn't run in a server mode, an instance will "
            "automatically be started when a task is created"
        )

    def stop_engine(self):
        Logger.info(
            "Toil doesn't run in a server mode, an instance will "
            "be automatically terminated when a task is finished"
        )

    def start_from_paths(self, tid, source_path: str, input_path: str, deps_path: str):
        print("TMP: " + os.getenv("TMPDIR"))
        scale = ["--scale", str(self.scale)] if self.scale else []
        loglevel = ["--logLevel=" + self.loglevel] if self.loglevel else []
        cmd = ["toil-cwl-runner", "--stats", *loglevel, *scale, source_path, input_path]
        Logger.log("Running command: '" + " ".join(cmd) + "'")
        process = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, preexec_fn=os.setsid, stderr=subprocess.PIPE
        )

        Logger.info("CWLTool has started with pid=" + str(process.pid))

        for line in read_stdout(process):
            if "Path to job store directory is" in line:
                idx = line.index("Path to job store directory is")
                Logger.critical("JOBSTORE DIR: " + line[idx + 1 :])
            Logger.log("toil: " + line)

        print("finished")

    def start_from_task(self, task):
        pass

    def poll_task(self, identifier) -> TaskStatus:
        return TaskStatus.PROCESSING

    def outputs_task(self, identifier) -> Dict[str, Any]:
        pass

    def terminate_task(self, identifier) -> TaskStatus:
        pass

    def metadata(self, identifier) -> TaskMetadata:
        raise NotImplementedError(
            "metadata needs to be implemented in Toil, may require rework of tool"
        )
