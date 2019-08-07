import platform
from venv.AaSystem.Colors import PrintRed
import os

SupportedOsTypes = ["windows", "linux"]
SupportedWindowsOs = ["10"]
SupportedLinuxOs = ["ubuntu"]


def IsSupportedOs(OperatingSystem, OperatingSystemRelease, OperatingSystemVersion):
    if OperatingSystem not in SupportedOsTypes:
        PrintRed(f"Operating system: '{OperatingSystem}' not supported")
        return False
    if OperatingSystem == "windows" and OperatingSystemRelease not in SupportedWindowsOs:
        PrintRed(f"Windows Operating system: '{OperatingSystemRelease}' not supported")
        return False
    if OperatingSystem == "linux" and OperatingSystemRelease not in SupportedLinuxOs:
        PrintRed(f"Linux Operating system: '{OperatingSystemRelease}' not supported")
        return False
    return True


def HasAriotsEnvironmentVariable():
    return str.lower(os.getenv('AriotsAA')) == "true"


def RunningOnPermittedMachine():
    OperatingSystem = str.lower(str(platform.system()))
    OperatingSystemRelease = str.lower(str(platform.release()))
    OperatingSystemVersion = str.lower(str(platform.version()))

    PermittedToRunOnMachine = IsSupportedOs(OperatingSystem, OperatingSystemRelease, OperatingSystemVersion)\
                              and HasAriotsEnvironmentVariable()
    return PermittedToRunOnMachine
