#!/usr/bin/env python

import MySQLdb
from settings import HOST, USER, PASSWD, DBNAME, TABLE
import re

class DBHandler:
    sql0 = "SELECT stu_id, name FROM users WHERE token=%s"
    sql1 = "SELECT * FROM users WHERE token=%s"
    sql2 = "UPDATE users SET stu_id=%s, name=%s WHERE token=%s"
    sql3 = "INSERT INTO users (stu_id, name, token) VALUES (%s, %s, %s)"
    sql4 = "UPDATE users SET time=%s WHERE token=%s"

    def __init__(self, wetoken):
        self.token = wetoken
        self.conn = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DBNAME, charset='utf8')
        self.mycursor = self.conn.cursor()

    def get(self):
        self.mycursor.execute(self.sql0, (self.token))
        return self.mycursor.fetchall()

    def update(self, time):
        self.mycursor.execute(self.sql4, (time, self.token)) 
        self.conn.commit()

    def bind(self, name, stu_id):
        self.mycursor.execute(self.sql1, (self.token))
        want_in = (stu_id, name, self.token)
        if len(self.mycursor.fetchall()) != 0:
            self.mycursor.execute(self.sql2, want_in)
        else:
            self.mycursor.execute(self.sql3, want_in)
        self.conn.commit()

    def __del__(self):
        self.conn.close()
