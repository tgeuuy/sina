import pymysql.cursors

# 连接数据库
connect = pymysql.Connect(
    host='rm-wz9325c14dsxj3l0kko.mysql.rds.aliyuncs.com',
    port=3306,
    user='root',
    passwd='zengjindong2018',
    db='phone_num',
    charset='utf8'
)

# 获取游标
cursor = connect.cursor()

# # 插入数据
# sql = "INSERT INTO trade (name, account, saving) VALUES ( '%s', '%s', %.2f )"
# data = ('雷军', '13512345678', 10000)
# cursor.execute(sql % data)
# connect.commit()
# print('成功插入', cursor.rowcount, '条数据')
#
# # 修改数据
# sql = "UPDATE trade SET saving = %.2f WHERE account = '%s' "
# data = (8888, '13512345678')
# cursor.execute(sql % data)
# connect.commit()
# print('成功修改', cursor.rowcount, '条数据')

# 查询数据
# sql = "SELECT name,saving FROM trade WHERE account = '%s' "
sql="select * from data"
# data = ('13512345678',)
cursor.execute(sql )
leibie=set()
count=100
for row in cursor.fetchall():
    # print( row[3])
    # filepath="news/"+row[3]+"/"++str(count)
    # count=count+1
    # print(filepath)
    leibie.add(row[3])
print('共查找出', cursor.rowcount, '条数据')
print(leibie)
# # 删除数据
# sql = "DELETE FROM trade WHERE account = '%s' LIMIT %d"
# data = ('13512345678', 1)
# cursor.execute(sql % data)
# connect.commit()
# print('成功删除', cursor.rowcount, '条数据')

# # 事务处理
# sql_1 = "UPDATE trade SET saving = saving + 1000 WHERE account = '18012345678' "
# sql_2 = "UPDATE trade SET expend = expend + 1000 WHERE account = '18012345678' "
# sql_3 = "UPDATE trade SET income = income + 2000 WHERE account = '18012345678' "

# try:
#     cursor.execute(sql_1)  # 储蓄增加1000
#     cursor.execute(sql_2)  # 支出增加1000
#     cursor.execute(sql_3)  # 收入增加2000
# except Exception as e:
#     connect.rollback()  # 事务回滚
#     print('事务处理失败', e)
# else:
#     connect.commit()  # 事务提交
#     print('事务处理成功', cursor.rowcount)

# 关闭连接
cursor.close()
connect.close()