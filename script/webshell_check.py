# -*- coding:utf-8 -*-
# 对每个.php结尾的文件进行一句话爆破

import os
import sys

from lib.core.Downloader import Downloader

filename = os.path.join(sys.path[0], 'data', 'web_shell.dic')
payload = []
f = open(filename)
a = 0
for i in f:
    payload.append(i.strip())
    a += 1
    if (a == 999):
        break


class spider():
    def run(self, url, html):
        if (not url.endswith('.php')):
            return False
        print('[Webshell check]: ', url)
        post_data = {}
        for _payload in payload:
            post_data[_payload] = 'echo "password is %s": ', _payload
            r = Downloader.post_data
            if r:
                print('webshell: %s' % r)
                return True
        return False


if __name__ == "__main__":
    pass
