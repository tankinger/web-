#!/usr/bin/python
#encoding=utf-8

import sys
reload (sys)
sys.setdefaultencoding('utf-8')
from login import LoginCheck

logincheck = LoginCheck()
print logincheck.login_check('tanjr','tanjr','User')

