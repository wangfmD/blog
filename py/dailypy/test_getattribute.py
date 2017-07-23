# -*- coding=utf-8 -*-


class A(object):
    def __getattribute__(self, *args):
        print "call..."

def func():
    a = 1
    print a1
