#!/usr/bin/env python
# coding=utf-8

from urllib import parse as urlparse

def cv_no_less_than(meta, destCV):
    meta_obj = dict(urlparse.parse_qsl(meta))
    # 没有传CV
    if "cv" not in meta_obj:
        return False

    sourceCV = meta_obj["cv"]
    # 不合法的cv长度
    if len(sourceCV) < 14 or len(destCV) < 14:
        return False

    # 去除CA
    sourceCV = sourceCV[2:]
    destCV = destCV[2:]

    #获取版本信息
    source = sourceCV.split("_")[0]
    dest = destCV.split("_")[0]

    sourceVec = source.split(".")
    sourceMajor = int(sourceVec[0])
    sourceMinor = int(sourceVec[1])
    sourceBuild = int(sourceVec[2])

    destVec = dest.split(".")
    destMajor = int(destVec[0])
    destMinor = int(destVec[1])
    destBuild = int(destVec[2])

    # 主版本更高
    if sourceMajor > destMajor:
        return True

    # 子版本更高
    if sourceMajor == destMajor and sourceMinor > destMinor:
        return True

    # 特性版本更高
    if sourceMajor == destMajor and sourceMinor == destMinor and sourceBuild >= destBuild:
        return True

    return False

if __name__ == "__main__":
    destCV = 'CA1.2.0_Iphone'
    meta = 'after=0&count=100&access_token=6d774774684e8d2d6b5927091b05a344&lc=0000000000000007&cc=TG0001&cv=CA1.5.2_Iphone&proto=8'
    flag = cv_no_less_than(meta, destCV)
    print('flag=%r' %(flag))