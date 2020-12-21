# -*- coding = 'utf-8' -*-
"""

--------------------------------------------------------

File Name : check_login

Description : 

Author : qiaowenfang

Date : 2020/12/8 11:38 上午

--------------------------------------------------------

"""
from get_status import get_status
import time
from tool import data_to_database,logger
from check_smartbi_login import check_smartbi_blogin


def check_login(url):
    # 检测的是网络正常情况下的登录
    log = logger('check_login.log')
    error_count = 0
    while 1:
        time.sleep(5)  # 多长时间检测一次60
        try:
            status = get_status(url)
            if status == 200:
                try:
                    if check_smartbi_blogin(url):
                        data_to_database(url, '')
                        log.info('%s:登录成功'%(url))
                    elif check_smartbi_blogin(url) != True:
                        error_count += 1
                        data_to_database(url, '1_0_2')
                        log.info('%s:登录页跳转失败;错误码:%s' % (url, '1_0_2'))
                except Exception:
                    error_count += 1
                    data_to_database(url, '1_0_1')
                    log.info('%s:登录页填写信息正常，跳转时崩溃;错误码:%s' % (url, '1_0_1'))
            elif status != 200:
                error_count += 1
                data_to_database(url, '1_0_0')
                log.info('%s:登录页访问异常;错误码:%s'%(url,'1_0_0'))
        except Exception as e:
            error_count += 1
            data_to_database(url, '1_0_0')
            log.info('%s:登录页访问异常;错误码:%s'%(url,'1_0_0'))
        if error_count >= 3:  # 异常超过3次就要提醒
            print("send an email")  # 发钉钉消息报警
            time.sleep(10)  # 访问异常时预留2小时解决问题7200
            break

# 针对单个URL
def login_checking(url):
    while 1:
        check_login(url)
if __name__ == '__main__':

    url = 'https://mnsmartbi.mengniu.cn/smartbi/vision/index.jsp'
    login_checking(url)

