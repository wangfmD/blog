# -*- coding:utf-8 -*-


class Si(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Si, cls).__new__(cls, *args, **kw)
        return cls._instance


class MyClass(Si):
    def __init__(self, a):
        self.a = a


if __name__ == "__main__":
    a1 = MyClass(1)
    print a1.a

    a2 = MyClass(2)
    print a1.a
    print a2.a
    print dir(MyClass)
