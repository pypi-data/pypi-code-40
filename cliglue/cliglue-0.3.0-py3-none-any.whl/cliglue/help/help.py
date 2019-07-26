import sys
from typing import List, Set, Optional

from dataclasses import dataclass

from cliglue.builder.rule import PrimaryOptionRule, ParameterRule, FlagRule, CliRule, SubcommandRule, \
    PositionalArgumentRule, ManyArgumentsRule, DictionaryRule
from cliglue.parser.context import RunContext
from cliglue.parser.error import CliError
from cliglue.parser.keyword import format_var_names
from cliglue.parser.parser import Parser
from cliglue.parser.transform import filter_rules


@dataclass
class _OptionHelp(object):
    cmd: str
    help: str
    parent: '_OptionHelp' = None


internal_options = {'--bash-install', '--bash-autocomplete'}


def print_help(rules: List[CliRule], app_name: str, version: str, help: str, subargs: List[str], hide_internal: bool):
    helps = generate_help(rules, app_name, version, help, subargs, hide_internal)
    print('\n'.join(helps))


def generate_help(rules: List[CliRule], app_name: str, version: str, help: str, subargs: List[str],
                  hide_internal: bool) -> List[str]:
    available_subcommands = filter_rules(rules, SubcommandRule)
    try:
        run_context: Optional[RunContext] = Parser(rules, dry=True).parse_args(subargs)
        all_rules: List[CliRule] = run_context.active_rules
        active_subcommands: List[SubcommandRule] = run_context.active_subcommands
        precommands: List[str] = [_subcommand_short_name(rule) for rule in active_subcommands]
        if active_subcommands:
            available_subcommands = filter_rules(active_subcommands[-1].subrules, SubcommandRule)
    except CliError:
        all_rules: List[CliRule] = rules
        precommands: List[str] = []

    return generate_subcommand_help(all_rules, app_name, version, help, precommands, available_subcommands,
                                    hide_internal)


def generate_subcommand_help(
        all_rules: List[CliRule],
        app_name: str,
        version: str,
        help: str,
        precommands: List[str],
        subcommands: List[SubcommandRule],
        hide_internal: bool,
) -> List[str]:
    flags = filter_rules(all_rules, FlagRule)
    parameters = filter_rules(all_rules, ParameterRule)
    primary_options = filter_rules(all_rules, PrimaryOptionRule)
    pos_arguments = filter_rules(all_rules, PositionalArgumentRule)
    many_args = filter_rules(all_rules, ManyArgumentsRule)
    dicts = filter_rules(all_rules, DictionaryRule)

    options: List[_OptionHelp] = _generate_options_helps(all_rules, hide_internal)
    commands: List[_OptionHelp] = _generate_commands_helps(subcommands)

    out = []
    # App info
    app_info = app_help_info(app_name, help, version)
    if app_info:
        out.append(app_info + '\n')

    # Usage
    app_bin_prefix = ' '.join([sys.argv[0]] + precommands)
    usage_syntax: str = app_bin_prefix

    if commands:
        usage_syntax += ' [COMMAND]'

    if flags or parameters or primary_options or dicts:
        usage_syntax += ' [OPTIONS]'

    usage_syntax += usage_positional_arguments(pos_arguments)
    usage_syntax += usage_many_arguments(many_args)

    out.append(f'Usage:\n  {usage_syntax}')

    if options:
        out.append('\nOptions:')
        __helpers_output(options, out)

    if commands:
        out.append('\nCommands:')
        __helpers_output(commands, out)
        out.append(f'\nRun "{app_bin_prefix} COMMAND --help" for more information on a command.')

    return out


def app_help_info(app_name: str, help: str, version: str) -> Optional[str]:
    info = app_name_version(app_name, version)
    if help:
        if info:
            info += ' - '
        info += help
    return info


def app_name_version(app_name, version):
    info = ''
    if app_name:
        info += app_name
    if version:
        version = _normalized_version(version)
        if info:
            info += ' '
        info += version
    return info


def __helpers_output(commands, out):
    padding = _max_name_width(commands)
    for helper in commands:
        name_padded = helper.cmd.ljust(padding)
        if helper.help:
            out.append(f'  {name_padded} - {helper.help}')
        else:
            out.append(f'  {name_padded}')


def print_version(app_name: str, version: str):
    print(app_name_version(app_name, version))


def _normalized_version(version: str) -> str:
    if version.startswith('v'):
        return version
    return f'v{version}'


def _max_name_width(helps: List[_OptionHelp]) -> int:
    return max(map(lambda h: len(h.cmd), helps))


def _generate_options_helps(rules: List[CliRule], hide_internal: bool) -> List[_OptionHelp]:
    # filter non-empty
    return list(filter(lambda o: o, [_generate_option_help(rule, hide_internal) for rule in rules]))


def _generate_option_help(rule: CliRule, hide_internal: bool) -> Optional[_OptionHelp]:
    if isinstance(rule, PrimaryOptionRule):
        return _primary_option_help(rule, hide_internal)
    elif isinstance(rule, FlagRule):
        return _flag_help(rule)
    elif isinstance(rule, ParameterRule):
        return _parameter_help(rule)
    elif isinstance(rule, DictionaryRule):
        return _dictionary_help(rule)


def _generate_commands_helps(rules: List[CliRule], parent: _OptionHelp = None, subrules: List[CliRule] = None
                             ) -> List[_OptionHelp]:
    commands: List[_OptionHelp] = []
    if not subrules:
        subrules = []
    for rule in rules:
        if isinstance(rule, SubcommandRule):
            subsubrules = subrules + rule.subrules
            helper = _subcommand_help(rule, parent, subsubrules)
            if rule.run or rule.help:
                commands.append(helper)
            commands.extend(_generate_commands_helps(rule.subrules, helper, subsubrules))
    return commands


def _subcommand_help(rule: SubcommandRule, parent: _OptionHelp, subrules: List[CliRule]) -> _OptionHelp:
    pos_args = filter_rules(subrules, PositionalArgumentRule)
    all_args = filter_rules(subrules, ManyArgumentsRule)
    cmd = _subcommand_prefix(parent) + '|'.join(sorted_keywords(rule.keywords))
    cmd += usage_positional_arguments(pos_args)
    cmd += usage_many_arguments(all_args)
    return _OptionHelp(cmd, rule.help, parent)


def _subcommand_prefix(helper: _OptionHelp) -> str:
    if not helper:
        return ''
    return helper.cmd + ' '


def _primary_option_help(rule: PrimaryOptionRule, hide_internal: bool) -> Optional[_OptionHelp]:
    if hide_internal:
        for keyword in rule.keywords:
            if keyword in internal_options:
                return None
    cmd = ', '.join(sorted_keywords(rule.keywords))
    pos_args = filter_rules(rule.subrules, PositionalArgumentRule)
    all_args = filter_rules(rule.subrules, ManyArgumentsRule)
    cmd += usage_positional_arguments(pos_args)
    cmd += usage_many_arguments(all_args)
    return _OptionHelp(cmd, rule.help)


def _flag_help(rule: FlagRule) -> _OptionHelp:
    cmd = ', '.join(sorted_keywords(rule.keywords))
    return _OptionHelp(cmd, rule.help)


def _parameter_help(rule: ParameterRule) -> _OptionHelp:
    cmd = ', '.join(sorted_keywords(rule.keywords)) + ' ' + _param_var_name(rule)
    return _OptionHelp(cmd, rule.help)


def _dictionary_help(rule: DictionaryRule) -> _OptionHelp:
    cmd = ', '.join(sorted_keywords(rule.keywords)) + ' KEY VALUE'
    return _OptionHelp(cmd, rule.help)


def _param_var_name(rule: ParameterRule) -> str:
    if rule.name:
        return rule.name.upper()
    else:
        # get name from longest keyword
        names: Set[str] = format_var_names(rule.keywords)
        return max(names, key=lambda n: len(n)).upper()


def _argument_var_name(rule: PositionalArgumentRule) -> str:
    return rule.name.upper()


def _subcommand_short_name(rule: SubcommandRule) -> str:
    return next(iter(rule.keywords))


def sorted_keywords(keywords: Set[str]) -> List[str]:
    # shortest keywords first, then alphabetically
    return sorted(keywords, key=lambda k: (len(k), k))


def display_positional_argument(rule: PositionalArgumentRule) -> str:
    var_name = _argument_var_name(rule)
    if rule.required:
        return f' {var_name}'
    else:
        return f' [{var_name}]'


def display_all_arguments(rule: ManyArgumentsRule) -> str:
    arg_name = rule.name.upper()
    return f' [{arg_name}...]'


def usage_positional_arguments(rules: List[PositionalArgumentRule]) -> str:
    return ''.join([display_positional_argument(rule) for rule in rules])


def usage_many_arguments(rules: List[ManyArgumentsRule]) -> str:
    return ''.join([display_all_arguments(rule) for rule in rules])
