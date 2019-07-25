#   Copyright 2018 Samuel Payne sam_payne@byu.edu
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#       http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import hashlib
import os

def get_dataset_path(dataset):
    """Get the path to the main directory for a dataset.

    Parameters:
    dataset (str): The path to get the directory for. Must be all lowercase.

    Returns:
    str: The path to the main directory of the specified dataset.
    """
    path_here = os.path.abspath(os.path.dirname(__file__))
    dataset_dir = f"data_{dataset}"
    dataset_path = os.path.join(path_here, dataset_dir)
    if os.path.isdir(dataset_path):
        return dataset_path
    else:
        print(f"{dataset} is not a valid dataset.")
        return

def is_latest_version(version, index):
    """Determine whether a specific version number is the latest version in the index.

    Parameters:
    version (str): The version number to check.
    index (dict): The parsed index for the dataset.

    Returns:
    bool: Whether the given version number is the latest in the index. Returns None if it's an invalid version.
    """
    # Check the version
    if version == "latest":
        return True
    elif version in index.keys():
        index_latest = max(index.keys(), key=float)
        if version == index_latest:
            return True
        else:
            return False
    else:
        return

def validate_version(version, dataset, use_context):
    """Parse and validate a given version number. If version is "latest", check that index and installed latest match.

    Parameters:
    version (str): The version number to validate.
    dataset (str): The name of the dataset we're validating the version for.
    use_context (str): Either "download" or "init", depending on whether the function is being called as part of a data download or a dataset loading. Allows for more detailed error messages. Pass None if you don't want more detailed error messages.

    Returns:
    str: The version number, if valid input. Else return None.
    """
    # Get our dataset path, then our dataset index
    dataset_path = get_dataset_path(dataset)
    index = get_index(dataset_path)

    # See what the highest version in the index is
    index_latest = max(index.keys(), key=float)

    # Parse and validate the version they passed
    if version in index.keys():
        if float(version) < float(index_latest): # Print a warning if they're using an old version
            print(f"WARNING: Old data version. Latest is {index_latest}. This is {version}.")
        return version

    elif version.lower() == "latest":
        latest_installed = get_latest_installed(dataset_path)
        if (index_latest == latest_installed) or (latest_installed is None):
            return index_latest
        else: # If their latest installed version is different from the latest version recorded in the index, then we don't know which one they meant when they passed "latest".
            if use_context == "download":
                print(f"NOTE: Downloading new version of {dataset} dataset: {index_latest}. This will now be the default version when the dataset is loaded. If you wish to load an older version of the data, you must specify it with the 'version' parameter when you load the dataset.")
                return index_latest
            elif use_context == "init":
                print(f"You requested to load the {dataset} dataset. Latest version is {index_latest}, which is not installed locally. To download it, run \"cptac.download(dataset='{dataset}')\". You will then be able to load the latest version of the dataset. To skip this and instead load the older version that is already installed, call \"cptac.{dataset.title()}(version='{latest_installed}')\".")
                return
    else:
        print(f"{version} is an invalid version for the {dataset} dataset. Valid versions: {', '.join(index.keys())}")
        return

def get_version_files_paths(dataset, version, data_files):
    """For dataset loading. Check that a version is installed, then return the paths to the data files for that version.

    Parameters:
    dataset (str): The name of the dataset to get the paths for.
    version (str): The version number of the dataset to get the paths for. This function will not parse "latest"; version should have been already validated.
    data_files: (list of str): The file names to get paths for.

    Returns:
    list of str: The paths to the given data files for specified version of the dataset.
    """
    # Get our dataset path and index
    dataset_path = get_dataset_path(dataset)
    index = get_index(dataset_path)

    # Check that they've installed the version they requested
    version_path = os.path.join(dataset_path, f"{dataset}_v{version}")
    if not os.path.isdir(version_path):
        print(f"Data version {version} is not installed. To install, run \"cptac.download(dataset='{dataset}', version='{version}')\".")
        return

    data_files_paths = []
    for data_file in data_files:
        file_path = os.path.join(version_path, data_file)
        if not os.path.isfile(file_path): # Check that the file exists
            if is_latest_version(version, index):
                print(f"Missing data file '{data_file}'. Call \"cptac.download(dataset='{dataset}')\" to download it. Dataset loading aborted.")
            else:
                print(f"Missing data file '{data_file}'. Call \"cptac.download(dataset='{dataset}', version='{version}')\" to download it. Dataset loading aborted.")
            return
        data_files_paths.append(file_path)

    return data_files_paths

def get_latest_installed(dataset_path):
    """Return the latest version number installed in a dataset directory.

    Parameters:
    dataset_path (str): The path to the dataset of interest.

    Returns:
    str: The latest version installed locally.
    """
    dirs = [dir.strip() for dir in os.listdir(dataset_path)
                if os.path.isdir(os.path.join(dataset_path, dir))]

    dataset_dir = dataset_path.split(os.sep)[-1]
    dataset_name = dataset_dir.split('_')[1] # For example, we get 'endometrial' from 'data_endometrial'
    version_dir_prefix = dataset_name + '_v'
    versions = [dir.replace(version_dir_prefix, '') for dir in dirs
                    if dir.startswith(version_dir_prefix)]
    if len(versions) == 0:
        return
    latest_installed = max(versions, key=float)
    return latest_installed

def get_index(dataset_path):
    """Get the index for a dataset, as a nested dictionary

    Parameters:
    dataset_path (str): The path to the dataset you want the index of.

    Returns:
    dict: The index, as a nested dictionary.
    """
    index_file = "index.txt"
    index_path = os.path.join(dataset_path, index_file)
    with open(index_path, 'r') as index_file:
        index_lines = index_file.readlines()

    index = {}
    version = None
    for line in index_lines:
        line = line.strip()
        if line.startswith('#'):
            version = line[1:]
            index[version] = {}
        else:
            line_list = line.split('\t')
            file_name = line_list[0]
            file_hash = line_list[1]
            file_url = line_list[2]
            index[version][file_name] = {}
            index[version][file_name]["hash"] = file_hash
            index[version][file_name]["url"] = file_url
    return index

def parse_tsv_dict(path):
    """Read in a dictionary from the given two column tsv file.

    Parameters:
    path (str): The path to the two column tsv file.

    Returns:
    dict: The tsv file read into a dictionary.
    """
    with open(path, 'r') as data_file:
        lines = data_file.readlines()

    data_dict = {}
    for line in lines:
        line_list = line.strip().split("\t")
        key = line_list[0]
        value = line_list[1]
        data_dict[key] = value

    return data_dict

def hash_file(path):
    """Return the md5 hash for the file at the given path. Return None if file doesn't exist.

    Parameters:
    path (str): The absolute path to the file to hash.

    Returns:
    str: The hash for the file.
    """
    if os.path.isfile(path):
        with open(path, 'rb') as file_obj:
            hash = hash_bytes(file_obj.read())
        return hash
    else:
        return

def hash_bytes(bytes):
    """Hash the given bytes.

    Parameters:
    bytes (bytes): The bytes to has.

    Returns:
    str: The hash for the bytes.
    """
    hasher = hashlib.md5()
    hasher.update(bytes)
    hash = hasher.hexdigest()
    return hash
