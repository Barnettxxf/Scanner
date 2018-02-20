# -*- coding:utf-8 -*-

import sys
from lib.core.Spider import SpiderMain


def main():
    root = "https://www.shiyanlou.com/"
    threadNum = 10
    w8 = SpiderMain(root, threadNum)
    w8.craw()


if __name__ == "__main__":
    main()
