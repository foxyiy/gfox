#类装饰器 
class Test():
    def __init__(self,fun):
        print(fun)
    def __call__(self):
        print("call")

@Test
def test():
    print("test")
#调用call方法
test()
    