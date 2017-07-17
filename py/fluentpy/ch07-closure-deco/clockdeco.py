# -*- coding:utf-8 -*-
import time


def clock(func):
    def clocked(*args):
        t0 = time.ctime()
        result = func(*args)
        elapsed = time.ctime()
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(t0, elapsed, name, arg_str, result)
        return result
    return clocked
