
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from utils.tools import *

class Main (object):
    def __init__ (self) :
        pass

    def run (self):
        args=get_args()
        if args.url != None and args.url != "":
            fetch = Tools()
            print(fetch.chkPlayable(args.url))

def get_args():
    parser = argparse.ArgumentParser(
                usage="python main.py url",
                description="根据专辑或者艺术家地址下载专辑."
    )
    parser.add_argument('-u', '--url', type=str, default='', help="待检测的m3u，m3u8的地址")

    parse_result = parser.parse_args()
    return parse_result
if __name__ == '__main__':
    App = Main()
    App.run()