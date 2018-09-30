# -- coding: UTF-8 --
from PIL import Image
from PIL import ImageGrab
import pytesseract
import win32gui, win32ui, win32con, win32api
import time


class mhMissionState(object):

    def __init__(self):
        self.stateStr = 6
        #判断当前的状态
        self.STATE_TEACH = 0
        self.STATE_DEON = 1
        self.STATE_MAP = 2
        self.STATE_MOVE = 3        
        
        #截图保存当前任务
        size = (600,148,750,192)
        pic = ImageGrab.grab(size)
        pic.save('mission.jpg')
        time.sleep(1)
        #识别文字
        text = pytesseract.image_to_string(Image.open('mission.JPG'),lang='chi_sim')
        print('图片文字:\n')
        print(text)
        
        text = 0
    
        if text == 0:
            self.stateStr = 0
        if text == 1:
            self.stateStr = 1
        if text == 2:
            self.stateStr = 2
        if text == 3:
            self.stateStr = 3                
        
        
        
    
             

            
        
           