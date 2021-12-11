class BoundedMeta(type):
    number = 0
    max_instance_count = 1
    @classmethod
    def __prepare__(metacls, name, bases, **kargs):
        return super().__prepare__(name, bases, **kargs)
    def __new__(metacls, name, bases, namespace, **kargs):
        return super().__new__(metacls, name, bases, namespace)
    def __init__(cls, name, bases, namespace, max_instance_count = 1, **kargs):
        BoundedMeta.max_instance_count = max_instance_count
        super().__init__(name, bases, namespace)
    def __call__(self, *args, **kwargs):
        BoundedMeta.number = BoundedMeta.number + 1
        if BoundedMeta.max_instance_count is not None:
            if BoundedMeta.number > BoundedMeta.max_instance_count:
                raise TypeError
class C(metaclass = BoundedMeta , max_instance_count = 2):
    pass
c1 = C ()
c2 = C ()
try :
    c3 = C ()
except TypeError :
    print ('everything works fine !')
else:
    print ('something goes wrong !')
 