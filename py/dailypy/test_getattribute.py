# -*- coding=utf-8 -*-


class A(object):
    def __getattribute__(self, *args):
        print "call..."