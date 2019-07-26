try:
   import simplejson
except:
   import json as simplejson

import os, sys, getpass, re

class BaseConfigError(Exception):
   def __init__(self, key, value, config):
      self.key = key
      self.value = value
      self.config = config

class InvalidConfig(BaseConfigError):
   def __str__(self):
      return str('Invalid config syntax in "%s" on "%s" with "%s" value.' % (self.config, self.key, self.value))

class FileDoesNotExist(BaseConfigError):
   def __str__(self):
      return str('File does not exist "%s". Check config in "%s" on "%s".' % (self.value, self.config, self.key))

class Settings(object):
   __base_path = None
   __object = None
   __services = None
   __config = {}
   __config_paths = {}

   def __new__(cls, *args, **kwargs):
      if Settings.__object is None:
         Settings.__object = object.__new__(cls)
         Settings.__object.__set_class(*args, **kwargs)

      elif "path" in kwargs and kwargs['path'] is not None:
         Settings.__object = object.__new__(cls)
         Settings.__object.__set_class(*args, **kwargs)

      return Settings.__object

   def __init__(self, path=None, verify=None):
      self.setup()

   def __set_class(self, path=None, verify=None):
      if path is None:
         path = Settings.__base_path
      else:
         Settings.__base_path = path

      if verify == None:
         self.verify = True
      else:
         self.verify = False

      Settings.__base_path = path

      Settings.__config_paths = self.__find_configs()
      Settings.__services = self.__services

      Settings.__config = {}
      self.__load()
      self.setup()

   def setup(self):
      self.__config_paths = Settings.__config_paths
      self.__config = Settings.__config
      self.__services = Settings.__services
      self.__bath_path = Settings.__base_path

   def get_service(self, service=None):
      if service != None:
         found = False
         for i in self.__services:
            if service == i:
               found = True

         if not found:
            if service in self.__config.keys():
               return [i for i in self.__config[service].keys() if i != "multiple"]
         else:
            return service

      return self.__services

   def get_actions(self, service):
      actions = {
         "start": {
            "default": True,
         },
         "restart": {
            "default": True,
         },
         "stop": {
            "default": True,
         },
         "update": {
            "default": True
         }
      }

      path = "%s/docker/actions/%s" % (self.__base_path, service)

      try:
         for i in os.listdir(path):
            regex = re.compile(r'(.+)?\.+')
            match = regex.search(i)

            if match != None and len(match.groups()) > 0:
               a = match.groups()[0]
               actions[a] = {
                  'default': False,
                  'cmd': "sh /home/container/actions/%s" % i
               }
         return actions

      except OSError:
         return actions

   def list_applications(self):
      return self.__config['cli']['applications']

   def __find_configs(self):
      path = "%s/settings/" % self.__base_path

      services = [i.replace(".json", "") for i in os.listdir(path) if "settings" not in i and "common" not in i]

      configs = {}
      for i in services:
         service = i.split("_")

         if len(service) > 1:
            if service[0] not in configs.keys():
               configs[service[0]] = {
                  service[1]: "%s/%s.json" % (path, i),
                  'multiple': True,
               }
            else:
               configs[service[0]][service[1]] = "%s/%s.json" % (path, i)

         else:
            configs[service[0]] = "%s/%s.json" % (path, i)

      self.__services = services

      return configs

   def __load(self):
      for i in list(self.__config_paths.keys()):
         path = self.__config_paths[i]
         
         if isinstance(path, dict):
            self.__config[i] = {}
            
            for j in list(path.keys()):
               self.__config[i][j] = self.__load_config(path[j])

         if isinstance(path, str):
            self.__config[i] = self.__load_config(path)

   def __load_config(self, path):
      try:
         with open(path) as target:
            try:
               return simplejson.load(target)

            except:
               return {"error": "JSON parsing error"}

      except IOError:
         return {"error": "Failed to load file"}

   def get_num_cores(self, config_type=None, get_range=False):
      configs = self.get_config()

      cores = {}
      for service, config_value in configs.items():
         if "num_cores" in config_value.keys():
            cores[service] = config_value['num_cores']
         else:
            cores[service] = 0

      num_cores = self.__set_num_cores(cores)

      if config_type == None:
         output = {}
         for key, value in num_cores.items():
            if get_range:
               output[key] = value['str']
            else:
               output[key] = value['int']

         return output

      else:
         if get_range:
            output = num_cores[config_type]['str']
            if output == "0-0":
               return None
            else:
               return output
         else:
            return num_cores[config_type]['int']

   def __set_num_cores(self, cores):
      output = {}

      start = 0
      for service, value in cores.items():
         output[service] = {
            "int": value,
         }

         if value != 0:
            if value == 1:
               output[service]["str"] = "%d" % (start)
            else:
               output[service]["str"] = "%d-%d" % (start, value + start - 1)
            start += value
         else:
            output[service]["str"] = "0-0"

      return output

   def get_config(self, config_type=None):
      output = {}

      if config_type is not None and config_type in list(self.__config.keys()):
         for key, value in list(self.__config[config_type].items()):
            output[key] = value

            if (isinstance(value, str) and value[0] == "/") or (isinstance(value, dict)):
               output_key, output_value = self.__process_config(key, value, config_type)
               output[output_key] = output_value

         return output

      else:
 
         for config_type in list(self.__config.keys()):
            tmp = {}

            for key, value in list(self.__config[config_type].items()):
               tmp[key] = value

               if (isinstance(value, str) and value[0] == "/") or (isinstance(value, dict)):
                  output_key, output_value = self.__process_config(key, value, config_type)
                  tmp[output_key] = output_value

            output[config_type] = tmp

         return output

      return self.__config

   def __process_config(self, key, value, config_type):
      if isinstance(value, list):
         parsed_path = []

         for i in value:
            path = os.path.abspath(os.path.join(self.__base_path, i))
            parsed_path.append(path)

            if self.verify:
               if value.get("verify") in (None, True) and not os.path.exists(path) and "pid" not in path and ("log" not in path and "debug" not in path):
                  try:
                     raise FileDoesNotExist(key, path, config_type)

                  except FileDoesNotExist as e:
                     print(e.value)
                     sys.exit()

         output_value = " ".join(parsed_path)

      elif isinstance(value, dict) and ("rel" in value or "abs" in value):
         output_value = value['path']

         path = None

         if "rel" in value:
            if len(output_value) > 1:
               path = os.path.abspath(os.path.join(self.__base_path, output_value))

            else:
               path = os.path.abspath(self.__base_path)

         else:
            path = os.path.abspath(output_value)

            if self.verify:
               if value.get("verify") in (None, True) and not os.path.exists(path) and "pid" not in path:
                  try:
                     raise FileDoesNotExist(key, path, config_type)

                  except FileDoesNotExist as e:
                     print(e)
                     sys.exit()

         output_value = path

         value = output_value
      
      elif isinstance(value, dict):
         new_value = {}
         for k, v in value.items():
            new_key, new_value[new_key] = self.__process_config(k, v, config_type)

         return key, new_value

      return key, value

   def get_environ_set(self, **kwargs):
      environ = {}

      if 'environ' in kwargs and isinstance(kwargs['environ'], dict):
         environ = kwargs['environ']

      for config_type in list(self.__config_paths.keys()):
         for key, value in list(self.__config[config_type].items()):
            base_key = "WEBPLATFORM_" + config_type.upper() + "_" + key.replace("-", "_").upper()

            if (isinstance(value, str) and value[0] == "/") or (isinstance(value, dict) and config_type != "mongodb"):
               environ_key, environ_value = self.__process_config(base_key, value, self.__config_paths[config_type])
               environ[environ_key] = environ_value

            else:
               if isinstance(value, list):
                  environ[base_key] = str(" ".join(value))

               elif config_type == "nodejs" and key == "port":
                  environ[base_key] = str(value)

               else:
                  environ_key = "_" + config_type.upper() + "_"  + key.replace("-", "_").upper()
                  environ[base_key] = str(value)

      return environ

   def get_path(self):
      return self.__base_path
