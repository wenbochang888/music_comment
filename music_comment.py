# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import re

def comment(url):
    driver = webdriver.PhantomJS()
    driver.get(url)
    driver.switch_to.frame(driver.find_element_by_name("contentFrame"))
    html = driver.page_source
    pa = re.compile("<.a>.{0,1}[\u4e00-\u9fa5].+?<.div>")
    dataList = pa.findall(html)

    dataList = str(dataList)
    dataList = re.sub('&nbsp;','', dataList)
    dataList = re.sub('<img.+?<.div>','',dataList)
    dataList = re.sub('</a>：','---', dataList)
    dataList = re.sub('</div>', '',dataList)
    dataList = re.sub("\', \'", '', dataList)
    dataList = re.sub("<a.+?</a>", '', dataList)
    dataList = re.sub('<br>', '', dataList)
    dataList = dataList.split('---')

    try:
        for x in range(1,15):
            print(str(x)+":  "+dataList[x] + "\n")
    except Exception as e:
        print("出问题了 不过不用担心")

# 薛之谦的热门歌曲30首
url = "http://music.163.com/#/artist?id=5781"
driver = webdriver.PhantomJS()
driver.get(url)
driver.switch_to.frame(driver.find_element_by_name("contentFrame"))
html = driver.page_source

bsObj = BeautifulSoup(html, 'html.parser')
dataList = bsObj.findAll(name = 'a', attrs = {'href':re.compile(r'/song.id=\d{1,10}')})
for data in dataList:
    print(data.string + "   http://music.163.com/#"+data.attrs['href'])
    comment("http://music.163.com/#"+data.attrs['href'])










