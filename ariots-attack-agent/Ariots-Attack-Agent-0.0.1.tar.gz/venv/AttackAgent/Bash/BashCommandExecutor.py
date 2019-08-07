import subprocess

from venv.AaSystem.Colors import PrintRed


def RunSubProcess(commandLineInput):
    try:
        subprocess.run(commandLineInput, shell=True, check=True)
    except Exception as ex:
        print(f"Failed execute bash command '{commandLineInput}', exception encountered:\n")
        PrintRed(ex)
