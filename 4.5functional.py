def smart_function(func):
    num = [0]
    def call_func():
        func()
        num[0] += 1
        print("times is",num[0])
    return call_func
# test
@smart_function
def test():
    pass
test()
test()
test()
