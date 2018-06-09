#!/usr/bin/env python
# coding=utf-8

import uuid
import hashlib
import random
import time

def get_ex_code():
    code = str(uuid.uuid1())
    return code

def test(*uids):
    print uids
    uid_list = list(uids)
    for uid in uid_list:
        print uid

if __name__ == "__main__":

    # print(get_ex_code())
    # print(get_ex_code())
    # print(get_ex_code())
    # print(get_ex_code())

    # src = 'abc'
    # m = hashlib.md5()
    # m.update(src.encode("utf8"))
    # print(m.hexdigest())

    code = "".join(random.sample('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ', 16))

    print(code)

    uids = [1,2,3]

    test(tuple(uids))

    time.struct_time

    now = time.localtime()

    t = now