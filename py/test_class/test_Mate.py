# -*- coding: utf-8 -*-
#  参考
#  http://python.jobbole.com/86367/
# ：类的定义过程，其实是type类型实例化的过程。


from time import ctime
from warnings import warn

# print 'start'


# class MetaC(type):
    # def __init__(cls, name, bases, attrd):
        # super(MetaC, cls).__init__(name, bases, attrd)
        # print 'ctreate class {} at: {}'.format(name, ctime())


# class Foo(object):
    # """docstring for Foo"""
    # __metaclass__ = MetaC

    # def __init__(self):
        # print 'Instance class {} at {}'.format(self.__class__.__name__,
                                               # ctime())


# print 'end'


class ReqStrRepr(type):
    def __init__(cls, name, bases, attrd):
        super(ReqStrRepr, cls).__init__(name, bases, attrd)

        if '__str__' not in attrd:
            raise TypeError('Class requires overriding of __str__()')

        if '__repr__' not in attrd:
            warn('class suggest overriding of __sepr__()\n', stacklevel=3)


class Foo(object):
    __metaclass__ = ReqStrRepr

    def __init__(self):
        print "init.."

    def __str__(self):
        pass

    def __repr__(self):
        pass

if __name__ == '__main__':
    f = Foo()
