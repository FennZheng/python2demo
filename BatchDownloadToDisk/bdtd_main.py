#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
根据txt的链接，多线程批量下载文件到本地
read download links from txt ,and download all in multithreading
"""

__author__ = 'vernonzheng'

import config_default
import re
import urllib2
import time
import os

configs = config_default.configs


def main():
    clean_export_dir()
    read_download_links()


def clean_export_dir():
    file_list = os.listdir(configs['export_path'])
    for f in file_list:
        os.remove(configs['export_path']+f)


def read_download_links():
    with open(configs['download_link_file'], 'r') as f:
        for line in f.readlines():
            if valid_dl(line):
                dump_to_disk(line)


def dump_to_disk(download_link):
    f = urllib2.urlopen(download_link)
    data = f.read()
    with open(configs['export_path']+str(time.time())+".jpg", "wb") as code:
        code.write(data)
    print 'finish download :'+download_link


def valid_dl(download_link):
    return re.match(configs['reg_download_link'], download_link)


if __name__ == "__main__":
    main()