# -*- coding=utf-8 -*-

class Hint(object):
    def __init__(self, aint):
        self.aint = aint

    def get_aint(self):
        return self.__aint

    def set_aint(self, value):
        if isinstance(value, int):
            self.__aint = value
        else:
            raise ValueError('must be int')

    aint = property(get_aint, set_aint)


def test():
    a = Hint('a')
    print a.aint


if __name__ == '__main__':
    test()
    