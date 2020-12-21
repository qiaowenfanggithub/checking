# -*- coding = 'utf-8' -*-
"""

--------------------------------------------------------

File Name : check_webs_withlogin

Description : 

Author : qiaowenfang

Date : 2020/12/8 1:49 下午

--------------------------------------------------------

"""

from check_web import checking
from get_urls import geturl_from_database
import threading
from time import ctime,sleep

data = geturl_from_database() # 从数据库中拿到url
url_smartbiindex = data[data['statu'] == 0]['url'] # url 分类
url_nologin = data[data['statu'] == 1]['url'] # url 分类

threads = []
for url_login,url_nolo in zip(url_smartbiindex,url_nologin): # 遍历链接
    turl_login = threading.Thread(target=checking, args=(url_login,)) # 不同的链接给到不同的函数处理
    turl_nolo = threading.Thread(target=checking, args=(url_nolo,))
    threads.append(turl_login)
    threads.append(turl_nolo)
# 现在的问题是，检测一个链接，是需要一直检测下来，那再来一个链接怎么检测呢？
if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()

    print("all over %s" % ctime())









