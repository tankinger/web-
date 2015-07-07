#encoding=utf-8

import tornado
import os.path
import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import uuid
from model.data_operate import MysqlDataOperate

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        try:
            table_name = 'User'
            self.Username = self.get_argument('inputUsername','')
            self.Passwd = self.get_argument('inputPassword','')
            print self.Username
            print self.Passwd
            mysql_data = MysqlDataOperate()
            login_info = mysql_data.login_check(self.Username,self.Passwd,table_name)
            if login_info[0]==True and login_info[1]==True:
                print '登录成功...'
                self.set_secure_cookie("UserName",self.UserName,expires_days=None)
                self.redirect('/index')
            else:
                print '登录失败...'
                self.redirect('/login')

        except Exception as e:
            print e
