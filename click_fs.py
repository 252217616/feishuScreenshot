import datetime
import time
from PIL import ImageGrab
from datetime import timedelta

import pyautogui

#年
year = 2021
# mouths = ["04", "03","02","01"]
#月
mouths = ["12","11","10","09","08","07","06","05","04","03","02","01"]
#日历首点坐标 坐标获取请运行 click_test.py
first = (1596,300)
#截图区域左上角坐标
screenshot1 = (1567,78)
#截图区域右下角坐标
screenshot2 = (1917,1034)
#滑动起点坐标
slideStart = (1632, 346)
#滑动终点坐标
slideEnd = (1828, 351)
#保存文件夹
path = "C:/Users/Admin/Desktop/zc/"

# 组装日历网格 50 35 7X4
date = [
    [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
    [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]]

for x in range(7):
    col = date[x]
    for y in range(7):
        col[y] = (first[0]+(y*50),first[1]+(x*35))
index = 1
for i in range(len(mouths)):
    mouth = mouths[i]
    # 计算该月第一天是星期几
    datetime_date = datetime.date(year, int(mouth), 1)
    weekday = datetime_date.weekday()+1
    for x in range(7):
        for y in range(7):
            if(x == 0):
                y = weekday % 7 + y
                if(y >= 7):
                    continue
            pos = date[x][y]
            #点击
            pyautogui.click(x=pos[0], y=pos[1], clicks=1, button='left')
            time.sleep(1)
            #截图
            day = ""
            if (index > 9):
                day = str(index)
            else:
                day = "0" + str(index)
            savePath = path+str(year) + mouth + day + '.png'
            #截图区域
            im = ImageGrab.grab(bbox=(screenshot1[0], screenshot1[1], screenshot2[0], screenshot2[1]))
            im.save(savePath)
            datetime_date = datetime_date + timedelta(days=1)
            index += 1
            if(datetime_date.month != int(mouth) ):
                break
        if (datetime_date.month != int(mouth)):
            break
    #翻页
    index = 1
    pyautogui.moveTo(slideStart[0], slideStart[1])
    pyautogui.dragTo(slideEnd[0], slideEnd[1], 0.5, button='left')
    time.sleep(3)

