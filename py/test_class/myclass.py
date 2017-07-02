# -*- coding:utf-8 -*-
class MyClass(object):
    """"""

    # def __new__(cls, *args, **kwargs):
    # print("exec __new__ func start")
    # print(args, kwargs)
    # print("exec __new__ func end")
    # return object.__new__(cls, *args, **kwargs)

    def __init__(self, a):
        print("exec __init__ MyClass func")
        self.a = a


class My(MyClass):
    def __init__(self, a):
        self.a = a
        print type(super(My, self))
        # super(My, self).__init__(2)
        print("exec __init__ My")


if __name__ == "__main__":
    mc = My(1)
    print mc
    # mc = MyClass(1)
    # print(mc.a)
