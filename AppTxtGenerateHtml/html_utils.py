#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'vernonzheng'

import config_default

configs = config_default.configs


class HtmlUtils(object):

    @staticmethod
    def init_new_html(page_index):
        html_file_name = configs['html_export_path'] + configs['html_file_prefix'] + str(page_index) + '.html'
        with open(html_file_name, 'w'):
            print 'new html file create:'+html_file_name
        return html_file_name

    @staticmethod
    def init_html_header(html_file, page_index, page_count):
        with open(html_file, 'w') as f:
            print 'file', f
            f.writelines(['<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">',
                          '<meta http-equiv="Cache-Control" content="no-store"/>',
                          '<meta http-equiv="Pragma" content="no-cache"/>',
                          '<meta http-equiv="Expires" content="0"/>',
                          '<meta http-equiv="X-UA-Compatible" content="IE=9">',
                          '<!DOCTYPE html>',
                          '<html><head><title>斯凯网络应用库信息</title></head>',
                          '<!-- CSS goes in the document HEAD or added to your external stylesheet -->',
                          '<style type="text/css">',
                          'table.imagetable {',
                          'margin:auto;font-family: verdana,arial,sans-serif;',
                          'font-size:11px;',
                          'color:#333333;',
                          'border-width: 1px;',
                          'border-color: #999999;',
                          'border-collapse: collapse;',
                          '}',
                          'table.imagetable th {',
                          'background:#b5cfd2 url("../img/cell-blue.jpg");',
                          'border-width: 1px;',
                          'padding: 8px;',
                          'border-style: solid;',
                          'border-color: #999999;',
                          '}',
                          'table.imagetable td {',
                          'background:#dcddc0 url("../img/cell-grey.jpg");',
                          'border-width: 1px;',
                          'padding: 8px;',
                          'border-style: solid;',
                          'border-color: #999999;',
                          '}',
                          '</style>',
                          '<body>',
                          '应用信息:',
                          '当前页('+str(page_index)+')',
                          '<div style="margin:auto;width:600px;word-break: break-all;">',
                          ''+HtmlUtils.init_page_jump_str(page_count)+'</div>',
                          '<table class="imagetable">',
                          '<tr><th>序号</th><th>应用名称</th><th>应用显示版本</th><th>应用Icon</th><th>应用下载链接</th>'])

    @staticmethod
    def init_html_end(html_file, page_index, page_count):
        with open(html_file, 'a') as f:
            f.write('</table>')
            f.write('当前页('+str(page_index)+")")
            f.write('<div style="margin:auto;width:600px;word-break: break-all;">')
            f.write(HtmlUtils.init_page_jump_str(page_count)+'</div>')
            f.write('</body></html>')

    @staticmethod
    def write_item(html_file, record_index, content):
        with open(html_file, 'a') as f:
            # mac下换行是/r
            f.write(HtmlUtils.format_html_line(record_index, HtmlUtils.split_line(content)) + "\r")

    @staticmethod
    def format_html_line(record_index, str_array):
        if len(str_array) < 4 or len(str_array) > 4:
            error_msg = ''
            for item in str_array:
                error_msg += item
            print('error item:' + error_msg)
        else:
            name = str_array[0]
            app_show_ver = str_array[1]
            icon_file_id = str_array[2]
            apk_file_id = str_array[3]
            format_str = '<tr><td>%s</td><td>%s</td><td>%s</td><td>' \
                         '<img src="http://dl.elevensky.net/imgf/%s" height="72" width="72"></td>' \
                         '<td><a href="http://dl.elevensky.net/apkf/%s">下载apk</a></td>'
            return format_str % (record_index, name, app_show_ver, icon_file_id, apk_file_id)

    @staticmethod
    def split_line(content):
        return content.split(configs['split_sign'])

    @staticmethod
    def init_page_jump_str(page_count):
        i = 1
        page_info = ""
        while i <= page_count:
            page_info += "&nbsp;<a href="+configs['html_file_prefix']+"%s.html>%s</a>&nbsp;" % (i, i)
            i += 1
        return page_info

    @staticmethod
    def get_file_lines(file_name):
        count = 0
        for count, line in enumerate(open(file_name, 'rU')):
            count += 1
        return count
