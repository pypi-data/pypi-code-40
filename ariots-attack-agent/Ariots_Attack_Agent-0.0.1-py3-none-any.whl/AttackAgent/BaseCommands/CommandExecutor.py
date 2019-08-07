from venv.AaSystem.Colors import PrintRed, PrintBlue
from venv.AttackAgent.BaseCommands.BaseCommands import *
from venv.AttackAgent.BaseCommands.CommandQueue import CommandQueueNotEmpty, DeQueueCommand, EmptyCommandQueue
from venv.AttackAgent.BaseCommands.RequestBuilder import ParseRequest


def RunCommands():
    while CommandQueueNotEmpty():
        command = DeQueueCommand()
        request = ParseRequest(command)
        success = PerformRequest(request)
        if not success:
            EmptyCommandQueue()
            return


def HelpRequested():
    print("All commands follow the format - [CommandType] [CommandsParameter] [CommandsParameter] ...\n"
          "Type -help with any CommandType for more information on that command\n\n"
          "Available CommandsTypes:\n"
          "ba: Bash Attacks using bash commands to perform tasks\n"
          "run: References text files containing a row delimited list of commands to run, places these commands at "
          "the front of the queue\n"
          "sc: Attack Agent System Commands - will perform program and environment commands such as waiting, looping, "
          "handling environment variables and so on")


def CommandExists(userInput):
    return userInput in CommandsSwitch.keys()


def PerformRequest(request):
    if not request:
        return False
    command = str.lower(request[0])
    if command == "-help":
        HelpRequested()
        return True
    if not CommandExists(command):
        print(f"No such command '{command}'")
        return False
    try:
        PrintBlue(f"Running Command:    {' '.join(request)}")
        CommandsSwitch[command](request[1:])
        return True
    except Exception as ex:
        print(f"Failed to execute command {command}:\n")
        PrintRed(ex)
        return False

