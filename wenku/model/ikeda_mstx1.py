#!/usr/bin/python
#encoding=utf-8
import MySQLdb
import sys
reload (sys)
sys.setdefaultencoding('utf-8')


		
conn=MySQLdb.connect(host='10.9.32.162',user='root',passwd='19830219',db='ikeda',charset='utf8')
		#mysql_query("SET NAMES 'GBK'");
cur=conn.cursor()
vs=["佛山美食","骑楼西餐厅",'3']    
cur.execute('update mstx set zone=%s,name1=%s where id=%s',vs)
conn.commit()
cur.close()
	
conn.close()



			
			
			
			
			
			
		
	

		
