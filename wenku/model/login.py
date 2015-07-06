#!/usr/bin/python
#encoding=utf-8

import sys
reload (sys)
sys.setdefaultencoding('utf-8')
from mysql_m import MysqlInfo

class LoginCheck(object):
    def __init__(self,username='',passwd='',table_name=''):
        self.username = username
        self.passwd = passwd
        self.table_name = table_name
    
    def login_check(self,username,passwd,table_name):
        mysqlinfo = MysqlInfo()
        b = 0
        data_user = mysqlinfo.get_data(table_name,1)
#print data_user
        for i in range(len(data_user)):
            if username == data_user[i].get('Username') and passwd == data_user[i].get('Passwd'):
                b = 1

        #print b
        return b


if __name__ == '__main__':
    logincheck = LoginCheck()
    print logincheck.login_check('tancj','tancj','User')
