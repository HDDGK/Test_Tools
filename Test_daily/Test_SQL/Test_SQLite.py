import sqlite3
connect=sqlite3.connect('../Test_DB.db')
cursor=connect.cursor()
# cursor.execute('create table user(id int(10) primary key,name varchar(20))')
# cursor.execute('insert into user(id,name) values("2","MRSOFT")')
# cursor.execute('insert into user(id,name) values("5","MRSOFTs")')
# cursor.execute('insert into user(id,name) values("4","MRSOFTsr")')
#这里重复插入会报错：sqlite3.IntegrityError: UNIQUE constraint failed: user.id
print("#这里重复插入会报错：sqlite3.IntegrityError: UNIQUE constraint failed: user.id")
cursor.close()
connect.commit()
connect.close()

conn=sqlite3.connect('../Test_DB.db')
cu=conn.cursor()

print("\n更新一下数据。")
cu.execute('update user set name =? where id=?',("MR",1))
print("cu.execute('update user set name =? where id=?',(\"MR\",1))\n")

print("删除数据")
cu.execute('delete from user where id > ?',(3,))
print("cu.execute('delete from user where id > ?',(3,))\n")

print("选择一下合适的目标")
cu.execute('select * from user where id > ?',(0,))
print("cu.execute('select * from user where id > ?',(0,))")

#这里问号是占位符，(1,)相当于一个元组，这里怎么通过元组识别成>1，没懂
#注意，先选在更新，和先更新再选有区别



res=cu.fetchall()
print(res)
cu.close()
conn.close()