#!/usr/bin/python
#encoding=utf-8
import MySQLdb
import sys
# reload (sys)
# sys.setdefaultencoding('utf-8')

class kkk():
	def kkk(self):
		
		conn=MySQLdb.connect(host='10.9.32.162',user='root',passwd='19830219',db='k1')
		cur=conn.cursor()

		sql="select * from k1"
		count=cur.execute(sql)
		result=cur.fetchone()
		print result
		kkk=[]
		

		j=0
		while j<3:
			kkk.append(result[j])
			j+=1
		conn.commit()
		cur.close()
	
		conn.close()
		return kkk
