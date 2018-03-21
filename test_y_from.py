#!/usr/bin/env python
# coding=utf-8

def htest():
    i = 1
    while i < 4:
        n = yield i
        if i == 3:
            return 100
        i += 1


def itest():
    val = yield from htest()
    print(val)

t = itest()
t.send(None)
j = 0
while j < 3:
    j += 1
    try:
        t.send(j)
    except StopIteration as e:
        print('异常了')