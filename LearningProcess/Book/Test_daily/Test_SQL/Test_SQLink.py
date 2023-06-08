import pymysql
print(r"C:\Users\HK145-TP\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages")
print(r"C:\Users\HK145-TP\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts")
'''
net start mysql80
mysql -u root -p
Hk145038
select database();
show tables;
create database ""RUNOON"";
'''
print("net start mysql80\n"
        "mysql -u root -p\n"
        "Hk145038\n"
        "select database();\n"
        "show tables;\n"
        "create database BGM;\n"
      "太他妈的傻逼了，链接的是SQL的库，需要在库里建一个才行\n ")
db=pymysql.connect(host="localhost",user="root",password="Hk145038",database="BGM")
cursor=db.cursor()
cursor.execute("SELECT VERSION()")
DB=cursor.fetchone()
print("Database version：%s"% DB)
cursor.execute("drop table if exists books")
sql="""
CREATE TABLE books(
    id int(8) NOT NULL AUTO_INCREMENT,
    name varchar(50) NOT NULL,
    category varchar(50) NOT NULL,
    price decimal(10,2) DEFAULT NULL,
    publish_time time date DEFAULT NULL,
    PRIMARY KEY (id)
)ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf-8;
"""
cursor.execute(sql)
db.close()

print("开始链接数据库")
db1=pymysql.connect(host="localhost",user="root",password="Hk145038",database="BGM",charset="utf-8")
print("已连接")
CDB=db1.cursor()
data1=[("零基础学 python","ptyhon","79.80","2018-10-1"),
       ("零基础学 pythoo","ptyhon","79.70","2018-10-2"),
       ("零基础学 pythop","ptyhon","79.60","2018-10-3"),
       ("零基础学 pythoq","ptyhon","79.50","2018-10-4")]
try:
    cursor.executemany("insert into books(name,category,price,publish_time)values(%s,%s,%s,%s)",data1)
    db1.commit()
except:
    db1.rollback()
db1.close()

