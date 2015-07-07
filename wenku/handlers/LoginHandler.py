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
            self.Username = self.get_argument('inputUsername','')
            self.Passwd = self.get_argument('inputPassword','')
            print self.Username
            print self.Passwd

            

        except Exception as e:
            print e
