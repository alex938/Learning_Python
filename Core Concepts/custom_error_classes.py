class ParseError(ValueError):
    def __init__(self):
        self.__message = "Command format error: CMD <OPTION>"
    
    def __str__(self):
        return self.__message
    
try:
    command = input("Command: ")
    if not command.startswith("CMD"):
        raise ParseError
except ParseError as err:
    print(err)
else:
    print("Performing: {}".format(command))