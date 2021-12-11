 
class BoundedBase:
    number = 0
    def __init__(self):
        BoundedBase.number = BoundedBase.number + 1
        if BoundedBase.number > 1:
            raise TypeError
class D ( BoundedBase ):
    @classmethod
    def get_max_instance_count ( cls ):
        return 1
d1 = D()
try :
    d2 = D()
except TypeError :
    print ('everything works fine !')
else:
    print ('something goes wrong !')
 