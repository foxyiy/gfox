from selenium import webdriver
import requests
from lxml import etree
from pymongo import *
import time
def Score_sheet():
    #模拟登录
    for num in range(16010315110,16010315126):
        option = webdriver.ChromeOptions()
        option.set_headless()
        brower = webdriver.Chrome(options=option)
        brower.get("http://222.25.2.82/eams/loginExt.action")
        try:
            brower.find_element_by_id("username").send_keys(num)
            brower.find_element_by_id("password").send_keys(num)
            brower.find_element_by_xpath("//input[@type='submit']").click()
        except:
            print("密码错误")

        
        cookies=brower.get_cookies()
        cook = {}
        for i in cookies:
            key = i["name"]
            value = i["value"]
            cook[key]=value
        r = requests.session()
        res=r.get("http://222.25.2.82/eams/teach/grade/course/person!search.action?semesterId=41&projectType=&_=1533816923016",cookies=cook)
        html=etree.HTML(res.text)
        class_name=html.xpath("//tbody/tr/td[4]")
        score = html.xpath("//tbody/tr/td[9]")
        
        time.sleep(3)
        #time.sleep(3)
        #brower.get("http://222.25.2.82/eams/teach/grade/course/person!search.action?semesterId=41&projectType=&_=1533366272282")
        #class_name = brower.find_elements_by_xpath("//tbody/tr/td[4]")
        #score = brower.find_elements_by_xpath(("//tbody/tr/td[9]"))
        person_score = {}
        all_score = []
        for j in range(len(score)):
            person_score["学号"]=num
            try:
                person_score[class_name[j].text] = int(score[j].text)
            except:
                person_score[class_name[j].text] = score[j].text
        yield person_score

client = MongoClient(host="localhost",port=27017)
db=client.py3
score_sheet = Score_sheet()

for person in score_sheet: 
    db.stu.insert_one(person)
