# -*- coding = 'utf-8' -*-
"""

--------------------------------------------------------

File Name : check_login

Description : 

Author : qiaowenfang

Date : 2020/12/8 11:38 上午

--------------------------------------------------------

"""
from bs4 import BeautifulSoup

from smartbi_login import login
import logging
import time
from time import ctime
import urllib.request

log = logging.getLogger(__name__)
'''


def check_smartbi_login(url):
    # 检测的是网络正常情况下的登录
    error_count = 0
    while 1:
        try: 
            login(url) # 光有这个不能判断登录正常//*[@id="topNavBanner"]/div/span[2]/span[1]
            
            print('登录正常',ctime())
            time.sleep(30)
        except Exception as e:
            # 发报警信息吧，看发什么
            log.info(e)
            print('can not login')
            error_count += 1
            raise e
        if error_count >= 3: # 异常超过3次就要提醒
            print("send a email") # 发钉钉消息报警
            time.sleep(3600) # 访问异常时预留2小时解决问题
            break
'''
def lg(url):

    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    current_user = soup.select('.item-dropdown.main_tone_near_hover_bgcolor').select('span')[0].text

    return current_user



def check_smartbi_login(url):
    # 检测的是网络正常情况下的登录
    error_count = 0
    while 1:
        try:
            login(url)  # 光有这个不能判断登录正常//*[@id="topNavBanner"]/div/span[2]/span[1]

            print('登录正常', ctime())
            time.sleep(30)
        except Exception as e:
            # 发报警信息吧，看发什么
            log.info(e)
            print('can not login')
            error_count += 1
            raise e
        if error_count >= 3:  # 异常超过3次就要提醒
            print("send a email")  # 发钉钉消息报警
            time.sleep(3600)  # 访问异常时预留2小时解决问题
            break




if __name__ == '__main__':
    # 代码本身需要6秒
    url = 'https://mnsmartbidev.mengniu.cn:7443/smartbi/vision/index.jsp'
    # check_smartbi_login(url)
    login(url)
    u = lg(url)
    print(u)

