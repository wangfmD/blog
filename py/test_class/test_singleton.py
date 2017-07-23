# -*- coding: utf-8 -*-
# python中实现单例有多种方式：
# 1，元类方式
# 2，__new__方式
# 3，装饰器方式
# 4，共享属性方式
# 5，模块方式
# http://python.jobbole.com/87791/


# 元类方式
# 不能放在init中初始化实例的值
class SingletonV1(type):
    print "init"

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            print "if"
            cls._instance = super(SingletonV1, cls).__call__(*args, **kwargs)
            # cls.instance = type.__call__(cls, *args, **kw)
            # cls.instance = type.__dict__['__call__'].__get__(cls)(*args, **kw)
        return cls._instance


class S1(object):
    __metaclass__ = SingletonV1

    def __init__(self, name):
        print('S1 init')
        self.name = name


class SingletonV2(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SingletonV2, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance


class FooV2(SingletonV2):
    def __init__(self, name):
        print("FooV2 init")
        self.name = name


def test_SingletonV2():
    """"""
    a1 = FooV2('wfm')
    a2 = FooV2('wzr')
    # print a2.__dict__
    # a2.name = 'wzr'
    print(a1.name)
    print("a2.name :{}".format(a2.name))


def test_SingletonV1():
    a1 = S1('wfm')
    print a1.name
    a2 = S1('wzr')
    a2.name = 'wzr'
    print a1.name


if __name__ == '__main__':
    pass
    # test_SingletonV1()
    test_SingletonV2()
