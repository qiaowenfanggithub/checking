# -*- coding = 'utf-8' -*-
"""

--------------------------------------------------------

File Name : get_cookies

Description : 

Author : qiaowenfang

Date : 2020/12/21 5:09 下午

--------------------------------------------------------

"""
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tool import logger
'''

# 登录页面和登录后页面链接一样，怎么判断登录成功，登录页面的cookie 和登录后的页面cookie 一样，但是爬下面的页面是不一样的，登录后的页面爬下来的带user，所以通过这个点差别可判断是否登录成功
# 这里好像不应该抛出异常
def get_cookie(url):
    # 参数：url,用户名，密码
    # 功能：模拟浏览器打开Smartbi首页，清空原来的账户密码，填入测试账户的账户和密码，登录后跳转到下一页面，拿到跳转后页面的cookie，并返回
    # 类型： 访问 -> 登录
    # 前提：首页可正常访问
    log = logger('get_cookie.log')
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        path = '../driver/chromedriver'  # chrome 浏览器驱动地址 当前目录的上层目录下的driver文件夹下的chromedriver  ### 代码复用时，这里可能需要改
        driver = webdriver.Chrome(executable_path=path, chrome_options=options) # 驱动浏览器
        driver.maximize_window()  # 最大化
        driver.get(url)
        log.info('打开模拟浏览器成功')
    except Exception as e:
        log.info(e)
        raise e
    try:
        username = driver.find_elements_by_xpath('//div[@class = "login-block login-user-input"]/input')[0]  # 这里不写【0】报错提示是个list,所以取一个 ### 代码复用时，这里需要改
        username.clear()  # 清空
        username.send_keys("0116719")  # 自动填值
        password = driver.find_elements_by_xpath('//div[@class = "login-block login-pass-input"]/input')[0] ### 代码复用时，这里需要改
        password.clear()  # 清空
        password.send_keys("Abc1234.com")  # 自动填值
        driver.find_elements_by_xpath('//div[@class = "login-block login-submit"]/input')[0].click() ### 代码复用时，这里需要改
        log.info('打开模拟浏览器成功，填入账号密码成功')
        driver.get(url)
        cookie_list = driver.get_cookies()
        cookies = []
        for cookie in cookie_list:
            cookies.append('%s=%s'%(cookie['name'],cookie['value']))
        log.info('获取cookie成功')
        return cookies#[0]#+';'+cookies[1]
    except Exception as e:
        log.info(e)
        # raise e
'''
def get_cookie(url):
    log = logger('get_cookie.log')
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    path = '../driver/chromedriver'  # chrome 浏览器驱动地址 当前目录的上层目录下的driver文件夹下的chromedriver  ### 代码复用时，这里可能需要改
    driver = webdriver.Chrome(executable_path=path, chrome_options=options) # 驱动浏览器
    driver.maximize_window()  # 最大化
    driver.get(url)
    log.info('%s:登录时打开模拟浏览器成功'%(url))
    username = driver.find_elements_by_xpath('//div[@class = "login-block login-user-input"]/input')[0]  # 这里不写【0】报错提示是个list,所以取一个 ### 代码复用时，这里需要改
    username.clear()  # 清空
    username.send_keys("0116719")  # 自动填值
    password = driver.find_elements_by_xpath('//div[@class = "login-block login-pass-input"]/input')[0] ### 代码复用时，这里需要改
    password.clear()  # 清空
    password.send_keys("Abc1234.com")  # 自动填值
    driver.find_elements_by_xpath('//div[@class = "login-block login-submit"]/input')[0].click() ### 代码复用时，这里需要改
    log.info('%s:登录时打开模拟浏览器成功，填入账号密码成功'%(url))
    driver.get(url)
    cookie_list = driver.get_cookies()
    cookies = []
    for cookie in cookie_list:
        cookies.append('%s=%s'%(cookie['name'],cookie['value']))
    log.info('%s:获取cookie成功'%(url))
    return cookies

if __name__ == '__main__':
    # 页面错误时，直接报错 list index out of range 无网络时直接报错 Message: unknown error: net::ERR_INTERNET_DISCONNECTED


    url = 'https://mnsmartbi.mengniu.cn/smartbi/vision/openresource.jsp?resid=I8a4886f301759bab9babaa470175de06d19b1a39'
    # url = 'https://mnsmartbi.mengniu.cn/smartbi/vision/index.jsp'

    cookie = get_cookie(url) # 账号密码错误时，也可以拿到cookie
    print(cookie)
    print(get_cookie(url)[1]+'; '+get_cookie(url)[0])


