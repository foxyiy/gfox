import cv2
import time
import os 
import random
import numpy

#截图上传到当前目录
def get_img():
    os.system("adb shell screencap -p /sdcard/jump.png")
    os.system("adb pull /sdcard/jump.png ./jump.png")
    #删除手机中的截图
    os.system("adb shell rm /sdcard/jump.png")

#得到人物位置
def get_play_point():
    img = cv2.imread("jump.png")
    #对截图尺寸调节为原来的四分之一
    player = cv2.imread("play.png")
    img = cv2.resize(img,(0,0),fx=0.25,fy=0.25)
    #进行模板匹配人物位置
    player = cv2.matchTemplate(img,player,cv2.TM_CCOEFF_NORMED)
    #play_poit 为匹配到的位置 
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(player)
    play_poit = []
    play_poit.append(max_loc[0]+9)
    play_poit.append(max_loc[1]-120+43)

    #在图中标出得到的点 便于修改
    p = cv2.circle(img, (play_poit[0],play_poit[1]+120), 3, (0, 0, 255), -1)
    cv2.imwrite("3.png",img)
    print(play_poit)
    return play_poit

#得到目的点
def get_location(play_poit):
    img = cv2.imread("jump.png")
    img = cv2.resize(img,(0,0),fx=0.25,fy=0.25)
    #play_poit = get_play_point()
    height,width,a = img.shape
    img_blur = cv2.GaussianBlur(img, (5, 5), 0)
    canny_img = cv2.Canny(img_blur, 1, 10)    
    canny_img = canny_img[120:int(height/2-15)]

#去除人物头部部分 避免造成影响
    for y in range(0,135):
        for x in range(play_poit[0],play_poit[0]+40):
            canny_img[y][x]=155

#通过遍历得到目的点
    max_x = 0
    center_x = 0
    center_y = 0
    crop_h,crop_w = canny_img.shape
    for y in range(crop_h):
        for x in range(crop_w):
            if canny_img[y][x]==255:
                if center_x==0:
                    center_x = x
                if x>max_x+5:
                    max_x =x
                    center_y = y
#标记得到的点
    c =  cv2.circle(canny_img, ((center_x,center_y)), 5, (255, 255, 255), -1)
    cv2.imwrite("2.png",c)
    location = []
    location.append(center_x)
    location.append(center_y)
    print(location)
    return location

def get_distance(play_poit,location):
    distance = numpy.sqrt(pow(play_poit[0]-location[0],2)+pow(play_poit[1]-location[1],2))
    print(distance)
    return distance

def press(distance):
    press_time = int(distance*5.6)
    #设置随机按压点
    x = str(random.uniform(200.1,400.1))
    y = str(random.uniform(200.1,800.1))

    os.system("adb shell input swipe "+x+" " + y +" " + x + " "  +y + " "+str(press_time))

while True:
    get_img()
    play_point = get_play_point()
    location = get_location(play_point)
    distance = get_distance(play_point,location)
    press(distance)
    time.sleep(random.uniform(2.1,3.1))

