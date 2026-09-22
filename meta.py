from models import Library,User
class UserMeta(type):

    def __new__(cls, name, bases, namespace, dct):
        if name != "User" and User in bases:
            if "get_permisseion"  not in dct:
                raise TypeError("in class get_permission nadarad!")
        return super().__new__(name, bases, namespace, dct)