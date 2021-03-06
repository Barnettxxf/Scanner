# -*- coding:utf-8 -*-
import sys
import os
import queue
import threading
import requests


class WebDir():
    def __init__(self, root, threadNum=5):
        self.root = root
        self.threadNum = threadNum
        self.headers = {
                     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
                     'Referer': 'http://www.shiyanlou.com',
                     'Cookie': 'whoami=w8ay',
        }
        self.task = queue.Queue()
        self.s_list = []
        filename = os.path.join(sys.path[0], 'data', 'dir.txt')
        # 原作中会有编码错误，这里加上errors参数忽略错误
        for line in open(filename, errors='ignore'):
            self.task.put(root + line.strip())

    def checkdir(self, url):
        status_code = 0
        try:
            # 用head访问网页头来判断返回状态码，提高访问速度
            r = requests.head(url, headers=self.headers)
            status_code = r.status_code
        except BaseException:
            status_code = 0
        return status_code

    def test_url(self):
        while not self.task.empty():
            url = self.task.get()
            s_code = self.checkdir(url)
            if s_code == 200:
                self.s_list.append(url)
            print("Testing: %s status:%s" % (url, s_code))

    def work(self):
        threads = []
        for i in range(self.threadNum):
            t = threading.Thread(target=self.test_url)
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        print('[*] The DirScan is complete!')

    def output(self):
        if len(self.s_list):
            print('[*] status == 200 dir:')
            for url in self.s_list:
                print(url)


if __name__ == "__main__":
    root = 'https://www.shiyanlou.com/'
    test = WebDir(root)
    test.output()
