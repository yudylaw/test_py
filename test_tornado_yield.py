#!/usr/bin/env python

import time
from datetime import timedelta

from tornado import httpclient, gen, ioloop, queues

base_url = 'http://www.tornadoweb.org/en/stable/'


@gen.coroutine
def mock_get():
    print('sleep')
    # f = yield gen.sleep(3)
    # time.sleep(3)
    print('wakeup')
    raise gen.Return('get data')

def test_raise():
    print('sleep')
    # f = yield gen.sleep(3)
    # time.sleep(3)
    print('wakeup')
    raise gen.Return('get data')

@gen.coroutine
def mock_fetch(url):
    # yield create a generator
    resp = yield mock_get()
    # 每个 gen.coroutine 中的 yield 都会启动一个 gen.Runner
    # gen.Runner 负责把 mock_get() 这个 Future 的 result 赋值给 resp
    # 赋值操作是通过 generator.send(value) 完成的，原理：yield 的输入参数
    raise gen.Return('mock, url=%s, resp=%r' % (url, resp))

@gen.coroutine
def get_links_from_url(url):
    """Download the page at `url` and parse it for links.

    Returned links have had the fragment after `#` removed, and have been made
    absolute so, e.g. the URL 'gen.html#tornado.gen.coroutine' becomes
    'http://www.tornadoweb.org/en/stable/gen.html'.
    """
    try:
        response = yield httpclient.AsyncHTTPClient().fetch(url)
        print('fetched %s' % url)
        size = len(response.body)
        print('body size=%d' %(size))

    except Exception as e:
        print('Exception: %s %s' % (e, url))
        raise gen.Return(['Error'])

    raise gen.Return(['Success'])

def callback(future):
    print('callback future.result=%r' %(future.result()))

def test():
    print('test begin')
    # f = get_links_from_url(base_url)
    # test_raise()
    f = mock_fetch(base_url)
    # 只是一个回调
    # ioloop.IOLoop.current().add_future(f, callback)
    print('test end')

if __name__ == '__main__':
    test()
    ioloop.IOLoop.current().start()