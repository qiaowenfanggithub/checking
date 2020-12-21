# -*- coding = 'utf-8' -*-
"""

--------------------------------------------------------

File Name : check_logins

Description : 

Author : qiaowenfang

Date : 2020/12/21 5:01 下午

--------------------------------------------------------

"""
from check_login import login_checking
import threading
from time import ctime
from tool import geturl_from_database
data = geturl_from_database() # 从数据库中拿到url
urls = data[data.url_type == 1]['url']
threads = []
for url in urls: # 遍历链接
    turl = threading.Thread(target=login_checking, args=(url,)) # 不同的链接给到不同的函数处理
    threads.append(turl)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()

    # 当网络打不开首页时 执行，待完成

    print("all over %s" % ctime())
    print("can not get access to the Internet") #



