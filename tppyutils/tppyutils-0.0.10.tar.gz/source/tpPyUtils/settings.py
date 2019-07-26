#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains different classes to handle settings
"""

from __future__ import print_function, division, absolute_import

import os
import sys
import ast
import time
from collections import OrderedDict

if sys.version_info[:2] > (2, 7):
    from importlib import configparser as ConfigParser
else:
    import ConfigParser

from tpPyUtils import fileio, path, jsonio


class FileSettings(object):
    def __init__(self):
        self.directory = None
        self.file_path = None

        self.settings_dict = OrderedDict()
        self.write = None

    # region Public Functions
    def data(self):
        """
        Return data dictonary contained in the settings
        :return: dict
        """

        return self.settings_dict

    def get(self, name, default=None):
        """
        Get a stored setting
        :param name: str, name of the setting to retrieve. Returns None, if setting is not found
        :param name: default, variant, default value to return if setting is not found
        :return: variant, None || str
        """

        if name in self.settings_dict:
            return self.settings_dict[name]

        if default is not None:
            return default

    def set(self, name, value):
        """
        Set the value of a specific setting. If the setting does not exists, the setting is created with the
        given value
        :param name: str, name of the setting
        :param value: varinat, value of the setting
        """

        self.settings_dict[name] = value
        self._write()

    def get_settings(self):
        """
        Returns a list with all the settings stored
        :return: list<list<str, variant>>
        """

        found = list()
        for setting in self.settings_dict.keys():
            found.append([setting, self.settings_dict[setting]])

        return found

    def get_file(self):
        """
        Retuns the file path of the settings file
        :return: str
        """

        return self.file_path

    def set_directory(self, directory, filename='settings.cfg'):
        """
        Set the file that is used to stored settins on file
        :param directory: str
        :param filename: str
        :return: str
        """

        self.directory = directory
        self.file_path = fileio.create_file(filename=filename, directory=directory)
        self._read()

        return self.file_path

    def has_setting(self, name):
        """
        Returns if a specific name is stored
        :param name: str, name of the setting
        :return: bool
        """

        return name in self.settings_dict

    def has_settings(self):
        """
        Returns if there are settings stored or not
        :return: bool
        """

        if self.settings_dict:
            return True
        return False

    def reload(self):
        """
        Forces the reading of the settings
        """

        self._read()

    def clear(self):
        """
        Cleans the stored settings
        """

        self.settings_dict = OrderedDict()
        self._write()
    # endregion

    # region Private Functions
    def _read(self):
        """
        Internal function used to read settings from file
        """
        if not self.file_path:
            return

        lines = fileio.get_file_lines(self.file_path)
        if not lines:
            return

        self.settings_dict = OrderedDict()

        for line in lines:
            if not line:
                continue
            split_line = line.split('=')
            name = split_line[0].strip()
            value = split_line[-1]
            if not value:
                continue
            value = path.clean_path(value)
            try:
                value = eval(str(value))
            except Exception:
                value = str(value)

            self.settings_dict[name] = value

    def _write(self):
        """
        Internal function that writes stored settings into text file
        """

        lines = list()
        for key in self.settings_dict.keys():
            value = self.settings_dict[key]
            if type(value) == str or type(value) == unicode:
                value = '"{}"'.format(value)
            if value is None:
                value = 'None'
            line = '{0} = {1}'.format(key, str(value))
            lines.append(line)

        write = fileio.FileWriter(file_path=self.file_path)
        try:
            write.write(lines)
        except Exception:
            sys.utils_log.debug('Impossible to write in {}'.format(self.file_path))
            time.sleep(.1)
            write.write(lines)


class JSONSettings(FileSettings, object):
    def __init__(self, directory=None, filename='settings.json'):
        super(JSONSettings, self).__init__()
        if directory:
            self.set_directory(directory, filename if filename and filename.endswith('.json') else 'settings.json')

    def set_directory(self, directory, filename='settings.json'):
        self.directory = directory

        # Check that given file name is a valid JSON file
        if not filename.endswith('.json'):
            old = path.join_path(directory, filename)
            if path.is_file(old):
                self.file_path = old
                self._read()
                return

        self.file_path = fileio.create_file(filename=filename, directory=directory)

        self._read()

        return self.file_path

    def _write(self):
        """
        Override function to add support to write JSON files
        """

        file_path = self._get_json_file()
        if not file_path:
            return

        writer = fileio.FileWriter(file_path)
        writer.write_json(self.settings_dict.items())

    def _read(self):
        """
        Override function to add support to read JSON files
        """

        if not self._has_json_file():
            self.settings_dict = OrderedDict()
            return

        file_path = self._get_json_file()
        if not file_path:
            return
        self.file_path = file_path

        try:
            data = OrderedDict(jsonio.read_file(file_path))
        except Exception:
            self.settings_dict = OrderedDict()
            return

        self.settings_dict = data

    def _get_json_file(self):
        """
        Internal function that returns JSON file where settings are stored
        :return: str
        """

        if not self.file_path:
            return

        settings_directory = path.get_dirname(self.file_path)
        name = path.get_basename(self.file_path, with_extension=False)
        file_path = fileio.create_file(name+'.json', settings_directory)
        if not file_path:
            test_path = path.join_path(settings_directory, name+'.json')
            if path.is_file(test_path):
                file_path = test_path

        return file_path

    def _has_json_file(self):
        """
        Checks if the JSON file where settings should be stored exists or not
        :return: bool
        """

        if not self.file_path:
            return False

        settings_directory = path.get_dirname(self.file_path)
        name = path.get_basename(self.file_path, with_extension=False)
        file_path = path.join_path(settings_directory, name+'.json')
        if path.is_file(file_path):
            return True

        return False


class INISettings(object):
    def __init__(self, filename):
        """
        Constructor
        :param filename: str, INI filename
        """

        self._file = filename
        self._parser = ConfigParser.RawConfigParser()
        self._is_dirty = False
        try:
            self._parser.read(self._file)
        except Exception:
            sys.utils_log.warning('Impossible to read INI config file "{}"'.format(filename))
        self._section = list()

    def __enter__(self):
        """
        Utility function to be used with Python 'with' functino
        """

        return self

    def __exit__(self, type_, value, tb):
        """
        Utility function bo be used with Python 'with' function. Release the raw file and parser
        """

        self.close()
        return False

    def get_section(self):
        """
        Returns the current stack's section
        """

        return self._section[len(self._section) - 1].upper() if self._section else None

    section = property(get_section)

    def save(self):
        """
        Writes INI file to disk
        """

        if self._is_dirty:
            if not os.path.exists(os.path.dirname(self._file)):
                os.makedirs(os.path.dirname(self._file))

            with open(self._file, 'w') as f:
                self._parser.write(f)

        self._is_dirty = False

    def show_in_explorer(self):
        """
        Displays the INI file explorer
        """

        import subprocess
        subprocess.Popen(r'explorer /select, {0}'.format(self._file))

    def get(self, section, option, default, eval_=False):
        """
        Returns the value associated with a key in a section
        :param section: str, section containing the key
        :param option: str, key to use in retrieval
        :param default: object, value to use if the key is not defined
        :param eval_: bool, if True, will attempt to evaluate the string returned into a Python type
        :return: variant, associated value if successful; value passed in as default otherwise
        """

        if self._parser.has_section(section) and self._parser.has_option(section, option):
            if isinstance(default, bool):
                return self._parser.getboolean(section, option)
            if isinstance(default, float):
                return self._parser.getfloat(section, option)
            if isinstance(default, (int, long)):
                return self._parser.getint(section, option)
            if eval_:
                return ast.literal_eval(self._parser.get(section, option))
            return self._parser.get(section, option)
        return default

    def set(self, section, option, value):
        """
        Sets the value with an associated key in the respective section
        :param section: str, section containing the key
        :param option: str, key to use in storing the value
        :param value: object, value to store
        """

        if section:
            if not self._parser.has_section(section):
                self._parser.add_section(section)
            self._parser.set(section, option, str(value))
            self._is_dirty = True

    def remove(self, section, option):
        """
        Removes a key in a section
        :param section: str, section containing the key
        :param option: str, key to remove
        :return: bool, True if successful or False, otherwise
        """

        success = False
        if section:
            if self._parser.has_section(section):
                success = self._parser.remove_option(section, option)

        if success:
            self._is_dirty = True

        return success

    def push_section(self, section):
        """
        Pushes a new section onto the section stack
        :param section: str, INI section to push
        :return: str
        """

        self._section.append(section)

    def pop_section(self):
        """
        Removes the current section from the section stack
        :return: str
        """

        self._section.pop()

    def import_option(self, option, default, eval_=False):
        """
        Returns the value associated with a key in the section at the top of the section stack
        :param option: str, key to use in retrieval
        :param default: str, value to use if the key is not defined
        :param eval_: bool, if True, will attempt to evaluate the string returned into a Python type
        :return: associated value if successful or the value passed in as default otherwise
        """

        return self.get(self.section, option, default, eval_)

    def delete_option(self, option):
        """
        Removes the associated key in the section at the top of the section stack
        :param option: key to use in storing the value
        """

        return self.remove(self.section, option)

    def export_option(self, option, value):
        """
        Sets the value with an associated key in the section at the top of the stack's section
        :param option: str, key to use in storing the value
        :param value: value to store
        """

        self.set(self.section, option, value)

    def close(self):
        """
        Closes INI file
        """

        self.save()
        self._parser = None
