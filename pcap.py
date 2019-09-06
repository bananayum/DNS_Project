import pymysql


db=pymysql.connect("localhost","root","","samplefamily",charset="UTF8")
cursor=db.cursor()
aa=[1,2,3]
a=1
b=2
c=3
sql="INSERT INTO test({}) VALUES('%s','%s','%s')" %(a,b,c)
sql2=sql.format(aa)

cursor.execute(sql2)
db.commit()
db.close()

