# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:41:46 2020

@author: zxw
"""
# 引入必要的库
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
import json
import time
import re

def get_driver():
    try:
        return webdriver.PhantomJS()
    except Exception:
        option = ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        return webdriver.Chrome(executable_path=r"F:\chromedriver.exe",options=option)


# 得到登录的cookie
def login_cookie():
    driver = get_driver()
    driver.set_page_load_timeout(20)
    driver.set_script_timeout(20)
    LOGIN_URL = 'https://www.zhihu.com/'
    driver.get(LOGIN_URL)
    time.sleep(5)
    input("请登录后按 Enter")
    cookies = driver.get_cookies()
    jsonCookies = json.dumps(cookies)
    #下面的文件位置需要自己改
    with open('zhihu.txt','w') as f:
        f.write(jsonCookies)
    driver.quit()

# 再次登录
def login():
    driver.set_page_load_timeout(20)
    driver.set_script_timeout(20)
    LOGIN_URL ='https://www.zhihu.com/'
    driver.get(LOGIN_URL)
    time.sleep(5)
    #下面的文件位置需要自己改，与上面的改动一致
    f = open('zhihu.txt')
    cookies = f.read()
    jsonCookies = json.loads(cookies)
    for co in jsonCookies:
        driver.add_cookie(co)
    driver.refresh()
    time.sleep(5)

# 爬取某问题下的所有答案
def get_answers(question_url):
    driver.get(question_url)
    number_text = driver.find_element_by_partial_link_text('查看全部').text
    number = int(re.search('[0-9]+',number_text).group())
    driver.find_element_by_partial_link_text('查看全部').click()
    for k in range(number):
        xpath = '/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[{}]/div/div[2]/div[1]/span'.format(k+1)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        answer = element.text
        #下面的文件位置需要自己改，保存到你想要的位置
        file = open('answer{}.txt'.format(k+1),'w',encoding='utf-8')
        file.write(answer)
        file.close()
        print('answer '+ str(k+1) +' collected!')
        time.sleep(1)
        js="window.scrollTo(0,document.body.scrollHeight)"
        driver.execute_script(js)
        time.sleep(1)

if __name__ == "__main__":
    # 设置你想要搜索的问题
    question_url ='https://www.zhihu.com/question/21592677/answer/142800018'
    login_cookie()
    driver = get_driver()
    login()
    get_answers(question_url)
