#!/usr/bin/env python
# coding=utf-8

import time
from datetime import timedelta
import threading
import signal
import sys

from tornado import httpclient, gen, ioloop, queues, concurrent
from concurrent.futures import ThreadPoolExecutor
from tornado.queues import Queue

base_url = 'http://www.tornadoweb.org/en/stable/'
is_started = False
q = Queue(maxsize=2)

def quit(signum, frame):
    print 'signum', signum
    io = ioloop.IOLoop.current()
    io.stop()
    global is_started
    is_started = False
    time.sleep(1)
    sys.exit()

@gen.coroutine
def mock_get(num):
    print('sleep')
    f = yield gen.sleep(0.5)
    # time.sleep(3)
    print('wakeup')
    raise gen.Return('get data, num=%d' %(num))

def test_raise():
    print('sleep')
    # f = yield gen.sleep(3)
    # time.sleep(3)
    print('wakeup')
    raise gen.Return('get data')

@gen.coroutine
def mock_fetch(url):
    # yield create a generator
    resp = yield mock_get(1)
    # f = yield mock_get(2)
    # gen.coroutine 含有 yield 会启动一个 gen.Runner, 循环处理所有 yield
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


@gen.coroutine
def handle_group_msg():
    while True:
        yield test()
        # yield gen.sleep(0.1)

@gen.coroutine
def test():
    print('test begin')
    # f = get_links_from_url(base_url)
    # test_raise()
    # yield gen.sleep(1)
    f = yield mock_fetch(base_url)
    print f
    print('test end')
    # 只是一个回调
    # ioloop.IOLoop.current().add_future(f, callback)
    raise gen.Return(None)

if __name__ == '__main__':
    # test()

    # threads = []
    # t1 = threading.Thread(target=handle_group_msg, args=())
    # threads.append(t1)
    #
    signal.signal(signal.SIGINT, quit)
    signal.signal(signal.SIGTERM, quit)
    # is_started = True
    #
    # for t in threads:
    #     t.setDaemon(True)
    #     t.start()

    handle_group_msg()
    # ioloop.IOLoop.current().spawn_callback(handle_group_msg)

    # 用来处理异步和回调的事情
    ioloop.IOLoop.current().start()
