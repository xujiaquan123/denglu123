import requests
import hashlib
import time

import config
#from common.log_handler import logger
from denglu.damapingtai import base64_api


def get_token(imageName, imagePath, imageId, account, pwd):


    pwd = hashlib.md5(pwd.encode(encoding='utf-8')).hexdigest()

    while True:

       imageCode = get_image_code(imageName, imagePath, imageId)
      # """登录平台，获取token"""
       url = 'http://172.16.3.96:9000/#/singlelogin'
       request_data = {"account": account, "pwd": pwd, "imageCode": imageCode, "imageId": imageId}


       response_data = requests.post(url=url, json=request_data).json()
       if response_data["resultCode"] == 200:
           token = response_data["data"]["token"]
           break
    print(token)




imageId = int(time.time())


def get_image_code(imagePath, imageId, imageWidth=72, imageHeight=32):
        """
        获取图片验证码
        :param imageName:
        :param imagePath:
        :param imageId:
        :param imageWidth:
        :param imageHeight:
        :return:
        """
        url = config.get_base_url() + 'facepay/face-payment-user/user/login/getImageCode/{0}/{1}/{2}'.format(imageWidth,
                                                                                                             imageHeight,
                                                                                                             imageId)
        res = requests.get(url=url)

        """将获取的图片验证码保存至本地"""
        with open('D:/a/response.jpg','wb') as f:
            f.write(res.content)

img_path='D:/a/response.jpg'
imageCode = base64_api(uname='13851458541', pwd='15050577213', img=img_path, typeid=3)



