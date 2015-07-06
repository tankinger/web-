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
from model.ikeda_mstx import ikeda_mstx


class Fsms1Handler(tornado.web.RequestHandler):
    def get(self):
        fsms=ikeda_mstx()
        name=fsms.name()
        address=fsms.address()
        telephone=fsms.telephone()
        #print u'name[0]'
        #print u'address[0]'
        #print u'telephone[0]'
        self.render('fsms1.html',
                    n1=name[0],
                    n2=name[1],
                    n3=name[2],
                    n4=name[3],
                    n5=name[4],
                    n6=name[5],
                    n7=name[6],
                    n8=name[7],
                    a1=address[0],
                    a2=address[1],
                    a3=address[2],
                    a4=address[3],
                    a5=address[4],
                    a6=address[5],
                    a7=address[6],
                    a8=address[7],
                    t1=telephone[0],
                    t2=telephone[1],
                    t3=telephone[2],
                    t4=telephone[3],
                    t5=telephone[4],
                    t6=telephone[5],
                    t7=telephone[6],
                    t8=telephone[7]
                   )
