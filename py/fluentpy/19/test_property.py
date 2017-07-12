# -*- coding=utf-8 -*-
# 1,property 必须是新式类 
# 老式的写法实例属性在 set 和get方法中必须加 "__" 否则会  File "D:\01_gitgub\notes\py\fluentpy\19\test_property.py", line 17, in set_weigth
    # self.weigth = value
# RuntimeError: maximum recursion depth exceeded while calling a Python object


class LineItem_v0(object):
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight  # ➊
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property  # ➋
    def weight(self):  # ➌
        return self._weight  # ➍

    @weight.setter   # ➎
    def weight(self, value):
        if value > 0:
            self._weight = value  # ➏
        else:
            raise ValueError('value must be > 0')


class LineItem(object):
    def __init__(self, desc, weigth, price):
        self.desc = desc
        self.weigth = weigth
        self.price = price

    def subtotal(self):
        return self.weigth * self.price

    def get_weigth(self):
        return self._weigth

    def set_weigth(self, value):
        if value > 0:
            self._weigth = value
        else:
            raise ValueError("weigth must be > 0")
    weigth = property(get_weigth, set_weigth)


class LineItem_v2(object):
    def __init__(self, desc, weigth, price):
        self.desc = desc
        self.weigth = weigth
        self.price = price

    def subtotal(self):
        return self.weigth * self.price

    @property
    def weigth(self):
        return self.__weigth

    @weigth.setter
    def weigth(self, value):
        if value > 0:
            self.__weigth = value
        else:
            raise ValueError("value must be > 0")


class P(object):
    def __init__(self, name, age=None):
        self.name = name
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, value):
        if value < 0:
            raise ValueError('age must be > 0')
        else:
            self._age = value
    age = property(get_age, set_age)


def test():
    a = LineItem_v0('pingguo', -10, 2)
    print a.subtotal()


def test_p():
    p = P('dsd', -1)
    p.age = -1
    print p.age
    print p._age


if __name__ == '__main__':
    test()

