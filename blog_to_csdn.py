#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: beer
# datetime:2019/6/17 7:59
# software: PyCharm

import requests
import csdn
import markdown_util as md

form_data = {
    'title': 'title',
    'markdowncontent': 'markdowncontent',
    'content': 'content',
    'id': None,
    'private': None,
    'read_need_vip': None,
    'tags': [],
    'status': 0,
    'categories': [],
    'channel': [],
}

if __name__ == '__main__':
    content_html = md.markdown_to_html("111")
    csdn = csdn.Csdn()
    csdn.put(content_html)
