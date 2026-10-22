class LibraryError(Exception):
    """khata omomi ketabkhaneh"""
    pass

class BookNotFound(LibraryError):
    """ketab mored nazar pyda nashod"""
    pass

class UserNotFound(LibraryError):
    """fard mored nazar peida nashod"""
    pass

class PermissionDenied(LibraryError):
    """ejaze daryaft ketab nadarid"""
    pass

class BookNotAvailable(LibraryError):
    """ketab as gable rezev shode ast"""
    pass

print(issubclass(PermissionDenied,LibraryError))
