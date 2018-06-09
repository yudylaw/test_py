#!/usr/bin/env python
# coding=utf-8

__author__ = 'fang'

import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient
import functools
import time

def task(fun, url):
    return functools.partial(fun, url)

def callback(gen, response):
    try:
        print 'callback:', response
        # gen 返回数据
        gen.send(response)
    except StopIteration:
        pass

def sync(func):
    def wrapper():
        gen = func()
        # gen 启动
        f = gen.next()
        print 'aa', f, gen
        # 固定 callback
        f(functools.partial(callback, gen))
    return wrapper

@sync
def fetch():
    # fetch(self, request, callback=None, raise_error=True, **kwargs)
    # 固定 url
    response = yield task(AsyncHTTPClient().fetch, 'http://www.suhu.com')
    print '1'
    print response
    print '2'

fetch()
print 3
tornado.ioloop.IOLoop.instance().start()