from enum import Enum 


class ExceptionCodes(Enum):
    DefaultExceptionCode = 30
    NoneValue = 31
    InvalidPath = 32
    EmptyValue = 33
    InvalidValue = 34
    CannotCreatePath = 35
    ElementNotFound = 36
    InvalidFile = 37
    InvalidFolder = 38
    CannotRemovePath = 39
    CannotParseValue = 40
    EmptyVlanDataframe = 41
    NoRedundantVlans = 42
    EmptyList = 43


def get_exception_message(code=None):
    msgs = dict()

    msgs[ExceptionCodes.DefaultExceptionCode] = "Something went wrong."
    msgs[ExceptionCodes.NoneValue] = "None value provided for:"
    msgs[ExceptionCodes.InvalidPath] = "Path informed is not a valid formatted folder or file."
    msgs[ExceptionCodes.EmptyValue] = "Value not informed for:"
    msgs[ExceptionCodes.EmptyList] = "Empty list provided for:"
    msgs[ExceptionCodes.EmptyVlanDataframe] = "There are no vlans available."
    msgs[ExceptionCodes.NoRedundantVlans] = "There are no redundant vlans available."
    msgs[ExceptionCodes.CannotCreatePath] = "Path informed cannot be created."
    msgs[ExceptionCodes.InvalidValue] = "Invalid value. Check value type or range."
    msgs[ExceptionCodes.CannotRemovePath] = "Path(s) informed cannot be removed."
    msgs[ExceptionCodes.CannotParseValue] = "Value informed cannot be parsed."
    msgs[ExceptionCodes.ElementNotFound] = "There is no element related to the key informed."
    msgs[ExceptionCodes.InvalidFile] = "Path informed is not a valid existent file."
    msgs[ExceptionCodes.InvalidFolder] = "Path informed is not a valid existent folder."
   
    try:
        return msgs[code]
    except KeyError:
        return msgs[ExceptionCodes.DefaultExceptionCode]


class BaseException(Exception):
    def __init__(self, message, code):
        super(BaseException, self).__init__(message, code)
        self.message = message
        self.code = code

    def __str__(self):
        return "Error Code {}. {}".format(self.code.value, self.message)

    def __repr__(self):
        return self.__str__()


class VlanException(BaseException):
    def __init__(self, code=None, parameters=None):
        code = code if code else ExceptionCodes.DefaultExceptionCode
        message = get_exception_message(code)
        super(VlanException, self).__init__(message, code)
        self.code = code
        self.parameters = parameters
        if self.parameters:
            self.message = "{} ({})".format(message, self.parameters)
        else:
            self.message = message
