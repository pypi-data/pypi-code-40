import shlex


def ParseRequest(userInput):
    return shlex.split(userInput)