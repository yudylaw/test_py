#!/usr/bin/python
# coding=utf-8

import MySQLdb

def test():
    sns = MySQLdb.connect("120.55.86.91", "root", "UO8EGk3Yms", "test")
    cursor = sns.cursor()
    cursor.execute("select feed_id, uid from feed")
    results = cursor.fetchall()
    for feed in results:
        print feed[0], feed[1]
    print "test"

def hello2(age, name):
    print age, name

def hello(age, *args, **kwargs):

    print 'args'

    for arg in args:
        print arg

    print 'kwargs'

    for k, v in kwargs.items():
        print k, v

if __name__ == "__main__":
    # print "hello main";
    # test();
    # hello(1, 'a', 2, 'b', old = 20, name = 'yudy')
    # args = [10, 'yudy']
    kwargs = {'age':10, 'name':'yudy'}
    hello2(**kwargs)