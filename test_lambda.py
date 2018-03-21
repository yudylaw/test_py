#!/usr/bin/env python
# coding=utf-8

def test(a):
    return a + 10

print test(1)

test2 = lambda a, b: a + b

print test2(1, 2)