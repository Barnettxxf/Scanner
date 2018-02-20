# -*- coding:utf-8 -*-

import json
import os
import sys
import hashlib
import threading
from lib.core import Downloader
import queue


class webcms():
    workQueue = queue.Queue()
    URL = ""
    threadNum = 0
    NotFound = True
    Downloader = Downloader.Downloader()
    result = ''

    def __init__(self, url, threadNum=10):
        self.url = url
        self.threadNum = threadNum
        filename = os.path.join(sys.path[0], 'data', 'data.json')
        fp = open(filename)
        webdata = json.load(fp, encoding='utf-8')
        for i in webdata:
            self.workQueue.put(i)
        fp.close()

    def getmd5(self, body):
        m2 = hashlib.md5()
        m2.update(body)
        return m2.hexdigest()

    def th_whatweb(self):
        if self.workQueue.empty():
            self.NotFound = False
            return False

        if self.NotFound is False:
            return False
        cms = self.workQueue.get()
        _url = self.url + cms['url']
        html = self.Downloader.get(_url)
        print('[whatweb log]: ', _url)
        if html is None:
            return False
        # 检测正则有没有匹配到内容，若没有则查看md5是否一样
        if cms['re']:
            if html.find(cms['re']) != -1:
                self.result = cms['name']
                self.NotFound = False
                return True
        else:
            md5 = self.getmd5(html)
            if md5 == cms['md5']:
                self.result = cms['name']
                self.NotFound = False
                return True

    # 用于启动多线程
    def run(self):
        while(self.NotFound):
            th = []
            for i in range(self.threadNum):
                t = threading.Thread(target=self.th_whatweb)
                t.start()
                th.append(t)
            for t in th:
                t.join()
        if self.result:
            print('[webcms]:%s cms is %s' % (self.url, self.result))
        else:
            print('[webcms]:%s cms NOTFound!' % self.url)


if __name__ == "__main__":
    webcms = webcms('http://blog.yesfree.pw/')
    webcms.run()
