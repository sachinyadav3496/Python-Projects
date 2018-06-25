import pymysql as sql
db = sql.connect('localhost','my_project','redhat','my_project')
c = db.cursor()

f = open('data_set.csv')

for line in f :
    d = line.split(',')
    d[4] = d[4][:-1]
    cmd = "insert into myapp_users(Name,First_Name,Last_Name,Email,Password) values('{}','{}','{}','{}','{}')".format(d[0],d[1],d[2],d[3],d[4])
    c.execute(cmd)

db.commit()
c.close()
db.close()
