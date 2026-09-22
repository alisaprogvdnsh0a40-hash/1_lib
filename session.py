from exceptions import *
from models import Library,User

class LibSession:
    def __init__(self,library,user_id):
        self.lib = library
        self.user_id = user_id
        self.user_object = None

    def __enter__(self):
        if self.user_id not in self.lib.users:
            raise UserNotFound("user_id peyda nashod")
        self.user_object = self.lib[self.user_id]
        print(f"........khosh amadid {self.user_object.name}.........")
        return self.user_object
    
    def __exit__(self, exc_type, exc, tb):
        
        if self.user_object:
            print(f"........khoda hafez {self.user_object.name}.........")
        if exc_type:
            print(f"khata :{exc} dar:{tb}")

        return False