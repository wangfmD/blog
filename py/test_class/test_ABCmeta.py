# -*- coding: utf-8 -*-
# http://yansu.org/2013/06/09/learn-python-abc-module.html
# https://docs.python.org/2/library/abc.html
# http://www.jianshu.com/p/19ed49293168 **

from abc import ABCMeta, abstractmethod


class MyABC(object):
    __metaclass__ = ABCMeta


def test_():
    MyABC.register(tuple)
    print(issubclass(tuple, MyABC))
    print(isinstance((), MyABC))


class PluginBase(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def load(self, input):
        """docstring for load"""
        pass

    @abstractmethod
    def save(self, outpt, data):
        """docstring for save"""
        pass


class Registered(object):
    """Docstring for Registered. """

    def load(self, input):
        """docstring for load"""
        return input.read()

    def save(self, output, data):
        """docstring for save"""
        return output.write(data)


def test_register():
    """docstring for test_register"""
    PluginBase.register(Registered)

    print("Subclasss :{}".format(issubclass(Registered, PluginBase)))
    print("Instance :{}".format(isinstance(Registered(), PluginBase)))


class RegisteredV1(PluginBase):
    """Docstring for Registered. """

    def load(self, input):
        """docstring for load"""
        return input.read()

    def save(self, output, data):
        """docstring for save"""
        return output.write(data)


def test_registerV1():
    """docstring for test_register"""

    print("Subclasss :{}".format(issubclass(RegisteredV1, PluginBase)))
    print("Instance :{}".format(isinstance(RegisteredV1(), PluginBase)))


def test_sub_PluginBase():
    """docstring for test_sub_PluginBase"""
    for sub_c in PluginBase.__subclasses__():
        print(sub_c)


class RegisteredV2(PluginBase):
    """Docstring for Registered. """

    def save(self, output, data):
        """docstring for save"""
        return output.write(data)


def test_registeredV2():
    """没有实现抽象基类的全部方法: TypeError"""
    print("Instance :{}".format(isinstance(RegisteredV2(), PluginBase)))


if __name__ == '__main__':
    #  test_()
    #  test_register()
    #  test_registerV1()
    test_registeredV2()
    #  print(PluginBase.__subclasses__())
    #  test_sub_PluginBase()
