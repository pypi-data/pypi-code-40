import pprint
import copy
import re

from assemblyline.common.str_utils import is_safe_str, safe_str
from assemblyline.common import forge
from assemblyline.odm.models.signature import RequiredMeta

config = forge.get_config()
cl_engine = forge.get_classification()
yara_externals = {f"al_{i}": i for i in config.system.yara.externals}

REQUIRED_META = list(RequiredMeta.fields().keys())


class YaraCharsetValidationException(Exception):
    def __init__(self, data):
        self.data = data


# noinspection PyUnresolvedReferences
class YaraParser(object):
    STATUSES = ["DEPLOYED", "TESTING", "NOISY", "DISABLED", "STAGING", "INVALID"]
    VALID_YARA_VERSION = ["1.6", "1.7", "2.0", "2.1", "3.0", "3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7", "3.8"]
    RULE_TYPE = ["rule", "private rule", "global private rule", "global rule"]
    RULE_GROUPS = ['exploit', 'implant', 'info', 'technique', 'tool']
    RULE_IMPORTANT = ['description', 'organisation', 'poc', 'rule_id', 'rule_version', 'yara_version']
    RULE_DEFAULT = {"depends": [], "comments": [], "meta": {"al_status": "TESTING"}, "meta_extra": {}, "strings": [],
                    "condition": [], "type": None, "name": None, "tags": []}
    YARA_RESERVED_KW = ["all", "and", "any", "ascii", "at", "condition", "contains", "entrypoint", "false",
                        "filesize", "fullword", "for", "global", "in", "import", "include", "index", "indexes",
                        "int8", "int16", "int32", "matches", "meta", "nocase", "not", "or", "of", "private", "rule",
                        "rva", "section", "strings", "them", "true", "uint8", "uint16", "uint32", "wide", "int8be",
                        "int16be", "int32be", "uint8be", "uint16be", "uint32be"]
    AL_RESERVED_KW = yara_externals
    YARA_MODULES = {"1.6": [],
                    "1.7": [],
                    "2.0": [],
                    "2.1": [],
                    "3.0": ["pe", "cuckoo"],
                    "3.1": ["pe", "cuckoo", "magic"],
                    "3.2": ["pe", "cuckoo", "magic", "math", "hash"],
                    "3.3": ["pe", "cuckoo", "magic", "math", "hash", "elf"],
                    "3.4": ["pe", "cuckoo", "magic", "math", "hash", "elf"],
                    "3.5": ["pe", "cuckoo", "magic", "math", "hash", "elf", "dotnet"],
                    "3.6": ["pe", "cuckoo", "magic", "math", "hash", "elf", "dotnet"],
                    "3.7": ["pe", "cuckoo", "magic", "math", "hash", "elf", "dotnet"],
                    "3.8": ["pe", "cuckoo", "magic", "math", "hash", "elf", "dotnet"]}

    CURRENT_YARA_VERSION = "3.8"

    FAKE_RULE = "rule %s { condition: \"THIS IS A FAKE RULE TO PASS VALIDATION TESTS. IGNORE!\"}"

    BUMP_REQ_FIELDS = [
        'rule_group',
        'implant',
        'exploit',
        'info',
        'technique',
        'tool',
        'organisation',
        'rule_id',
        'rule_version',
        'al_configdumper',
        'al_configparser'
    ]
        
    def __init__(self):
        
        self.in_rule = False
        self.in_comment = False
        self.in_meta = False
        self.in_strings = False
        self.in_condition = False
        self.open_bracket = 0
        self.got_open = False
        self.cur_rule = copy.deepcopy(self.RULE_DEFAULT)

    def _reset(self):
        self.cur_rule = copy.deepcopy(self.RULE_DEFAULT)
        self.in_rule = False
        self.in_meta = False
        self.in_strings = False
        self.in_comment = False
        self.in_condition = False
        self.open_bracket = 0
        self.got_open = False
        
    def _switch_to(self, val):
        if val == "meta":
            self.in_meta = True
            self.in_strings = False
            self.in_condition = False
        elif val == "strings":
            self.in_meta = False
            self.in_strings = True
            self.in_condition = False
        elif val == "condition":
            self.in_meta = False
            self.in_strings = False
            self.in_condition = True

    # noinspection PyBroadException
    @staticmethod
    def get_rule_error(rule):
        try:
            import yara
        except Exception:
            return {"type": "ImportError",
                    "line": 0,
                    "error": "Could not test rule. Yara python bindings are not installed."}

        rule_text = YaraParser.dump_rule_file([rule],
                                              fake_dependencies=True,
                                              show_header=False)

        try:
            yara.compile(source=rule_text, externals=yara_externals)
        except yara.Error as e:
            try:
                line, message = e.message.split("): ", 1)
                line = line.split("(", 1)[1]
            except Exception:
                line = "N/A"
                message = e.message
            return {"type": "Error", "line": line, "error": message, "rule_text": rule_text}

        try:
            yara.compile(source=rule_text, externals=yara_externals, error_on_warning=True)
            return None
        except yara.WarningError as w:
            return {"type": "WarningError", "error": str(w), "rule_text": rule_text}

    # noinspection PyUnusedLocal
    @staticmethod
    def custom_bump_rules(rule, old_rule):
        return False

    # noinspection PyUnusedLocal
    @staticmethod
    def custom_validation_rules(rule, al_rule=True):
        return None
    
    @classmethod
    def require_bump(cls, rule, old_rule):
        if old_rule['meta']['al_status'] in ['TESTING', 'STAGING', 'INVALID']:
            return False

        # Test a name change
        if rule['name'] != old_rule['name']:
            return True
        # Test strings changes
        if rule['strings'] != old_rule['strings']:
            return True
        # Test condition changes
        if rule['condition'] != old_rule['condition']:
            return True
        # Test tag changes
        if rule['tags'] != old_rule['tags']:
            return True
        # Test type changes
        if rule['type'] != old_rule['type']:
            return True
        # Test custom rules for validating rule bump
        if cls.custom_bump_rules(rule, old_rule):
            return True

        rule_meta = rule.get('meta', {})
        rule_extra = rule.get('meta_extra', {})
        old_rule_meta = old_rule.get('meta', {})
        old_rule_extra = old_rule.get('meta_extra', {})

        # Check the values of the different fields that warrant a rule bump
        for item in cls.BUMP_REQ_FIELDS:
            # Test field in the meta section
            if rule_meta.get(item, None) != old_rule_meta.get(item, None):
                return True

            # Test field in the extra section
            if rule_extra.get(item, None) != old_rule_extra.get(item, None):
                return True
         
        return False

    @staticmethod
    def path_builder(root, new):
        if not root:
            return new
        else:
            return f"{root}.{new}"

    @classmethod
    def recurse_validate_charset(cls, item, path=None):
        if isinstance(item, dict):
            for k in item.keys():
                cls.recurse_validate_charset(item[k], cls.path_builder(path, k))
        elif isinstance(item, list):
            for i in item:
                cls.recurse_validate_charset(i, path)

        elif isinstance(item, str):
            if not is_safe_str(item):
                raise YaraCharsetValidationException({
                    "valid": False,
                    "field": path,
                    "message": f"Invalid char in string [{repr(item)}]"
                })

    @classmethod
    def validate_rule(cls, rule, al_rule=True):
        # TOP LEVEL
        meta = rule.get("meta", None)
        rtype = rule.get("type", None)
        name = rule.get("name", None)
        tags = rule.get("tags", None)
        strings = rule.get("strings", None)
        comments = rule.get("comments", None)
        conditions = rule.get("condition", None)
        
        if not rtype:
            return {"valid": False, "field": "type", "message": "No type of rule provided"}
        if rtype not in YaraParser.RULE_TYPE:
            return {"valid": False, "field": "type", "message": "Invalid rule type"}
        
        if not name:
            return {"valid": False, "field": "name", "message": "No name of rule provided"}
        if " " in name:
            return {"valid": False, "field": "name", "message": "No space allowed in signature name"}
        if not isinstance(tags, list):
            return {"valid": False, "field": "tags", "message": "Tags field should be an array"}
        if not isinstance(strings, list):
            return {"valid": False, "field": "strings", "message": "Strings field should be an array"}
        if not isinstance(comments, list):
            return {"valid": False, "field": "comments", "message": "Comments field should be an array"}
        if not isinstance(conditions, list):
            return {"valid": False, "field": "conditions", "message": "Conditions field should be an array"}
        if len(conditions) == 0:
            return {"valid": False, "field": "conditions", "message": "There should be at least one condition"}
        
        # META
        if not meta:
            return {"valid": False, "field": "meta", "message": "No meta section"}
        rule_group = meta.get('rule_group', None)
        section = meta.get(rule_group, None)
        description = meta.get('description', None)
        s_id = meta.get('rule_id', None)
        organisation = meta.get('organisation', None)
        poc = meta.get('poc', None)
        rule_version = meta.get('rule_version', None)
        yara_version = meta.get('yara_version', None)
        al_status = meta.get('al_status', None)
        
        if rule_group not in YaraParser.RULE_GROUPS:
            return {"valid": False, "field": "meta.rule_group", "message": "Rule group not valid."}
        
        if section is None or section == "":
            return {"valid": False, "field": f"meta.{rule_group}", "message": f"Missing field meta.{rule_group}"}
        
        if description is None or description == "":
            return {"valid": False, "field": "meta.description", "message": "No description provided"}
        
        if s_id is None or s_id == "":
            return {"valid": False, "field": "meta.rule_id", "message": "No signature ID provided"}
        
        if organisation is None or organisation == "":
            return {"valid": False, "field": "meta.organisation", "message": "No organisation provided"}
        
        if poc is None or poc == "":
            return {"valid": False, "field": "meta.poc", "message": "No point of contact provided"}
        
        if not poc.endswith(f"@{organisation.lower()}"):
            return {"valid": False, "field": "meta.poc",
                    "message": f"Invalid point of contact. Format is userid@{organisation.lower()}"}
        
        if rule_version is None or rule_version == "":
            return {"valid": False, "field": "meta.rule_version", "message": "No rule version provided"}
        
        if yara_version is None or yara_version == "":
            return {"valid": False, "field": "meta.yara_version", "message": "No yara version provided"}

        if yara_version not in YaraParser.VALID_YARA_VERSION:
            return {"valid": False, "field": "meta.yara_version", "message": "Unsupported yara version"}
        
        if al_rule and (al_status is None or al_status == ""):
            return {"valid": False, "field": "meta.al_status", "message": "No status provided"}
        
        if al_rule and al_status not in YaraParser.STATUSES:
            return {"valid": False, "field": "meta.al_status", "message": f"Invalid status {al_status}"}

        # noinspection PyNoneFunctionAssignment
        custom_return = cls.custom_validation_rules(rule, al_rule=True)
        if custom_return:
            return custom_return

        try:
            cls.recurse_validate_charset(rule)
        except YaraCharsetValidationException as e:
            return e.data

        yara_error = YaraParser.get_rule_error(rule)
        if yara_error:
            if yara_error.get("type", None) == "Error":
                return {"valid": False, "field": None, "message": yara_error}
            return {"valid": True, "warning": yara_error.get('error', None)}
        
        return {"valid": True, "warning": None}
    
    @staticmethod
    def parse_dependencies(conditions, modules=None):
        yara_reserved_kw = copy.deepcopy(YaraParser.YARA_RESERVED_KW)
        al_reserved_kw = copy.deepcopy(YaraParser.AL_RESERVED_KW)
        out_depends = []
        out_modules = []
        # Build dependencies
        for c in conditions:
            # Remove comments
            if "/*" in c:
                temp = c[:c.index("/*")]
            elif "//" in c:
                temp = c[:c.index("//")]
            else:
                temp = c

            # Remove static and regex strings for externals/modules

            if '"' in c:
                temp = re.sub('"[^"]+"', '', temp)
            if ' matches ' in c:
                temp = re.sub('matches[ ]+/[^ ]+/[a-zA-Z]{0,4}', '', temp)
                
            # Remove special chars
            temp = temp.replace("(", " ").replace(")", " ").replace("..", " ").replace("<", " ").replace(">", " ").\
                replace("=", " ").replace("+", " ").replace("-", " ").replace("/", " ").replace("*", " ").\
                replace(",", "").replace("!", " ").replace(":", " ").replace("\\", " ").replace("%", " ").\
                replace("&", " ").replace("|", " ").replace("~", " ").replace("^", " ")
            
            in_for = False
            for item in temp.split(" "):
                # Handle for loop in condition
                if item == "for":
                    in_for = True
                    continue
                elif in_for:
                    if item == "in":
                        in_for = False
                    elif item != "all":
                        yara_reserved_kw.append(item)
                    continue
                
                # Filter out reserved KW
                if item in yara_reserved_kw:
                    continue

                # Filter out AL reserved KW
                if item in al_reserved_kw:
                    continue

                # Filter out Strings
                if item.startswith("$") or item.startswith("#") or item.startswith("@") or item.startswith("!"):
                    continue
                
                # Filter out empties
                if item == "":
                    continue
                
                # Filter out string parts
                if '"' in item:
                    continue

                # Filter out anything that starts with a number
                # noinspection PyBroadException
                try:
                    int(item[0])
                    continue
                except Exception:
                    pass

                if modules and "." in item:
                    mod_name = item.split(".", 1)[0]
                    if mod_name in modules:
                        out_modules.append(mod_name)
                        continue
                    elif mod_name == "]":
                        continue

                # Add the remainder to the dependency list
                out_depends.append(item)
                in_for = False
                
        return list(set(out_depends)), list(set(out_modules))

    # noinspection PyTypeChecker
    def parse_rule_file(self, data, debug=False, force_safe_str=False):
        out = []
        for line in data.splitlines():
            if self.in_rule and debug:
                print(line)
                
            line = line.strip()
            
            if line.startswith("/*"):
                self.in_comment = True
            if self.in_comment:
                if "*/" in line:
                    self.in_comment = False
                    # There might be data after the inline comment
                    line = line.split('*/', 1)[1]
                    if not line:
                        continue
                else:
                    continue
            
            if not line.startswith("//") and not self.in_meta and not self.in_strings and not self.in_condition:
                prev_bracket = self.open_bracket
                self.open_bracket += line.count("{")
                if prev_bracket == 0 and self.open_bracket == 1:
                    self.got_open = True

                # Conditions may be on the same line as the curly bracket
                temp_line = line.strip('{').strip()
                if temp_line.startswith("meta"):
                    self._switch_to("meta")
                elif temp_line.startswith("strings"):
                    self._switch_to("strings")
                elif temp_line.startswith("condition"):
                    self._switch_to("condition")

            if self.in_rule and not self.in_meta and not self.in_condition and not self.in_strings \
                    and line.startswith("//"):
                line_data = line[2:].strip()
                if force_safe_str:
                    line_data = safe_str(line_data)
                self.cur_rule['comments'].append(line_data)
                    
            if line.startswith("rule "):
                self.cur_rule['type'] = "rule"
                self.in_rule = True
            elif line.startswith("private rule "):
                self.cur_rule['type'] = "private rule"
                self.in_rule = True
            elif line.startswith("global rule "):
                self.cur_rule['type'] = "global rule"
                self.in_rule = True
            elif line.startswith("global private rule "):
                self.cur_rule['type'] = "global private rule"
                self.in_rule = True 
            
            if line.startswith("rule ") or line.startswith("private rule ") or line.startswith("global private rule "):
                if debug:
                    print(line)
                line = line[len(self.cur_rule['type']) + 1:].split("//")[0]
                self.cur_rule['tags'] = []

                if ":" in line:
                    self.cur_rule['name'], tags = line.split(':')
                    self.cur_rule['name'] = self.cur_rule['name'].strip()
                    tags = tags.split("{")[0].strip().split(" ")
                    for t in tags:
                        if force_safe_str:
                            t = safe_str(t)

                        self.cur_rule['tags'].append(t)
                else:
                    self.cur_rule['name'] = line.split("{")[0].strip()

                if force_safe_str:
                    self.cur_rule['name'] = safe_str(self.cur_rule['name'])
                
            if line.startswith("meta"):
                self._switch_to("meta")
            elif line.startswith("strings"):
                self._switch_to("strings")
            elif line.startswith("condition"):
                self._switch_to("condition")
            elif not line.startswith("}"):
                if self.in_meta and "=" in line:
                    key, val = line.split("=", 1)
                    key = key.strip()
                    val = val.strip().strip('"')
                    if force_safe_str:
                        val = safe_str(val)
                    if key == 'classification':
                        self.cur_rule['classification'] = val
                    elif key in REQUIRED_META:
                        self.cur_rule['meta'][key] = val
                    elif key == 'id':
                        self.cur_rule['meta']['rule_id'] = val
                    else:
                        self.cur_rule['meta_extra'][key] = val
                elif self.in_strings and line != "":
                    if force_safe_str:
                        line = safe_str(line)
                    self.cur_rule['strings'].append(line)
                elif self.in_condition and line != "":
                    if force_safe_str:
                        line = safe_str(line)
                    self.cur_rule["condition"].append(line)

            if not line.startswith("//") and not self.in_meta and not self.in_strings:
                self.open_bracket -= line.count("}")
                if self.got_open and self.open_bracket == 0:
                    if debug: 
                        pprint.pprint(self.cur_rule)
                        print("")
                        print("")

                    yara_version = self.cur_rule.get('meta', {}).get('yara_version', "3.7")
                    modules = self.YARA_MODULES.get(yara_version, [])
                    self.cur_rule['depends'], self.cur_rule['modules'] = \
                        self.parse_dependencies(self.cur_rule['condition'], modules)
                        
                    out.append(self.cur_rule)
                    self._reset()
        
        return out

    @staticmethod
    def dump_rule_file(rule_list, fake_dependencies=False, show_header=True):
        if show_header:
            out = [f"//\t{len(rule_list)} rule(s)", "", ""]
        else:
            out = []

        modules = list(set([m for rule in rule_list for m in rule.get('modules', [])]))
        for m in modules:
            out.append(f'import "{m}"')
            out.append("")

        if fake_dependencies:
            depends = list(set([d for rule in rule_list for d in rule.get('depends', [])]))
            for d in depends:
                out.append(YaraParser.FAKE_RULE % d)
                out.append("")

        for rule in rule_list:
            if rule is None:
                continue

            if len(rule["tags"]) > 0:
                tags = f': {" ".join(rule["tags"])}'
            else:
                tags = ""

            out.append(f'{rule["type"]} {rule["name"]}{tags} {{')
            
            # Do comments
            for c in rule['comments']:
                out.append(f"    // {c}")
            
            # Do meta. Try to preserve ordering
            metadata = rule.get('meta', {})
            metadata.update(rule.get('meta_extra', {}))
            classification = rule.get('classification', None)
            if metadata or classification:
                out.append("    meta:")
                keys = list(metadata.keys())
                do_space = False
                if "rule_group" in keys:
                    out.append(f'        rule_group = "{metadata["rule_group"]}"')
                    keys.remove('rule_group')
                    do_space = True
                for i in YaraParser.RULE_GROUPS:
                    if i in keys:
                        if metadata[i] is None:
                            continue

                        out.append(f'        {i} = "{metadata[i]}"')
                        keys.remove(i)
                        do_space = True
                if do_space:
                    out.append("        ")
                    
                do_space = False
                if classification and cl_engine.enforce:
                    out.append(f'        classification = "{classification}"')
                    do_space = True
                for i in YaraParser.RULE_IMPORTANT:
                    if i in keys:
                        if metadata[i] is None:
                            continue

                        do_space = True
                        out.append(f'        {i} = "{metadata[i]}"')
                        keys.remove(i)
                if do_space:
                    out.append("        ")
                    
                keys.sort()
                for k in keys:
                    if metadata[k] is None:
                        continue

                    out.append(f'        {k} = "{metadata[k]}"')
                    
                out.append("    ")
            
            # Do Strings
            if rule['strings']:
                if len(set(rule['strings'])) > 1 or rule['strings'][0] != "":
                    out.append("    strings:")
                    for s in rule['strings']:
                        out.append(f'        {s}')
                    out.append("    ")
                    
            # Do conditions
            if rule['condition']:
                out.append("    condition:")
                for c in rule['condition']:
                    out.append(f'        {c}')
                
                out.append("    ")
                            
            out.extend(["}", "", ""])
            
        return safe_str("\n".join(out))
