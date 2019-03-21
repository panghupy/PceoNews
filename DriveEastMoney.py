import requests
import time
import random
import json
import csv
from selenium import webdriver

'''
selenium获取cookie并保存在csv文件
'''


def writeCookie():
    opt = webdriver.ChromeOptions()

    # 把chrome设置成为无界面模式
    opt.set_headless()

    # 创建chrome无界面对象
    # browser = webdriver.Chrome(options=opt, executable_path='/home/djs/Desktop/chromedriver')

    # 创建chrome有界面对象
    browser = webdriver.Chrome(executable_path='/home/djs/Desktop/chromedriver')
    url = 'http://www.eastmoney.com/'
    browser.get(url)
    browser.find_element_by_id('code_suggest').send_keys('科创板')
    browser.find_element_by_id('search_view_btn3').click()
    time.sleep(3)

    browser.find_element_by_class_name('container').find_element_by_link_text('资讯').click()

    time.sleep(10)
    cookie_data = {}
    for cookie in browser.get_cookies():
        cookie_data[cookie['name']] = cookie['value']
    list = [
        cookie_data
    ]
    csvfile = open('cookie.csv', 'w')
    # csv文件的头
    fieldnames = [i for i in cookie_data]
    writehandler = csv.DictWriter(csvfile, fieldnames)
    # 写入头
    writehandler.writeheader()
    # 写入数据

    writehandler.writerows(list)
    csvfile.close()

writeCookie()
