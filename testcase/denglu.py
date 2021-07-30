import time
import uuid

from damapingtai import base64_api
import requests
import random

# t= int(round(time.time()*1000))
# print(t)
uid = str(uuid.uuid1())
print(uid)


# url ='http://172.16.3.96:9000/facepay/face-payment-user/user/login/getImageCode/72/32/Id'
# res = requests.get(url=url)
# with open('D:/a/response.jpg', 'wb') as f:
#          f.write(res.content)
# img_path = 'D:/a/response.jpg'
# imageCode = base64_api(uname='13851458541', pwd='15050577213', img=img_path, typeid=3)
# print(imageCode)
#
#
# url = "http://172.16.3.96:9000/facepay/face-payment-user/user/adminLogin"
# data ={"account": "zhangsan123",
# "imageCode": imageCode,
# "imageId":"",
# "pwd": "d2440013815d575150d27d77773c7a17"}
# r =requests.post(url=url,json=data)
# print(r.text)
# print(imageCode)
#

