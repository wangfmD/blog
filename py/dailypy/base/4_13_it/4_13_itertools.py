# -*- coding=utf-8 -*-
import itertools
# chain 连接多个迭代器

it = itertools.chain(xrange(10), "abc")
print it
print list(it)
print 111
