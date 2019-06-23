#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: beer
# datetime:2019/6/17 7:59
# software: PyCharm

import requests
import csdn
import os
import json
import markdown
import config


def put_article(csdn):
    response = requests.post(csdn.url, headers=csdn.headers, data=form_data)
    s = response.content.decode()
    response_json = json.loads(s)
    if response_json['status']:
        return None
    else:
        return response_json['error']


def build_form_data(file, content, content_html, tags):
    form_data = {
        'title': file,
        'markdowncontent': content,
        'content': content_html,
        'id': None,
        'private': 0,
        'read_need_vip': 0,
        'tags': tags,
        'status': 0,
        'categories': 'java',
        'channel': 1,
        'type': 'original',
        'articleedittype': '1',
        'Description': 1
    }
    return form_data


def get_all_file(path):
    file_list = os.listdir(path)
    if len(file_list) >= 9:
        return file_list[0:9]
    else:
        return file_list


def get_content(path):
    content = ''
    f = open(path, 'r', encoding='utf-8')
    lines = f.readlines()
    for line in lines:
        content += line

    title = ''
    tags = []
    title_and_tags = content[content.index("---"):content.rindex("---"):]
    for line in title_and_tags.split("\n"):
        if line.find('title') == 0:
            title = line.split(':')[1]
        if line.find('tags') == 0:
            tags = line.split(':')[1]
            if tags.__contains__('['):
                tags = tags[tags.index('[') + 1:tags.index(']')]

    content = content[content.rindex("---"):]

    return content, title, tags


if __name__ == '__main__':
    cookies = config.cookies
    path = config.path
    csdn_url = config.csdn_url

    file_list = get_all_file(path)
    for file in file_list:
        content, title, tags = get_content(path + file)
        content_html = markdown.markdown(content)
        form_data = build_form_data(title, content, content_html, tags)
        csdn_obj = csdn.Csdn(cookies, csdn_url, form_data)
        result = put_article(csdn_obj)
        if result is not None:
            print("file: " + file + "; status: " + result)
