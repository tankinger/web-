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
from model.ikeda_mysql import DBIOConnection

class shujuHandler(tornado.web.RequestHandler):
    def get(self):
        id1 = (self.get_argument(name='id1',default=''))
        id2 = (self.get_argument(name='id2',default=''))
        id3 = (self.get_argument(name='id3',default=''))
        id4 = (self.get_argument(name='id4',default=''))

        host=id1
        user=id2
        passwd=id3
        db=id4
        #print zone
        #print name1
        #print telephone
        mySQL = DBIOConnection()
        #mySQL.net_conn(host,user,passwd,db)

        self.render('shuju.html',
                    i=0,
                    j=0

                  )
    def post(self):
        
        id1 = (self.get_argument(name='id1',default=''))
        id2 = (self.get_argument(name='id2',default=''))
        id3 = (self.get_argument(name='id3',default=''))
        id4 = (self.get_argument(name='id4',default=''))
        id = (self.get_argument(name='id',default=''))
        z = (self.get_argument(name='zone',default=''))
        n1 = (self.get_argument(name='name1',default=''))
        n2 = (self.get_argument(name='name2',default=''))
        add = (self.get_argument(name='address',default=''))
        tele = (self.get_argument(name='telephone',default=''))
        vs=[z,n1,n2,add,tele,id]
        host=id1
        user=id2
        passwd=id3
        db=id4
        mySQL = DBIOConnection()
        (ID,zone,name1,name2,address,telephone,i) = mySQL.net_conn(host,user,passwd,db)
        mySQL.update(host,user,passwd,db,*vs)
        print vs
        print id1
        print id2
        print id3
        print id4
        print id
        print z
        print n1
        print n2
        print add
        print tele
        
        self.render('shuju.html',
                    id=ID,
                    zone=zone,
                    name1=name1,
                    name2=name2,
                    address=address,
                    telephone=telephone,
                    i=i,
                    j = 0,
                    host=host,
                    user=user,
                    passwd=passwd,
                    db=db
                    
                    

                 )

