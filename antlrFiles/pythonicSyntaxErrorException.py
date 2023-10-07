class PythonicSyntaxErrorException(Exception):

    def __init__(self, stacktrace):
        self.stacktrace = stacktrace

    def __str__(self) -> str:
        errorMessage = "WHOOPS\n"
        errorMessage += str(self.stacktrace)
        return errorMessage