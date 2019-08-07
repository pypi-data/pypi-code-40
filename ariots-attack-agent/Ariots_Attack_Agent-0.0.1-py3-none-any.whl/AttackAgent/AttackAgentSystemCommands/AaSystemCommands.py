from venv.AaSystem.Colors import PrintRed
import time


WaitRequestConversionsFromSeconds = {
    "-s": 1,
    "-m": 60,
    "-h": 3600,
    "-d": 86400
}


class AaSystemCommands:
    def Wait(self, request):
        if not request or len(request) < 2:
            PrintRed(f"Missing system command parameters")
            return

        requestedTimeType = request[0]
        waitTimeRequested = request[1]

        if requestedTimeType not in WaitRequestConversionsFromSeconds.keys():
            PrintRed(f"Requested wait type '{requestedTimeType}' not valid type")
            return

        try:
            WaitTime = float(waitTimeRequested) * WaitRequestConversionsFromSeconds[requestedTimeType]
        except ValueError:
            PrintRed("The Wait time entered is not a valid number")
            return

        time.sleep(WaitTime)


class AaSystemCommandsHelp:
    def Wait(self, request):
        print("Sleeps for a requested amount of time"
              "Command parameters: [WaitTimeType] [WaitTime]\n"
              "'WaitTimeType' - The time format that for the WaitTime parameter, available options:\n"
              "     -s: seconds\n"
              "     -m: minutes\n"
              "     -h: hours\n"
              "     -d: days\n"
              "'WaitTime: The amount of time that will be waited'")


def AaSystemCommandsSwitch(helpRequested=False):
    commands = AaSystemCommands() if not helpRequested else AaSystemCommandsHelp()
    switchOptions = {
        'wait': commands.Wait
    }

    return switchOptions


def HelpRequested(availableCommands):
    print("sc: Stands for System Commands. sc run system and program functions such as waiting, changing system "
          "variables and more\n"
          "The available system commands are:")
    for command in availableCommands:
        print(f"    {command}")
    print("For more information on a command add -help after a command, i.e.: '-sc wait -help'")


def RunAaSystemCommand(request):
    if not request:
        PrintRed(f"No Attack Agent system command to execute passed in parameters")
        return
    command = str.lower(request[0])
    availableAaSystemCommands = AaSystemCommandsSwitch().keys()
    if command == "-help":
        HelpRequested(availableAaSystemCommands)
        return
    if command not in availableAaSystemCommands:
        PrintRed(f"No such Attack Agent system command: '{command}'")
        return
    AaSystemCommandHelpRequested = "-help" in request
    AaSystemCommandsSwitch(AaSystemCommandHelpRequested)[command](request[1:])
