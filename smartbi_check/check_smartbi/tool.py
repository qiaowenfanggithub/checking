# -*- coding = 'utf-8' -*-
"""

--------------------------------------------------------

File Name : tool

Description : 

Author : qiaowenfang

Date : 2020/12/21 5:02 下午

--------------------------------------------------------

"""
import logging
import logging.handlers
import pandas as pd
import pymysql
import datetime

def logger(logfile_name):
    logger = logging.getLogger()
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        format = "%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"
        handler_file = logging.FileHandler(logfile_name)
        handler_file.setFormatter(logging.Formatter(format))
        logger.addHandler(handler_file)
        handler_kztai = logging.StreamHandler()
        handler_kztai.setFormatter(logging.Formatter(format))
        logger.addHandler(handler_kztai)
    return logger

# 从数据库中取出数据
def geturl_from_database():
    db = pymysql.connect(host = "localhost", user = "root",password = "mysql12345" ,db = "mysql") # 本地那里，可以写IP地址；账户名；密码；数据库名；端口；编码（'utf-8'）
    cursor = db.cursor()
    cursor.execute("select * from checkurl") #
    da = cursor.fetchall()
    data = pd.DataFrame(list(da),columns=['id','url','url_name','url_type','founder','manager','cookie_type']) # 结果是元组，需要转成list，再用pandas，
    return data # 操作在关闭数据库之前
    db.close()
    cursor.close()

# 将数据写到数据库

def data_to_database(url,error_code):
    db = pymysql.connect(host = "localhost", user = "root",password = "mysql12345" ,db = "mysql") # 本地那里，可以写IP地址；账户名；密码；数据库名；端口；编码（'utf-8'）
    cursor = db.cursor()
    insert_sql = "insert into check_result(url,check_time,error_code) values(%s,%s,%s)"
    cursor.execute(insert_sql,[url,datetime.datetime.now(),error_code])
    db.commit()
    db.close()
    cursor.close()
