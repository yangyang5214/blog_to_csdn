#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: beer
# datetime:2019/6/17 11:40
# software: PyCharm


class Csdn:

    def __init__(self, cookies, url,form_data):
        self.cookies = cookies
        self.url = url
        self.headers = self.build_headers(self)
        self.form_data = form_data

    @staticmethod
    def build_headers(self):
        headers = {'cookie': self.cookies}
        return headers
