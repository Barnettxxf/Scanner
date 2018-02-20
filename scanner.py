# -*- coding:utf-8 -*-
from lib.core.Spider import SpiderMain
from lib.core import webcms, common, PortScan, webdir


def main():
    root = "https://www.shiyanlou.com/"
    threadNum = 10
    ip = common.gethostbyname(root)
    print('IP:', ip)
    print("start Port Scan:")

    # portscan
    pp = PortScan.PortScan(ip)
    pp.work()

    # DIR Fuzz
    dd = webdir.WebDir(root, threadNum)
    dd.work()
    dd.output()

    # webcms
    ww = webcms.webcms(root, threadNum)
    ww.run()

    # spider
    sm = SpiderMain(root, threadNum)
    sm.craw()


if __name__ == "__main__":
    main()
