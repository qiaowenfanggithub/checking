# -*- coding = 'utf-8' -*-
"""

--------------------------------------------------------

File Name : check_smartbi

Description : 

Author : qiaowenfang

Date : 2020/12/7 10:39 上午

--------------------------------------------------------

"""

from check_web import checking
from get_urls import geturl_from_database
import threading
from time import ctime,sleep

data = geturl_from_database() # 从数据库中拿到url
'''
链接只要加进来就可以，线程只要加进来就可以
'''

urls = data['url']
threads = []
for url in urls: # 遍历链接
    turl = threading.Thread(target=checking, args=(url,)) # 不同的链接给到不同的函数处理
    threads.append(turl)


if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()

    # 当网络打不开首页时 执行，待完成

    print("all over %s" % ctime())
    print("can not get access to the Internet") #





