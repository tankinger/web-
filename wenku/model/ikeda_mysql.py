#!/usr/bin/python
#encoding=utf-8
import MySQLdb
import sys
reload (sys)
sys.setdefaultencoding('utf-8')

class DBIOConnection:
    def net_conn(self,host='',user='',passwd='',db=''):
        self.host=host
        self.user=user
        self.passwd=passwd
        self.db=db
        conn=MySQLdb.connect(self.host,self.user,self.passwd,self.db,charset='utf8')
        cur=conn.cursor()
        kk="select * from mstx where id=(select max(id) from mstx)"
	count=cur.execute(kk)
	maxs=cur.fetchone()
	i=maxs[0]
        sql="select * from mstx"
	count=cur.execute(sql)
	result=cur.fetchmany(i)
	self.ID=[]
	self.zone=[]
	self.name1=[]
	self.name2=[]
	self.address=[]
	self.telephone=[]
	
	j=0
	while j<i:
            self.ID.append(result[j][0])
            self.zone.append(result[j][1])
            self.name1.append(result[j][2])
            self.name2.append(result[j][3])
            self.address.append(result[j][4])
            self.telephone.append(result[j][5])
            
            j+=1
	conn.commit()
	cur.close()
	conn.close()
	return (self.ID,self.zone,self.name1,self.name2,self.address,self.telephone,i)
	



    def update(self,host='',user='',passwd='',db='',*vs):
        self.host=host
        self.user=user
        self.passwd=passwd
        self.db=db        
        conn=MySQLdb.connect(self.host,self.user,self.passwd,self.db,charset='utf8')
        cur=conn.cursor()
        if vs is not None:
            cur.execute('update mstx set zone=%s,name1=%s,name2=%s,address=%s,telephone=%s where id=%s',vs) 
       	conn.commit()
	cur.close()
	conn.close()

    #def find(self,db,sheet,doc):
        #print('DBIO.find() is abstract!')
        #raise Exception('DBIO.find() is abstract!')

    #def update(self,db,sheet,spec,update):
        #print('DBIO.update() is abstract!')
        #raise Exception('DBIO.update() is abstract!')

    #def remove(self,db,sheet,spec_or_id):
        #print('DBIO.remove() is abstract!')
        #raise Exception('DBIO.remove() is abstract!')




