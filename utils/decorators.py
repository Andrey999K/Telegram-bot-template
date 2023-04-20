from .functions import logMessage

print("Импорт декораторов")


def loggingMessage(func):
    def output(message):
        logMessage(message)
        func(message)
    return output