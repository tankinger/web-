#!/usr/bin/env python
#encoding=utf-8

import sys
reload (sys)
sys.setdefaultencoding('utf-8')
from data_operate import MysqlDataOperate

logincheck = MysqlDataOperate()
print logincheck.login_check('zhangwei','zhangwei','User')

