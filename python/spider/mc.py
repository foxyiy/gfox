import time
import requests
import urllib
import re
import threading
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from lxml import etree
from selenium.webdriver.support.wait import WebDriverWait

def x_html(url):
        
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36i",
            }
    response = requests.get(url,headers=headers)
    html = etree.HTML(response.text)
    return html

def kg_play():
    url = "http://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord="+wd
    brower= play(url)
    brower.find_element_by_xpath('//ul/li[1]/div/a/em').click()
    time.sleep(2)
    brower.switch_to_window(brower.window_handles[1])
    time.sleep(3)
    mp3_url = brower.current_url
    brower.close()
    patter = ".*hash=(.{32}).*=(.*)"
    attr = re.findall(patter,mp3_url)
    hash = attr[0][0]
    unix = int(time.time()*1000)
    id = attr[0][1]
    json = "http://www.kugou.com/yy/index.php?r=play/getdata&hash="+hash+"&album_id="+id+"&_="+str(unix)
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            }
    response = requests.get(json,headers=headers)
    dic = response.json()
    finaly_url = dic["data"]["play_url"]
    play(finaly_url)
def kw_play():
    url = "http://sou.kuwo.cn/ws/NSearch?type=all&catalog=yueku20177&key="+wd
    x_htm = x_html(url)

    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            }
    play_link = str(x_htm.xpath('//ul/li[1]/p[@class="listen"]/a/@href')[0])
    id = str(x_htm.xpath('//ul/li[1]/p/input/@value')[0])
    anti_url = "http://antiserver.kuwo.cn/anti.s?format=aac|mp3&rid=MUSIC_"+id+"&type=convert_url&response=res"
    play(anti_url)
    print(anti_url)

def QQ_play():
    url = "https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w="+wd   

    driver = play(url)
    driver.get((url))
    driver.find_element_by_class_name("mod_btn__icon_play").click()
    time.sleep(3)
    driver.switch_to_window(driver.window_handles[1])
    audio = driver.find_element_by_tag_name("audio")
    play_url = audio.get_property('src')
    driver.close()
    print(play_url)
    play(play_url)

def xm_play():
    
    url ="https://www.xiami.com/search?key="+wd
    option = Options()
    option.add_argument('--headless')
    driver = webdriver.Firefox()
    driver.get((url))
def wy_play():

    url = "https://music.163.com/#/search/m/?s="+wd
    option = Options()
    option.add_argument('--headless')
    driver = webdriver.Chrome()
    driver.get((url))
    play() 
def qy_play():

    url ="http://music.taihe.com/search?key="+wd
    option = Options()
    option.add_argument('--headless')
  #  driver = webdriver.Firefox()
   # driver.get(url)

    play()

def play(url):

    option = Options()
    option.add_argument('--headless')
    driver = webdriver.Firefox(options=option)
    driver.get(url)
    return driver
wd = input("请输入歌曲名：")
wd = urllib.request.quote(wd)
url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd="+wd 
kw_play()
    
