# -*- coding = 'utf-8' -*-
"""

--------------------------------------------------------

File Name : check_smartbi_login

Description : 

Author : qiaowenfang

Date : 2020/12/21 5:08 下午

--------------------------------------------------------

"""
from urllib import request
import urllib.request
from bs4 import BeautifulSoup
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from get_cookies import get_cookie
from tool import logger

'''
登录跳转后,在跳转后的页面找cookie 然后访问新页面找到就是登陆成功了
这里不能抛出异常，调用它的函数得用这个异常
'''
def check_smartbi_blogin(url):
    '''
    网页打不开，直接报错
    能匹配"0116719"返回True
    能打开匹配不到返回None
    :param url:
    :return:
    '''
    cookie = get_cookie(url)[1]+'; '+get_cookie(url)[0]
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    headers = {'User-Agent': user_agent, 'Cookie': cookie}
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode()  # .decode('GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    appConfigs = soup.select('script')[0].contents[0] # contents 是拿到标签里的内容，是调试的时候看出来的
    user = appConfigs[878:885] # 取到用户账户，也可以用正则表达式
    if user == '0116719': # 如果能取到就是登录成功了，测试账号写死的
        return True
if __name__ == '__main__':
    url = 'https://mnsmartbi.mengniu.cn/smartbi/vision/index.jsp'
    if check_smartbi_blogin(url):
        print('it is true')
    elif check_smartbi_blogin(url) != True:
        print('there is nothing')


