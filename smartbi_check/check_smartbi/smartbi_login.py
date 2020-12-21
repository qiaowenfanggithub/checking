# -*- coding = 'utf-8' -*-
"""

--------------------------------------------------------

File Name : smartbi_login

Description : 

Author : qiaowenfang

Date : 2020/12/2 2:12 下午

--------------------------------------------------------

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 获取网页
# 测试账号是否要拿出来，还是写死，待完成
# log 及入库信息待完成
def login(url):
    options = Options()
    # path = '/Users/chuckzhao/Documents/qwf/mengniu/driver/chromedriver'# chrome 浏览器驱动地址 绝对路径
    path = '../driver/chromedriver'  # chrome 浏览器驱动地址 当前目录的上层目录下的driver文件夹下的chromedriver
    driver = webdriver.Chrome(executable_path=path, chrome_options=options)  # 驱动浏览器
    driver.maximize_window()  # 最大化
    driver.get(url)
    username = driver.find_elements_by_xpath('//div[@class = "login-block login-user-input"]/input')[0] # 这里不写【0】报错提示是个list,所以取一个
    username.clear()  # 清空
    username.send_keys("0116719")  # 自动填值
    password = driver.find_elements_by_xpath('//div[@class = "login-block login-pass-input"]/input')[0]
    password.clear()  # 清空
    password.send_keys("Abc1234.com")  # 自动填值
    driver.find_elements_by_xpath('//div[@class = "login-block login-submit"]/input')[0].click()
if __name__ == '__main__':
    login('https://mnsmartbidev.mengniu.cn:7443/smartbi/vision/index.jsp')

# try:
#     login(url)
#     print('登录正常')  # 返回信息待定
# except Exception as e:
#     logging.log.info(e)
#     raise e
#     print('登录异常')  # 发钉钉消息报警




