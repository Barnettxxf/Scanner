# -*- coding:utf-8 -*-
import socket
from urllib import parse


def urlsplit(url):
    domain = url.split('?')[0]
    _url = url.split("?")[-1]
    param = {}
    for val in _url.split('&'):
        param[val.split('=')[0]] = val.split('=')[-1]

    # combine
    urls = []
    for val in param.values():
        new_url = domain + '?' + _url.replace(val, 'my_Payload')
        urls.append(new_url)
    return urls


def gethostbyname(url):
    domain = parse.urlparse(url)
    if domain.netloc is None:
        return None
    ip = socket.gethostbyname(domain.netloc)
    return ip


if __name__ == '__main__':
    test_url = 'https://www.shiyanlou.com/courses/?a=1&b=2&c=3'
    print(urlsplit(test_url))
    print(gethostbyname(test_url))
