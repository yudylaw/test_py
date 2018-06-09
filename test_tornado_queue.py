from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue

q = Queue(maxsize=2)

@gen.coroutine
def consumer():
    while True:
        item = yield q.get()
        try:
            print('Doing work on %s' % item)
            yield gen.sleep(0.01)
        finally:
            q.task_done()

@gen.coroutine
def producer():
    for item in range(100):
        yield q.put(item)
        print('Put %s' % item)

if __name__ == '__main__':
    # Start consumer without waiting (since it never finishes).
    # IOLoop.current().spawn_callback(consumer)
    consumer()
    producer()     # Wait for producer to put all tasks.
    q.join()       # Wait for consumer to finish all tasks.
    IOLoop.current().start()
    print('Done')
