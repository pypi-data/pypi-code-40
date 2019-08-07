class CommandLineColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDCOLOR = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def PrintHeader(text):
    print(f"{CommandLineColors.HEADER}{text}{CommandLineColors.ENDCOLOR}")


def PrintBlue(text):
    print(f"{CommandLineColors.OKBLUE}{text}{CommandLineColors.ENDCOLOR}")


def PrintGreen(text):
    print(f"{CommandLineColors.OKGREEN}{text}{CommandLineColors.ENDCOLOR}")


def PrintOrange(text):
    print(f"{CommandLineColors.WARNING}{text}{CommandLineColors.ENDCOLOR}")


def PrintRed(text):
    print(f"{CommandLineColors.FAIL}{text}{CommandLineColors.ENDCOLOR}")


def PrintBold(text):
    print(f"{CommandLineColors.BOLD}{text}{CommandLineColors.ENDCOLOR}")


def PrintUnderline(text):
    print(f"{CommandLineColors.UNDERLINE}{text}{CommandLineColors.ENDCOLOR}")