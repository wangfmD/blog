# -*- coding: utf-8 -*-


class Property_P(object):
    def __init__(self, age):
        """TODO: to be defined1. """
        self.age = age

    # @property
    def age():
        def fget(self):
            return self._age

        def fset(self, value):
            if value > 0:
                self._age = value
            else:
                raise ValueError("must be > 0")

        print "locals:{}".format(locals())
        return locals()

    age = property(**age())


class H(object):
    def __init__(self, age):
        self.x = age

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, v):
        self._x = 100


def test_a():
    p = Property_P(-10)
    print p.age


def test_b():
    p = H(1)
    print p.x


if __name__ == '__main__':
    # test_a()
    test_b()
