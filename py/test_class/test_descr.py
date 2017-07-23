# -*- coding: utf-8 -*-
import os
import pickle


class FileDescr(object):
    saved = []

    def __init__(self, name=None):
        self.name = name

    def __get__(self, obj, typ=None):
        if self.name not in FileDescr.saved:
            raise AttributeError('{} before assignment'.format(self.name))

        try:
            with open(self.name, 'r') as fp:
                val = pickle.load(fp)
                return val
        except Exception:
            raise AttributeError('could not read {}'.format(self.name))

    def __set__(self, obj, val):
        with open(self.name, 'w') as fp:
            try:
                pickle.dump(val, fp)
                FileDescr.saved.append(self.name)
            except Exception:
                raise AttributeError('could not pickle {}'.format(self.name))

    def __delete__(self, obj):
        try:
            os.unlink(self.name)
            FileDescr.saved.remove(self.name)
        except Exception:
            pass
