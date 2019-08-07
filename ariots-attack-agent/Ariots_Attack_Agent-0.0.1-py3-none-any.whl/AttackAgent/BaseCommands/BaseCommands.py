from venv.AttackAgent.BatchCommands.BatchCommandHandler import AddCommandsBatch
from venv.AttackAgent.Bash.BashCommands import RunBashCommand
from venv.AttackAgent.AttackAgentSystemCommands.AaSystemCommands import RunAaSystemCommand


def AddBatchCommands(request):
    AddCommandsBatch(request)


def BashAttackCommand(request):
    RunBashCommand(request)


def AaSystemCommand(request):
    RunAaSystemCommand(request)


CommandsSwitch = {
    "ba": BashAttackCommand,
    "run": AddCommandsBatch,
    "sc": AaSystemCommand
}
