# coding=utf-8
import requests
import json


import requests
import self as self


class RequestHandler():
    def get(self, url, **kwargs):
        """封装get方法"""
        # 获取请求参数
        params = kwargs.get("params")
        headers = kwargs.get("headers")
        try:
            result = requests.get(url, params=params, headers=headers)
            return result
        except Exception as e:
            print("get请求错误: %s" % e)
    def post(self, url, **kwargs):
        """封装post方法"""
        # 获取请求参数
        params = kwargs.get("params")
        data = kwargs.get("data")
        json = kwargs.get("json")
        headers =kwargs.get("headers")
        try:
            result = requests.post(url, params=params, data=data, json=json,headers=headers)
            return result
        except Exception as e:
            print("post请求错误: %s" % e)
    def run_main(self, method, **kwargs):
        """
        判断请求类型
        :param method: 请求接口类型
        :param kwargs: 选填参数
        :return: 接口返回内容
        """
        if method == 'get':
            result = self.get(**kwargs)
            return result
        elif method == 'post':
            result = self.post(**kwargs)
            return result
        else:
            print('请求接口类型错误')

if __name__ == '__main__':

    headers = {"token": "30b79786-1ba5-436e-aa56-d6ed975096fa"}

    url = "http://172.16.3.96:9000/facepay/face-payment-mgmt/device/query/deviceOrder"
    data = {"companyId": "757",
                "endTime": "2021-06-04",
                "pageNum": "1",
                "pageSize": "10",
                "startTime": "2021-06-04"}
    res = RequestHandler().run_main(method="post",url=url,json=data,headers=headers)
    print(res.json())

