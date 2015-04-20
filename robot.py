#!/usr/bin/env python2.7
#coding:utf-8

import werobot
import re
from zccx.handle import Handle

robot = werobot.WeRoBot(token="kevince")
msg1 = u"欢迎使用南邮晨跑查询微信公众号\n"
msg2 = u"Developed by Kevince & Powered by https://github.com/prikevs/nupt-zccx\n"
msg3 = u"首先请进行绑定操作：\n输入 绑定+姓名+学号 例如\n绑定 田二狗 B13040216"
HELLO_MSG = msg1 + msg2 + msg3

@robot.subscribe
def wesubscribe(message):
    return HELLO_MSG

@robot.filter(u"查询")
def word_consult(message):
    h = Handle(message.source)
    return h.consult()

@robot.filter(re.compile(u"绑定(.*)"))
def webind(message):
    h = Handle(message.source)
    return h.bind(message.content)

@robot.voice
def voice_consult(message):
    if message.recognition == u"查询":
        h = Handle(message.source) 
        return h.consult()
    return "What are you talking about?"

@robot.text
def echo(message):
    return "请直接回复 查询 或者语音回复查询"

robot.run()
