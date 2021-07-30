def pic_down():
    import requests
    r = requests.get("http://172.16.3.96:9000/facepay/face-payment-user/user/login/getImageCode/72/32/1621237493577")
    with open("D:\Python\yyy\image3.png","wb")as f:
        f.write(r.content)
pic_down()



# noinspection PyUnresolvedReferences

import requests
import time
from selenium import webdriver

# noinspection PyUnresolvedReferences
from pymouse import PyMouse
# noinspection PyUnresolvedReferences
from hashlib import md5
# noinspection PyUnresolvedReferences
import re
# noinspection PyUnresolvedReferences
from PIL import Image   # 鐢ㄤ簬鎵撳紑鍥剧墖鍜屽鍥剧墖澶勭悊
from denglu.damapingtai import base64_api



driver = webdriver.Chrome()
driver.get("http://172.16.3.96:9000/#/singlelogin")
driver.maximize_window()
time.sleep(2)
#
image = driver.find_element_by_xpath('//*[@id="singlelogin"]/div/div[2]/form/div[4]/div/div/span[2]/span/img')
image = image.screenshot("yzm.png")
#
img_path = "yzm.png"
code_result = base64_api(uname='13851458541', pwd='15050577213', img=img_path, typeid=3)

def fangfa(self,dizhi,nerong):
    self.mima = driver.find_element_by_xpath(dizhi).send_keys(nerong)
    dizhi = '//*[@id="singlelogin"]/div/div[2]/form/div[3]/div/div/input'
    nerong = "Xu@15050577213"

zhanghao = driver.find_element_by_class_name("el-input__inner").send_keys("zhangsan123")
mima = driver.find_element_by_xpath('//*[@id="singlelogin"]/div/div[2]/form/div[3]/div/div/input').send_keys("Xu@15050577213")

shuruyzm =driver.find_element_by_xpath('//*[@id="singlelogin"]/div/div[2]/form/div[4]/div/div/input').send_keys(code_result)
denglv = driver.find_element_by_xpath('//*[@id="singlelogin"]/div/div[2]/form/div[5]/div/button').click()
