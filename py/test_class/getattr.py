# -*- coding=utf-8 -*-


class A(object):
    """class A"""
    c = 1

    def __init__(self):
        self.attr_a = 1

    def __getattribute__(self, *args, **kwargs):
        print("{} call _getattribute:".format(args))
        print super(A, self), "%%%%%%%%%%", type(super(A, self))
        # return self.attr_a
        # return super(A, self).__getattribute__(self, *args, **kwargs)
        return object.__getattribute__(self, *args, **kwargs)


def test_a():
    a = A()
    print(a.attr_a)
    # print(a.c)


class C(object):
    # a = 'abc'

    def __getattribute__(self, *args, **kwargs):
        print("__getattribute__() is called")
        if args[0] == 'a':
            return object.__getattribute__(self, *args, **kwargs)
        else:
            print '调用函数foo()'
            return object.__getattribute__(self, 'foo')()

    def foo(self):
        return "hello"

if __name__ == "__main__":
    test_a()
    # c = C()
    # print c.a
