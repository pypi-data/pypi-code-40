import queue


commandQueue = queue.Queue()
tempQueue = queue.Queue()


def CommandQueueNotEmpty():
    return not commandQueue.empty()


def EnqueueCommand(command):
    commandQueue.put(command)


def EnqueueCommands(commands):
    for command in commands:
        commandQueue.put(command)


def EnqueueCommandsNext(commands):
    while not commandQueue.empty():
        tempQueue.put(commandQueue.get())
    for command in commands:
        commandQueue.put(command)
    while not tempQueue.empty():
        commandQueue.put(tempQueue.get())


def DeQueueCommand():
    if CommandQueueNotEmpty():
        return commandQueue.get()
    else:
        return None


def EmptyCommandQueue():
    while not commandQueue.empty():
        commandQueue.get()
