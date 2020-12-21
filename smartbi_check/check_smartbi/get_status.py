# -*- coding = 'utf-8' -*-
"""

--------------------------------------------------------

File Name : get_status

Description : 

Author : qiaowenfang

Date : 2020/12/21 5:07 下午

--------------------------------------------------------

"""
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context # 不加时，报错 urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:833)>

def get_status(url):
    '''
    根据URL返回状态码,链接打不开时，代码抛出异常，链接能打开，返回状态码，
    分两种情况，code == 200,访问正常，code != 200,访问异常，
    :param url:
    :return:
    '''
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    request = urllib.request.Request(url, headers=headers)
    status = urllib.request.urlopen(request).code
    return status