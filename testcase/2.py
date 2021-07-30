import  requests
from testcase.bianliang1 import cf
import random
from testcase.bianliang1 import headers
from log.logs import Log
import time

from testcase.jiekou import RequestHandler

log = Log(__name__, 'C:/Users/许加权/Desktop/新建文件夹 (5)/face-payment/denglu/files.log')



class TestMgmt():

    def setup_class(self):
        self.g = globals()
        # self.logger = log.Logger()

    def teardown_class(self):
        pass

    def testbutie(self):  # 新建补贴规则成功
        self.logger = log.Logger
        base_url = cf.get("db", "base_url2") + "perquisite/createPerquisite"
        i = ''.join(random.sample("123456", 5))
        self.g["w"]=i
        data = {"name": i, "rule": "1", "limitAmount": "4", "amount": "4", "limit": "",
                "time": ["2021-07-28T07:07:55.000Z", "2021-07-28T08:07:55.000Z"],
                "startTime": "15:07", "endTime": "16:07"}
        r = RequestHandler.post(self, url=base_url, headers=headers, json=data).json()
        self.logger.info(r)
        assert r["resultMessage"] == "成功"

    def testbutiemingchen(self):  # 新建补贴规则名称重复
        self.logger = log.Logger
        base_url = cf.get("db", "base_url2") + "perquisite/createPerquisite"

        data = {"name": self.g["w"], "rule": "1", "limitAmount": "4", "amount": "4", "limit": "",
                "time": ["2021-07-28T07:07:55.000Z", "2021-07-28T08:07:55.000Z"],
                "startTime": "15:07", "endTime": "16:07"}
        r = RequestHandler.post(self, url=base_url, headers=headers, json=data).json()
        self.logger.info(r)
        assert r["resultMessage"] == "名称已存在"