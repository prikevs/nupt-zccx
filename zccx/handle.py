#coding:utf-8

from crawler import Crawler, Status
from dbhandler import DBHandler
from settings import *
import datetime
import re

RE_SQL = r"""[/!='"|&\\*()\[\]<>`?]"""

class Handle:
    cnweeks = (u"星期一", u"星期二", u"星期三", u"星期四", u"星期五", u"星期六", u"星期日")

    def __init__(self, wetoken):
        self.db = DBHandler(wetoken)
        self.handlers = {
            CODE_OK: self.handle_ok,
            CODE_FOP: self.handle_failed_to_open,
            CODE_WRONG: self.handle_wrong_pwd,
            CODE_UNBIND: self.handle_unbind,
        }
        self.wetoken = wetoken

    def parse_data(self, data):
        self.weekday_c = self.weekend_c = 0
        (self.times, date) = data
        first = True
        self.last = datetime.datetime(1994, 10, 2)
        for day in date:
            d = datetime.datetime(int(day[0]), int(day[1]), int(day[2]))
            if first:
                first = False
                self.last = d
            if d.weekday() in range(0, 5):
                self.weekday_c = self.weekday_c + 1;
            else:
                self.weekend_c = self.weekend_c + 1;
        self.date = "%s %s"% (str(self.last.date()), self.cnweeks[self.last.weekday()])

        
    def consult(self):
        status = Crawler(self.wetoken, self.db).work()
        return self.handlers[status.code](status)

    def parse_bind_message(self, msg):
        temp = msg.split(u' ')
        if len(temp) < 3:
            raise Exception("Wrong msg while split") 
        if len(temp[2]) != 9 or re.search(RE_SQL,temp[2]) != None:
            raise Exception("Wrong stu_id format")
        if re.search(RE_SQL, temp[1]) != None:
            raise Exception("Wrong name format")
        return (temp[1], temp[2]) 

    def bind(self, msg):
        try:
            (name, stu_id) = self.parse_bind_message(msg)
            self.db.bind(name, stu_id)
        except Exception as var:
            print(var)
            return u"绑定失败，请按照格式重新绑定"
        return u"绑定成功！可以开始查询\n直接回复 查询 或者语音回复查询皆可"

    def handle_ok(self, status):
        self.parse_data(status.data) 
        return u"%s 本学期已跑操 %s 次，其中平时 %s 次，周末 %s 次。\n最后一次跑操时间为：\n%s" % (status.name, str(self.times), str(self.weekday_c), str(self.weekend_c), self.date)

    def handle_failed_to_open(self, status):
        return u"由于网络原因，体育部网站暂时无法访问，请稍后再试"

    def handle_wrong_pwd(self, status):
        return u"登陆失败，请检查你的学号和姓名：\n%s %s" % (status.stu_id, status.name)

    def handle_unbind(self, status):
        return u"你还没有绑定，请先绑定"
