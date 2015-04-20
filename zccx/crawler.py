#!/usr/bin/env python
#coding:utf-8

import urllib2, urllib, cookielib
import time, datetime
import re

from dbhandler import DBHandler
from settings import *

class Status:
    def __init__(self, code, name='', stu_id='', data=()):
        self.code, self.name, self.stu_id, self.data = code, name, stu_id, data


class Crawler:
    re_token = re.compile(RE_TOKEN)
    re_times = re.compile(RE_TIMES)
    re_an = re.compile(RE_AN)

    def __init__(self, wetoken, dbhandler):
        self.wetoken = wetoken
        self.db = dbhandler
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))

    def get_stu_info(self):
        """
        Use database handler to get student's infomation
        """
        info = self.db.get()
        (self.stu_id, self.name) = info[0]
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.db.update(t)

    def get_login_token(self):
        html = self.opener.open(INIT_URL).read()
        return self.re_token.findall(html)[0]

    def parse_html(self, html):
        times = self.re_times.findall(html)[0]
        lis = self.re_an.findall(html)
        return (times, lis)

    def login_to_get_html(self, login_token):
        form = {FNAME_A:login_token, FNAME_B:self.stu_id, FNAME_C:self.name.encode("utf8")}
        post = urllib.urlencode(form)
        req = urllib2.Request(INFO_URL, post, HEAD)
        response = self.opener.open(req)
        return response.read()
        
    def work(self):
        try:
            self.get_stu_info()
        except Exception as var:
            """Unbind"""
            print(var)
            return Status(CODE_UNBIND)

        try:
            login_token = self.get_login_token()
        except Exception as var:
            print(var)
            return Status(CODE_FOP)

        try:
            html = self.login_to_get_html(login_token)
            if "刷卡计数" not in html:
                raise ValueError("Wrong NAME or STU_ID")
        except ValueError as var:
            print(var)
            """failed to login, wrong name or stu_id"""
            return Status(CODE_WRONG, self.name, self.stu_id)
        except:
            return Status(CODE_FOP)

        try:
            data = self.parse_html(html)
        except Exception as var:
            print(var)
            """the website unreachable"""
            return Status(CODE_FOP, self.name, self.stu_id)
        
        return Status(CODE_OK, self.name, self.stu_id, data)
