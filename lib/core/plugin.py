# -*- coding:utf-8 -*-

import os
import sys

# 插件系统的开发流程
# 1.获取插件，通过一个目录里的以.py的文件扫描得到
# 2.将插件目录加入到环境变量sys.path
# 3.爬虫将扫描好的url和网页源码传递给插件
# 4.插件工作，工作完毕后主动权还给扫描器


class SpiderPlus(object):
    def __init__(self, plugin, disallow=[]):
        self.dir_exploit = []
        self.disallow = ['__init__']
        self.disallow.extend(disallow)
        self.plugin = os.getcwd() + '/' + plugin
        print('os.getcwd: ', self.plugin)
        sys.path.append(self.plugin)

    def list_plusg(self):
        def filter_func(file):
            if not file.endswith(".py"):
                return False
            for disfile in self.disallow:
                if disfile in file:
                    return False
            return True

        dir_exploit = filter(filter_func, os.listdir(self.plugin))
        return list(dir_exploit)

    def work(self, url, html):
        for _plugin in self.list_plusg():
            try:
                m = __import__(_plugin.split('.')[0])
                spider = getattr(m, 'spider')
                p = spider()
                p.run(url, html)
            except Exception as e:
                print(e)
