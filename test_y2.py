#!/usr/bin/env python
# coding=utf-8

mygenerator = (x*x for x in range(3))
# for i in mygenerator:
#     print i

# StopIteration 已经结束
# print mygenerator.next()

def gen():
    mylist = range(3)
    for i in mylist:
        yield i*i


def gen2():
    r = 10
    while True:
        # n 接收输入 send(n)
        # r 是输出
        n = yield r
        print 'gen, n=%d, r=%d' %(n, r)
        r = r * n


# it = gen()
#
# print it
#
# for i in it:
#     print i

it2 = gen2()
r = it2.send(None) #启动并执行
print 'start gen, result=', r
r = it2.send(2)    #从第一次结束的地方接着执行, 第二次执行
print 'send to gen, result=', r
