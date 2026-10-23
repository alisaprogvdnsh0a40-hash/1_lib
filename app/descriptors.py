class Descriptor_int:
    def __set_name__(self,owner,name):
        self.private_name = '_' + name 
        print(name)

    def __set__(self, instance, value):
        if not isinstance(value,int):
            raise TypeError('adad vared shavad')
        if value < 0:
            raise ValueError('tadad nemitavanad manfi bashad')
        setattr(instance,self.private_name,value)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance,self.private_name,0)