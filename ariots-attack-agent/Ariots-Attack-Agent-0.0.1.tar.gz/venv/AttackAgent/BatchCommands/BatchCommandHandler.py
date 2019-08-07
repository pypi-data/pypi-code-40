from venv.AaSystem.Colors import PrintRed
import ntpath
from venv.AttackAgent.BaseCommands.CommandQueue import EnqueueCommandsNext
from os import listdir
from os.path import isfile, join

SupportedRequestTypes = ["-help", "-f", "-p"]
PreMadeBatchCommandsPath = "venv\\AttackAgent\\BatchCommands\\Scripts\\"


def GetAllPreMadeBatchNames():
    return [f for f in listdir(PreMadeBatchCommandsPath) if isfile(join(PreMadeBatchCommandsPath, f))]


def HelpRequested():
    print("Command parameters: run [-f] [filePath]\n"
          "                    run [-p] [CommandsBatchName]"
          "run: References text files containing a row delimited list of commands to run, places these commands at "
          "the front of the queue\n"
          "     '-f' - Indicates you will pass a file path to the batch command file, this will be followed by the"
          "filePath parameter\n"
          "     '-p' - Indicating you wish to use one of the pre made batch command scripts, will be followed by the"
          "CommandsBatchName parameter\n"
          "     'filePath' - the full path to the batch command file - "
          "The batch file referenced must contain only commands as provided when normally calling "
          "the attack agent\n"
          "     'CommandsBatchName' - The name of the pre made batch commands script, the available batch commands are:")
    for commandName in GetAllPreMadeBatchNames():
        print(f"            {commandName}")
    print("Each command must be separated by a new line\n"
          "It is possible to recursively add additional batch -run calls using a batch file"
          "Lines in Command Batch Files can be commented out by adding # to the start of the line")


def AddCommandsBatch(request):
    if not request:
        PrintRed("Missing parameters in request")
        return

    requestType = request[0]

    if requestType not in SupportedRequestTypes:
        PrintRed(f"No such batch command type: '{requestType}'")
        return

    if requestType == "-help":
        HelpRequested()
        return

    if len(request) < 2:
        PrintRed("Missing parameters in request")
        return

    filePath = request[1]

    if requestType == "-p":
        if filePath not in GetAllPreMadeBatchNames():
            PrintRed(f"No such PreMade batch command: '{filePath}'")
            return
        filePath = f"{PreMadeBatchCommandsPath}{filePath}"
    try:
        with open(filePath, "r") as file:
            commandLines = list(filter(lambda a: not a.startswith('#'), list(file.read().splitlines())))
            print(f"Adding {len(commandLines)} Commands from {ntpath.basename(filePath)}")
            EnqueueCommandsNext(commandLines)
        file.close()
    except Exception as ex:
        print(f"Failed to load command batch file, exception encountered:\n")
        PrintRed(ex)

