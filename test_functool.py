#!/usr/bin/env python
# coding=utf-8

import functools

def add(a, b):
    print 'a=%d, b=%d' %(a, b)
    return a + b

add3 = functools.partial(add, 3)
add5 = functools.partial(add, 5)

print add3(4)

print add5(10)

