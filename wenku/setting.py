#encoding=utf-8

## Copyright (C), 2013-2014, ****.
## File name:       setting.py
## Author:          liutao    liutaoup@gmail.com
## Version:         0.1.7
## Date:            2013-09-10
## Description:     settings for server
## Others:          none
## History:         none 
##   1. Date:
##      Author:
##      Modification:
##   2. ...

import os
from  handlers.MysqlHandler import mysqlHandler
from  handlers.shujuHandler import shujuHandler




PORT = '8888'

SETTINGS = dict(
    template_path = os.path.join(os.path.dirname(__file__),"templates"),
    static_path = os.path.join(os.path.dirname(__file__),"static"),
    )

urls = [
  
    (r'/mysql.html',mysqlHandler),
    (r'/shuju.html',shujuHandler)
    
]
myCookeSecret="KCSSGoodLuckComeOn"
