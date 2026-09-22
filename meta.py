# from models import Library,User

# class UserMeta(type):

#     def __new__(cls, name, bases, namespace, dct):
#         if name != "User" and User in bases:
#             if "get_permisseion"  not in dct:
#                 raise TypeError("in class get_permission nadarad!")
#         return super().__new__(name, bases, namespace, dct)



class UserMeta(type):

    def new(cls, name, bases, namespace, **kwargs):
        is_user_subclass = any(b.name == "User" for b in bases)
        if name != "User" and is_user_subclass:
            if "get_permission" not in namespace:
                raise TypeError(f"class {name} does not have get_permission method!")
        return super().new(cls, name, bases, namespace, **kwargs)