# -*- coding = 'utf-8' -*-
"""

--------------------------------------------------------

File Name : check_web

Description : 

Author : qiaowenfang

Date : 2020/12/7 10:37 上午

--------------------------------------------------------

"""

import time
from time import ctime
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context # 不加时，报错 urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:833)>

def getstatus(url):
    '''
    根据URL返回状态码可封装成函数
    '''
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    request = urllib.request.Request(url, headers=headers)
    time.sleep(30) # 60秒检测一次并返回页面状态码
    status = urllib.request.urlopen(request).code
    return status

def checkStatus(url):
    '''
    根据页面状态码判断访问是否正常
    异常超过三次就要发邮件、发钉钉
    检测是一直进行的

    :param url:
    :return:
    '''
    error_count = 0
    while 1:
        status = getstatus(url)
        if status != 200: #判断状态是否异常
            error_count += 1
        if status == 200:
            print(url,'访问正常',ctime()) # 返回信息待定
        if error_count >= 3: # 异常超过3次就要提醒
            print("send a email") # 发钉钉消息报警
            time.sleep(7200) # 访问异常时预留2小时解决问题
            break

# 针对单个链接
def checking(url):
    while 1:
        checkStatus(url)

if __name__ == '__main__':
    url = 'https://mnsmartbidev.mengniu.cn:7443/smartbi/vision/index.jsp'
    checking(url)

# 需要先得到URL然后再一直调用checkStatus()方法







