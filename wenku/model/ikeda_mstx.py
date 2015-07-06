#!/usr/bin/python
#encoding=utf-8
import MySQLdb
import sys
reload (sys)
sys.setdefaultencoding('utf-8')

class ikeda_mstx():
	def ID(self):
		
		conn=MySQLdb.connect(host='192.168.1.107',user='root',passwd='19830219',db='ikeda',charset='utf8')
		#mysql_query("SET NAMES 'GBK'");
		cur=conn.cursor()
#get max id
                kk="select * from mstx where id=(select max(id) from mstx)"
                count=cur.execute(kk)
                maxs=cur.fetchone()
                i=maxs[0]

#search all information
		sql="select * from mstx"
		count=cur.execute(sql)
		result=cur.fetchmany(i)
		print result
		ID=[]
		

		j=0
		while j<i:
			ID.append(result[j][0])
			j+=1
		conn.commit()
		cur.close()
	
		conn.close()
		return ID


	def zone(self):
		
		conn=MySQLdb.connect(host='192.168.1.107',user='root',passwd='19830219',db='ikeda',charset='utf8')
		#mysql_query("SET NAMES 'GBK'");
		cur=conn.cursor()
		kk="select * from mstx where id=(select max(id) from mstx)"
		count=cur.execute(kk)
		maxs=cur.fetchone()
		i=maxs[0]
		sql="select * from mstx"
		count=cur.execute(sql)
		result=cur.fetchmany(i)
		zone=[]
		j=0
		while j<i:
			zone.append(result[j][1])
			j+=1
		conn.commit()
		cur.close()
		conn.close()
		return zone


	def name1(self):
		
		conn=MySQLdb.connect(host='192.168.1.107',user='root',passwd='19830219',db='ikeda',charset='utf8')
		#mysql_query("SET NAMES 'GBK'");
		cur=conn.cursor()
		kk="select * from mstx where id=(select max(id) from mstx)"
		count=cur.execute(kk)
		maxs=cur.fetchone()
		i=maxs[0]
		sql="select * from mstx"
		count=cur.execute(sql)
		result=cur.fetchmany(i)
		name1=[]
		j=0
		while j<i:
			name1.append(result[j][2])
			j+=1
		conn.commit()
		cur.close()
		conn.close()
		return name1
			



	def name2(self):
		
		conn=MySQLdb.connect(host='192.168.1.107',user='root',passwd='19830219',db='ikeda',charset='utf8')
		#mysql_query("SET NAMES 'GBK'");
		cur=conn.cursor()
		kk="select * from mstx where id=(select max(id) from mstx)"
		count=cur.execute(kk)
		maxs=cur.fetchone()
		i=maxs[0]
		sql="select * from mstx"
		count=cur.execute(sql)
		result=cur.fetchmany(i)
		name2=[]
		j=0
		while j<i:
			name2.append(result[j][3])
			j+=1
		conn.commit()
		cur.close()
		conn.close()
		return name2



	def address(self):
		
		conn=MySQLdb.connect(host='192.168.1.107',user='root',passwd='19830219',db='ikeda',charset='utf8')
		#mysql_query("SET NAMES 'GBK'");
		cur=conn.cursor()
		kk="select * from mstx where id=(select max(id) from mstx)"
		count=cur.execute(kk)
		maxs=cur.fetchone()
		i=maxs[0]
		sql="select * from mstx"
		count=cur.execute(sql)
		result=cur.fetchmany(i)
		address=[]
		j=0
		while j<i:
			address.append(result[j][4])
			j+=1
		conn.commit()
		cur.close()
		conn.close()
		return address



	def telephone(self):
		
		conn=MySQLdb.connect(host='192.168.1.107',user='root',passwd='19830219',db='ikeda',charset='utf8')
		#mysql_query("SET NAMES 'GBK'");
		cur=conn.cursor()
		kk="select * from mstx where id=(select max(id) from mstx)"
		count=cur.execute(kk)
		maxs=cur.fetchone()
		i=maxs[0]
		sql="select * from mstx"
		count=cur.execute(sql)
		result=cur.fetchmany(i)
		telephone=[]
		j=0
		while j<i:
			telephone.append(result[j][5])
			j+=1
		conn.commit()
		cur.close()
		conn.close()
		return telephone



	def map1(self):
		
		conn=MySQLdb.connect(host='192.168.1.107',user='root',passwd='19830219',db='ikeda',charset='utf8')
		#mysql_query("SET NAMES 'GBK'");
		cur=conn.cursor()
		kk="select * from mstx where id=(select max(id) from mstx)"
		count=cur.execute(kk)
		maxs=cur.fetchone()
		i=maxs[0]
		sql="select * from mstx"
		count=cur.execute(sql)
		result=cur.fetchmany(i)
		map1=[]
		j=0
		while j<i:
			map1.append(result[j][6])
			j+=1
		conn.commit()
		cur.close()
		conn.close()
		return map1



	def pic1(self):
		
		conn=MySQLdb.connect(host='192.168.1.107',user='root',passwd='19830219',db='ikeda',charset='utf8')
		#mysql_query("SET NAMES 'GBK'");
		cur=conn.cursor()
		kk="select * from mstx where id=(select max(id) from mstx)"
		count=cur.execute(kk)
		maxs=cur.fetchone()
		i=maxs[0]
		sql="select * from mstx"
		count=cur.execute(sql)
		result=cur.fetchmany(i)
		pic1=[]
		j=0
		while j<i:
			pic1.append(result[j][8])
			j+=1
		conn.commit()
		cur.close()
		conn.close()
		return pic1



	def pic2(self):
		
		conn=MySQLdb.connect(host='192.168.1.107',user='root',passwd='19830219',db='ikeda',charset='utf8')
		#mysql_query("SET NAMES 'GBK'");
		cur=conn.cursor()
		kk="select * from mstx where id=(select max(id) from mstx)"
		count=cur.execute(kk)
		maxs=cur.fetchone()
		i=maxs[0]
		sql="select * from mstx"
		count=cur.execute(sql)
		result=cur.fetchmany(i)
		pic2=[]
		j=0
		while j<i:
			pic2.append(result[j][9])
			j+=1
		conn.commit()
		cur.close()
		conn.close()
		return pic2



	def pic3(self):
		
		conn=MySQLdb.connect(host='192.168.1.107',user='root',passwd='19830219',db='ikeda',charset='utf8')
		#mysql_query("SET NAMES 'GBK'");
		cur=conn.cursor()
		kk="select * from mstx where id=(select max(id) from mstx)"
		count=cur.execute(kk)
		maxs=cur.fetchone()
		i=maxs[0]
		sql="select * from mstx"
		count=cur.execute(sql)
		result=cur.fetchmany(i)
		pic3=[]
		j=0
		while j<i:
			pic3.append(result[j][10])
			j+=1
		conn.commit()
		cur.close()
		conn.close()
		return pic3



	def pic4(self):
		
		conn=MySQLdb.connect(host='192.168.1.107',user='root',passwd='19830219',db='ikeda',charset='utf8')
		#mysql_query("SET NAMES 'GBK'");
		cur=conn.cursor()
		kk="select * from mstx where id=(select max(id) from mstx)"
		count=cur.execute(kk)
		maxs=cur.fetchone()
		i=maxs[0]
		sql="select * from mstx"
		count=cur.execute(sql)
		result=cur.fetchmany(i)
		pic4=[]
		j=0
		while j<i:
			pic4.append(result[j][11])
			j+=1
		conn.commit()
		cur.close()
		conn.close()
		return pic4


	def background(self):
		
		conn=MySQLdb.connect(host='192.168.1.107',user='root',passwd='19830219',db='ikeda',charset='utf8')
		#mysql_query("SET NAMES 'GBK'");
		cur=conn.cursor()
		kk="select * from mstx where id=(select max(id) from mstx)"
		count=cur.execute(kk)
		maxs=cur.fetchone()
		i=maxs[0]
		sql="select * from mstx"
		count=cur.execute(sql)
		result=cur.fetchmany(i)
		background=[]
		j=0
		while j<i:
			background.append(result[j][12])
			j+=1
		conn.commit()
		cur.close()
		conn.close()
		return background


	def mapfd(self):
		
		conn=MySQLdb.connect(host='192.168.1.107',user='root',passwd='19830219',db='ikeda',charset='utf8')
		#mysql_query("SET NAMES 'GBK'");
		cur=conn.cursor()
		kk="select * from mstx where id=(select max(id) from mstx)"
		count=cur.execute(kk)
		maxs=cur.fetchone()
		i=maxs[0]
		sql="select * from mstx"
		count=cur.execute(sql)
		result=cur.fetchmany(i)
		mapfd=[]
		j=0
		while j<i:
			mapfd.append(result[j][7])
			j+=1
		conn.commit()
		cur.close()
		conn.close()
		return mapfd



			
			
			
			
			
			
		
	

		
