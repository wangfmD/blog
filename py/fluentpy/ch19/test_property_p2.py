# -*- coding=utf-8 -*-


class Hint(object):
    def __init__(self, aint):
        self.aint = aint

    def get_aint(self):
        return self.__aint

    def set_aint(self, value):
        if isinstance(value, int):
            self.__aint = 10
        else:
            raise ValueError('must be int')

    aint = property(get_aint, set_aint)


class H(object):
    def __init__(self, a):
        self.name = a

    @property
    def get_name(self):
        return self.name + "NAME"


class Claz(object):
    data = 'the class data attr'

    @property
    def prop(self):
        return 'the prop value'


def test():
    a = H('a')
    print a.name


if __name__ == '__main__':
    test()
