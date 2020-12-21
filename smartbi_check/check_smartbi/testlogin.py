# -*- coding = 'utf-8' -*-
"""

--------------------------------------------------------

File Name : testlogin

Description : 

Author : qiaowenfang

Date : 2020/12/9 1:54 下午

--------------------------------------------------------

"""
from bs4 import BeautifulSoup

from smartbi_login import login
import logging
import time
from time import ctime
import urllib.request
from smartbi_login import login
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
url = 'https://mnsmartbidev.mengniu.cn:7443/smartbi/vision/index.jsp'
login(url)
time.sleep(5)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
html = response.read()#.decode('GB2312')
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
current_user = soup.select('.item-dropdown.main_tone_near_hover_bgcolor').select('span')[0].text
print(current_user)