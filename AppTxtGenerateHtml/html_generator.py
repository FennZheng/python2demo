#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
根据App的信息，生成分页的html
"""
__author__ = 'vernonzheng'

from html_utils import *

configs = config_default.configs


def main():
    print 'main start'
    read_and_generate()
    print 'main_end'


#取模分页
def read_and_generate():
    page_count = HtmlUtils.get_file_lines(configs['apk_info_txt'])//configs['page_size']+1
    with open(configs['apk_info_txt'], 'r') as f:
        record_count = 0
        page_inner_count = 0
        page_index = 1
        html_file_name = HtmlUtils.init_new_html(page_index)
        HtmlUtils.init_html_header(html_file_name, page_index, page_count)
        for fl in f.readlines():
            record_count += 1
            page_inner_count += 1
            if page_inner_count > configs['page_size']:
                #end this html
                HtmlUtils.init_html_end(html_file_name, page_index, page_count-1)
                #reset index
                page_index += 1
                page_inner_count = 1
                #create new html
                html_file_name = HtmlUtils.init_new_html(page_index)
                HtmlUtils.init_html_header(html_file_name, page_index, page_count)
            HtmlUtils.write_item(html_file_name, record_count, str(fl).replace("\"", ""))
        #end latest html
        HtmlUtils.init_html_end(html_file_name, page_index, page_count-1)


if __name__ == '__main__':
    main()