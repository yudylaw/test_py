#!/usr/bin/env python
# coding=utf-8

import datetime
import urlparse

if __name__ == "__main__":
    d1 = datetime.datetime.now()
    d2 = datetime.datetime(d1.year, d1.month, d1.day + 1)
    diff = (d2 - d1)
    print int(diff.total_seconds())

    query = urlparse.parse_qsl('/api/v1/payment/wxpay?uid=200050&xrealip=59.110.125.194')
    print dict(query)