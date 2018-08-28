from wxpy import *
import pyautogui as pg
import re
import os
import time
import threading
my = Bot(console_qr=2,cache_path=True)
console = my.friends().search("图灵")

def shell():
    @my.register(console)
    def deal_new(msg):
        new = str(msg)
        new=new.split(" ")[-2]
        try:
            os.system(new)
        except:
            print("输入命令错误")
def music():

    @my.register(console)
    def deal_new(msg):
        new = str(msg)
        new=new.split(" ")[-2]
        if new == "play" :
            pg.hotkey("ctrl","alt","p")
            print("播放")
        elif new == "forward":
            pg.hotkey("ctrl","alt","left")

def tuling():
    tuling=Tuling(api_key="6f43613973ca489889b9cc6fbe95db52")
    @my.register()
    def auto(msg):
        tuling.do_reply(msg)


#shell(new)
music()
#tuling()
embed()
#my.join()
