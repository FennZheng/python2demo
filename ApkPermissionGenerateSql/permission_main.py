#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
根据android应用权限txt，持久化到数据库表

"""

__author__ = 'vernonzheng'


def main():
    print 'start..'
    read_permission_txt()
    print 'end..'


def read_permission_txt():
    sql = "insert into mkt_app_permission_meta values('%s',0 ,'%s', '%s');"
    with open('permission.txt', 'r') as f:
        with open('permission.sql', 'w') as sql_f:
            flag = 0
            while 1:
                lines = f.readlines()
                if flag == 1:
                    break
                for i in range(0, len(lines)-1):
                    line = lines[i]
                    if str(line).strip().find('---end---') != -1:
                        flag == 1
                        return
                    if str(line).strip() == '':
                        continue
                    if str(line).find('android.permission') != -1:
                        permission_name = str(line).replace('android.permission.', '').replace('\r\n', '').strip()
                        i += 1
                        permission_info_ch = str(lines[i]).replace('android.permission.', '').replace('\r\n', '').strip()
                        i += 1
                        permission_info_en = str(lines[i]).replace('android.permission.', '').replace('\r\n', '').strip()
                        print(sql % (permission_name, permission_info_ch, permission_info_en)+"\r")


if __name__ == '__main__':
    main()