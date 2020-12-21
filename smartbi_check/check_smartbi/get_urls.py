# -*- coding = 'utf-8' -*-
"""

--------------------------------------------------------

File Name : get_urls

Description : 

Author : qiaowenfang

Date : 2020/12/7 11:23 上午

--------------------------------------------------------

"""
import pymysql
import pandas as pd
def geturl_from_database():
    db = pymysql.connect(host = "localhost", user = "root",password = "mysql12345" ,db = "mysql") # 本地那里，可以写IP地址；账户名；密码；数据库名；端口；编码（'utf-8'）
    cursor = db.cursor()
    cursor.execute("select * from checkurl") #
    da = cursor.fetchall()
    data = pd.DataFrame(list(da),columns=['id','url','statu']) # 结果是元组，需要转成list，再用pandas，
    return data # 操作在关闭数据库之前
    db.close()
    cursor.close()
