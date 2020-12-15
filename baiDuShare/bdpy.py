#! -*- encoding:utf-8 -*-
from selenium import webdriver
from time import sleep
import json

# cookie本地化，需要在30秒内完成认证，否则拿不到cookie
def get_cookie(driver,user,pwd,fztime=30):
    url = 'https://pan.baidu.com/pcloud/home'

    driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys(user)
    driver.find_element_by_id('TANGRAM__PSP_4__password').send_keys(pwd)
    driver.find_element_by_id('TANGRAM__PSP_4__submit').click()

    sleep(fztime)
    cookie=driver.get_cookies()
    with open('bd_cookie','w+') as f:
        f.write(json.dumps(cookie))

    return cookie


# 启用本地的cookie
def use_cookie(driver):
    url = 'https://pan.baidu.com/pcloud/home'
    driver.get(url)

    with open('bd_cookie', 'r') as f:
        data = json.loads(f.read())
    for i in data:
        driver.add_cookie(i)

    driver.refresh()


# 将分享链接保存到网盘的根目录，step默认间隔1秒，如果网络延长大，可以调高参数
def load2url(driver,url,passwd,fztime=1):
    driver.get(url)
    sleep(fztime)
    driver.find_element_by_id('accessCode').send_keys(passwd)
    sleep(fztime)
    driver.find_element_by_css_selector('#submitBtn > a').click()
    sleep(fztime)
    driver.find_element_by_css_selector('#layoutMain > div.frame-content > div.module-share-header > div > div.slide-show-right > div > div > div.x-button-box > a.g-button.g-button-blue').click()
    sleep(fztime)
    driver.find_element_by_css_selector('#fileTreeDialog > div.dialog-footer.g-clearfix > a.g-button.g-button-blue-large').click()






if __name__ =='__main__':
    driver = webdriver.Chrome()

    # 在没有本地cookie的时候取消注释，执行一次，然后检查本地是否生成了cookie文件
    # 这里的账号密码是百度云盘的账号密码
    # user = 'xxxx'
    # pwd = 'oooo'
    # get_cookie(driver,user,pwd)

    use_cookie(driver)


    # 处理分享链接，提取url和分享密码
    with open('share_url','r') as f:
        data = f.readlines()
    for i in data:
        url,passwd = i.split('\t')
        passwd = passwd.strip().replace('密码:','')

        print(url)
        load2url(driver, url, passwd,2)
        sleep(3)
