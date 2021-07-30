import requests
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

    def test_chaxun(self):  # 查询接口
        base_url = cf.get("db", "base_url")+"query/deviceOrder"

        data = {"companyId": "757",
                "endTime": "2021-06-04",
                "pageNum": "1",
                "pageSize": "10",
                "startTime": "2021-06-04"}
        r = requests.post(url=base_url, headers=headers, json=data).json()

        assert r['resultCode'] == 200


    def test_gschaxun(self):  # 公司查询
        base_url = cf.get("db", "base_url")+"query/deviceOrder"
        data = {"companyId": "755",
                "endTime": "2021-06-10",
                "pageNum": "1",
                "pageSize": "10",
                "startTime": "2021-06-10"}
        r = requests.post(url=base_url, headers=headers, json=data)
        r = r.json()
        print(r)
        assert r["data"][0]["companyName"] == "有限公司"

    def test_shebeichaxun(self):  # 设备号查询
        base_url = cf.get("db", "base_url") + "query/deviceOrder"
        data = {"deviceIds": [545],
                "companyId": "",
                "pageNum": "1",
                "pageSize": "10",
                "sn": ""
                }
        r = requests.post(url=base_url, headers=headers, json=data)
        r = r.json()
        print(r)

        assert r["data"][0]["deviceName"] == "张三"

    def test_merchantIdtime(self):  # 修改就餐时间成功
        base_url = cf.get("db", "base_url") + "query/deviceOrder"
        data = {"breakfastEnd": "08:02",
                "breakfastStart": "07:00",
                "dinnerEnd": "20:00",
                "dinnerStart": "15:00",
                "id": "545",
                "lunchEnd": "14:00",
                "lunchStart": "10:30",
                "model": "HeShi-M1 Pro",
                "name": "张三",
                "version": "1.0.7"}
        r = requests.post(url=base_url, headers=headers, json=data)
        r = r.json()
        print(r)
        assert r["resultCode"] == 200

    def test_merchantIdtimerepeat(self):  # 就餐时间重叠
        base_url = cf.get("db", "base_url") + "updateDevice"
        data = {"breakfastEnd": "08:02",
                "breakfastStart": "07:00",
                "dinnerEnd": "20:00",
                "dinnerStart": "15:00",
                "id": "545",
                "lunchEnd": "15:00",
                "lunchStart": "10:30",
                "model": "HeShi-M1 Pro",
                "name": "许家权",
                "version": "1.0.7"}
        r = requests.post(url=base_url, headers=headers, json=data)
        r = r.json()
        print(r)
        assert r["resultMessage"] == "就餐时间段设置重叠，请重新设置"

    def test_merchantIdparameter(self):  # 缺少设备名称参数
        base_url = cf.get("db", "base_url") + "query/deviceOrder"
        data = {"breakfastEnd": "08:02",
                "breakfastStart": "07:00",
                "dinnerEnd": "20:00",
                "dinnerStart": "15:00",
                "id": "545",
                "lunchEnd": "15:00",
                "lunchStart": "10:30",
                "model": "HeShi-M1 Pro",
                # "name": "",
                "version": "1.0.7"}
        r = requests.post(url=base_url, headers=headers, data=data)
        r = r.json()
        print(r)
        assert r["resultCode"] == 10003

    def test_merchantIdparameter(self):  # 编辑设备名称重复
        base_url = cf.get("db", "base_url") + "query/deviceOrder"
        data = {"breakfastEnd": "08:02",
                "breakfastStart": "07:00",
                "dinnerEnd": "20:00",
                "dinnerStart": "15:30",
                "id": "545",
                "lunchEnd": "15:00",
                "lunchStart": "10:30",
                "model": "HeShi-M1 Pro",
                "name": "许家权",
                "version": "1.0.7"}
        r = requests.post(url=base_url, headers=headers, data=data)
        r = r.json()
        print(r)
        assert r["resultCode"] == 10012

    def test_merchantIdparameter(self):  # 设备消费按时间段统计
        base_url = cf.get("db", "base_url") + "query/deviceOrder"
        data = {"companyId": "",
                "deviceIds": [],
                "pageNum": "1",
                "pageSize": "10",
                "endTime": "2021-05-26",
                "startTime": "2021-05-26",
                "sn": ""}
        r = requests.post(url=base_url, headers=headers, json=data)
        r = r.json()
        print(r)
        assert r["resultCode"] == 200

    def test_accountcreate(self):  # 创建账号成功
        self.logger = log.Logger
        str_start = random.choice(['135', '136', '138'])
        str_end = ''.join(random.sample('0123456789', 8))
        str_phone = str_start + str_end
        self.g["m"] = str_phone
        base_url = cf.get("db", "base_url1") + "createAccount"
        data = {"name": "展rgrgb", "phone": str_phone, "sex": "1"}
        file = {"file": ("u.jpg", open('D:/a/u.jpg', "rb"), "image/jpeg")}
        r = requests.post(url=base_url, headers=headers, files=file, data=data).json()
        self.g["b"] = r

        assert r['resultMessage'] == "成功"
        self.logger.info("{}".format(r))


    def test_accountexist(self):#创建账号手机号重复
        self.logger = log.Logger
        base_url = cf.get("db", "base_url1") + "createAccount"
        data = {"name": "展rgrgb", "phone": self.g["m"], "sex": "1"}
        file = {"file": ("u.jpg", open('D:/a/u.jpg', "rb"), "image/jpeg")}
        r = requests.post(url=base_url, headers=headers, files=file, data=data).json()
        self.logger.info(r)
        assert r["resultMessage"] =="手机号已经存在"

    def test_updateaccount(self):#编辑账号
        self.logger = log.Logger
        base_url = cf.get("db", "base_url1") + "updateAccount"
        data ={"name": 212300,
               "phone": self.g["m"],
               "sex": 0,
               "id": self.g["b"]["data"],
               "merchantId": 158}
        file = {"file": ("u.jpg", open('D:/a/u.jpg', "rb"), "image/jpeg")}
        r = requests.post(url=base_url, headers=headers, files=file, data=data).json()
        self.logger.info(r)
        assert r["resultMessage"] == "成功"

    # def test_deleteaccount(self):#删除账号
    #     self.logger = log.Logger
    #     base_url = cf.get("db", "base_url1") + "deleteAccount"
    #     for i in range(50111,55112):
    #         if i < 55112:
    #             data = {"id": i, "merchantId": 158}
    #             r = requests.get(url=base_url, headers=headers, params=data).json()
    #             self.logger.info(r)
    #         else:
    #            print(r.text)
    #            self.logger.info(r)

    def test_deletecard(self):#批量删除卡片
        self.logger = log.Logger
        base_url = cf.get("db", "base_url2") + "card/deleteCard"
        for i in range(52207, 94395):
            if i < 94395:
                    data = {"id": i, "merchantId": 158}
                    r = requests.get(url=base_url, headers=headers, params=data).json()
                    self.logger.info(r)
                    break
            else:
                print(i)


    def test_upcard(self):#修改卡片金额为0
        self.logger = log.Logger
        base_url = cf.get("db", "base_url2") + "card/updateCard"
        data ={"accountId": self.g["b"]["data"],
                "cardId": self.g["m"],
                "companyId": 2267,
                "deposit": 0,
                "employeeNumber":"",
                "faceFlag": "0",
                "id":94225,
                "invalidTime":"",
                "merchantId": 158,
                "name":"汤纪阔1",
                "orgId": 2296}
        r = requests.post(url=base_url, headers=headers, json=data).json()
        self.logger.info(r)

    def test_changmoney(self):#金额变更操作公司查询
        self.logger = log.Logger
        base_url = cf.get("db","base_url2")+"amount/queryAmountManage"
        data ={"companyId": 755,
               "orgId":"",
                "name":"",
                "cardId":"",
                "accountNum": "",
                "startDate": "",
                "endDate": "",
                "pageNum": 1,
                "pageSize": 10
             }
        r = requests.get(url=base_url,headers=headers,params=data).json()

        assert r["resultMessage"] == "成功"
        print(r)

    def test_department(self):#金额变更操作部门查询
        self.logger = log.Logger
        base_url = cf.get("db","base_url2")+"amount/queryAmountManage"
        data ={"companyId": "",
               "orgId":"1017",
                "name":"",
                "cardId":"",
                "accountNum": "",
                "startDate": "",
                "endDate": "",
                "pageNum": 1,
                "pageSize": 10
             }
        r = requests.get(url=base_url,headers=headers,params=data).json()
        print(r)
        assert r["resultMessage"] == "成功"

    def test_queryname(self):#金额变更操作姓名查询
        self.logger = log.Logger
        base_url = cf.get("db","base_url2")+"amount/queryAmountManage"
        data ={"companyId": "",
               "orgId":"",
                "name":"许家权",
                "cardId":"",
                "accountNum": "",
                "startDate": "",
                "endDate": "",
                "pageNum": 1,
                "pageSize": 10
             }
        r = requests.get(url=base_url,headers=headers,params=data).json()
        print(r)
        assert r["resultMessage"] == "成功"

    def test_daochu(self):#导出
        self.logger = log.Logger
        base_url = cf.get("db","base_url2")+"amount/queryAmountManage/export"
        data ={"companyId": "",
               "orgId":"",
                "name":"",
                "cardId":"",
                "accountNum": "",
                "startDate": "",
                "endDate": "",}
        r = requests.get(url=base_url, headers=headers, params=data)
        with open('C:/Users/许加权/Desktop/新建文件夹 (5)/face-payment/denglu/response.csv','wb') as f:
         f.write(r.content)

    def test_hongbaochongzhi(self):#红包充值
        self.logger = log.Logger
        base_url = cf.get("db","base_url2")+"redPacket/add"
        data ={"cardId":"57847","money":4,"invalidTime":"2021-07-20"}
        r = requests.post(url=base_url, headers=headers, json=data).json()
        self.logger.info(r)
        assert r["resultMessage"] == "成功"

    def test_chongzhi(self):#充值
        self.logger = log.Logger
        base_url = cf.get("db","base_url2")+"amount/deposit"
        data ={"ids":[57847],"money":"11"}
        r = requests.post(url=base_url, headers=headers, json=data).json()
        self.logger.info(r)
        assert r["resultMessage"] == "成功"


    def test_koukuan(self):#扣款
        self.logger = log.Logger
        base_url = cf.get("db","base_url2")+"amount/deduction"
        data ={"ids":[57847],"money":"3"}
        r = requests.post(url=base_url, headers=headers, json=data).json()
        self.logger.info(r)
        assert r["resultMessage"] == "成功"


    def test_koukuan1(self):#扣款大于余额
        self.logger = log.Logger
        base_url = cf.get("db","base_url2")+"amount/deduction"
        data ={"ids":[57847],"money":"100000"}
        r = requests.post(url=base_url, headers=headers, json=data).json()
        self.logger.info(r)
        assert r["resultMessage"] == "余额不足"


    def test_tuikuan(self):#退款
        self.logger = log.Logger
        base_url =cf.get("db","base_url2")+"amount/refund"
        data ={"ids":[57847],"money":"0"}
        r = requests.post(url=base_url, headers=headers, json=data).json()
        self.logger.info(r)
        assert r["resultMessage"] == "成功"

    def test_yuebiangen(self):#余额变更记录公司查询

        base_url = cf.get("db", "base_url2") + "amount/queryRecord"
        data ={"companyId": 755,
                "orgId":"" ,
                "name":"",
                "cardId":"",
                "accountNum":"",
                "changeMethod":"",
                "startDate":"2021-07-26",
                "endDate":"2021-07-26",
                "tradeState":"",
                "pageNum": 1,
                "pageSize": 10}
        r = requests.get(url=base_url, headers=headers, params=data).json()
        self.logger.info(r)
        assert r["resultMessage"] == "成功"



    def test_xiaofeiguizi(self):#创建消费规则成功
        self.logger = log.Logger
        str_1 = ''.join(random.sample('0123456789', 3))
        self.g["s"]=str_1
        base_url =cf.get("db","base_url2")+"perquisite/createPerquisite"
        data ={"name":str_1,"rule":"1","limitAmount":"10","amount":"5",
               "limit":"","time":["2021-07-20T07:08:57.000Z",
               "2021-07-20T08:08:57.000Z"],"startTime":"15:08","endTime":"16:08"}
        r = requests.post(url=base_url, headers=headers, json=data).json()

        self.logger.info(r)
        assert r["resultMessage"] == "成功"


    def test_xiaofeiguizichongfu(self):#创建消费规则名称重复
        self.logger = log.Logger
        base_url =cf.get("db","base_url2")+"perquisite/createPerquisite"
        data ={"name":"perquisiteRuleName60","rule":"1","limitAmount":"10","amount":"5",
               "limit":"","time":["2021-07-20T07:08:57.000Z",
               "2021-07-20T08:08:57.000Z"],"startTime":"15:08","endTime":"16:08"}
        r = requests.post(url=base_url, headers=headers, json=data).json()
        self.logger.info(r)
        assert r["resultMessage"] == "名称已存在"


    def test_xiaofeiguizibianji(self):#消费规则编辑成功
        self.logger = log.Logger
        base_url = cf.get("db", "base_url2") +"perquisite/updatePerquisite"
        data ={"id":320,"name":"m","rule":"1","limitAmount":10,"amount":5,
               "merchantId":158,"deleteState":"A","updateTime":"2021-07-20T07:17:25.976+0000",
               "createTime":"2021-07-20T07:17:25.976+0000","startTime":"15:08","endTime":"16:08",
               "isModify":"1","time":["2021-07-20T07:08:00.000Z","2021-07-20T08:08:00.000Z"]}
        r = requests.post(url=base_url, headers=headers, json=data).json()
        self.logger.info(r)
        assert r["resultMessage"] == "成功"


    def test_xiaofeiguizibianjicunzai(self):#消费规则编辑名称存在
        self.logger = log.Logger
        base_url = cf.get("db", "base_url2") +"perquisite/updatePerquisite"
        data ={"id":675,"name":"m","rule":"1","limitAmount":10,"amount":5,
               "merchantId":158,"deleteState":"A","updateTime":"2021-07-20T07:17:25.976+0000",
               "createTime":"2021-07-20T07:17:25.976+0000","startTime":"15:08","endTime":"16:08",
               "isModify":"1","time":["2021-07-20T07:08:00.000Z","2021-07-20T08:08:00.000Z"]}
        r = requests.post(url=base_url, headers=headers, json=data).json()
        self.logger.info(r)
        assert r["resultMessage"] == "名称已存在"



    def test_shanchuxiaofeiguizi(self):  # 删除消费规则不存在
        base_url = cf.get("db", "base_url2") +"/perquisite/deletePerquisite"
        data ={"id":684}
        r = requests.post(url=base_url, headers=headers, json=data).json()
        print(r)
        assert r["resultMessage"] == "Perquisite is not exist"


    def test_gongsi(self):#微信付款码公司查询
        self.logger=log.Logger
        base_url =cf.get("db","base_url2")+"paymentCode/pay/orderList"
        data ={"companyId":"","deviceSn":"","outTradeNo":"","tradeState":"",
                "startDate":"","endDate":"","pageNum":1,"pageSize":10}
        r = RequestHandler.post(self,url=base_url,headers=headers,json=data).json()
        self.logger.info(r)
        #r = requests.post(url=base_url,headers=headers,json=data).json()
        assert r["resultMessage"] =="成功"

    def test_shebei(self):  # 微信付款码设备查询
        self.logger = log.Logger
        base_url = cf.get("db", "base_url2") + "paymentCode/pay/orderList"
        data ={"companyId":"","deviceSn":"2904A46800600276","outTradeNo":"null",
                "tradeState":"null","startDate":"null","endDate":"null","pageNum":1,"pageSize":10}
        r = RequestHandler.post(self, url=base_url, headers=headers, json=data).json()
        self.logger.info(r)
        assert r["resultMessage"] =="成功"



    def test_dingdanzhuangtai(self):  # 微信付款码支付状态查询
        self.logger = log.Logger
        base_url = cf.get("db", "base_url2") + "paymentCode/pay/orderList"
        data={"companyId":"","deviceSn":"","outTradeNo":"null","tradeState":"SUCCESS",
              "startDate":"","endDate":"null","pageNum":1,"pageSize":10}
        r = RequestHandler.post(self, url=base_url, headers=headers, json=data).json()
        self.logger.info(r)
        assert r["resultMessage"] == "成功"

    def test_shijianchaxun(self):  # 微信付款码付款时间查询
        self.logger = log.Logger
        base_url = cf.get("db", "base_url2") + "paymentCode/pay/orderList"
        data = {"companyId":"","deviceSn":"","outTradeNo":"","tradeState":"",
                "startDate":"2021-07-26 00:00:00","endDate":"2021-07-26 23:59:59","pageNum":1,"pageSize":10}
        r = RequestHandler.post(self, url=base_url, headers=headers, json=data).json()
        self.logger.info(r)
        assert r["resultMessage"] == "成功"



    def test_weixinfukuandaochu(self):  # 微信付款码记录导出
        self.logger = log.Logger
        base_url = cf.get("db", "base_url2") + "paymentCode/pay/exportOrderList"
        data = {"companyId":"","deviceSn":"","outTradeNo":"null","tradeState":"",
                "startDate":"2021-07-26 00:00:00","endDate":"2021-07-26 23:59:59"}
        r = requests.post(url=base_url, headers=headers, json=data)
        with open('C:/Users/许加权/Desktop/新建文件夹 (5)/face-payment/denglu/weixin.csv','wb') as f:
            f.write(r.content)


    def testbutie(self):#新建补贴规则成功
        self.logger=log.Logger
        base_url =cf.get("db","base_url2")+"perquisite/createPerquisite"
        i =''.join(random.sample("123456",5))
        self.g["w"] = i
        data ={"name":i,"rule":"1","limitAmount":"4","amount":"4","limit":"",
               "time":["2021-07-28T07:07:55.000Z","2021-07-28T08:07:55.000Z"],
               "startTime":"15:07","endTime":"16:07"}
        r =RequestHandler.post(self, url=base_url, headers=headers, json=data).json()
        self.logger.info(r)
        assert r["resultMessage"] == "成功"

    def testbutiemingchen(self):#新建补贴规则名称重复
        self.logger=log.Logger
        base_url =cf.get("db","base_url2")+"perquisite/createPerquisite"
        data ={"name":self.g["w"],"rule":"1","limitAmount":"4","amount":"4","limit":"",
               "time":["2021-07-28T07:07:55.000Z","2021-07-28T08:07:55.000Z"],
               "startTime":"15:07","endTime":"16:07"}
        r =RequestHandler.post(self, url=base_url, headers=headers, json=data).json()
        self.logger.info(r)
        assert r["resultMessage"] == "名称已存在"


    def test_butiebiji(self):#补贴规则编辑
        self.logger = log.Logger
        base_url= cf.get("db","base_url2")+"perquisite/queryPerquisite"
        base_url2 = cf.get("db", "base_url2")+"perquisite/updatePerquisite"
        data1 ={ "name":"",
                "pageNum": 1,
                "pageSize": 10}
        r = RequestHandler.get(self, url=base_url, headers=headers, params=data1).json()
        u = r["data"][0]["id"]
        m =''.join(random.sample('1234567',5))
        data2 = {"id":u, "name": m, "rule": "1", "limitAmount": 4, "amount": 4,
                 "merchantId": 158, "deleteState": "A", "updateTime": "2021-07-28T07:36:39.556+0000",
                 "createTime": "2021-07-28T07:36:39.556+0000", "startTime": "15:07", "endTime": "16:07",
                 "isModify": "1",
                 "time": ["2021-07-28T07:07:00.000Z", "2021-07-28T08:07:00.000Z"]}
        r = RequestHandler.post(self, url=base_url2, headers=headers, json=data2).json()
        self.logger.info(r)
        assert r["resultMessage"] =="成功"


    def test_butieguizechongfu(self):#编辑补贴规则名称存在
        self.logger=log.Logger
        base_url = cf.get("db", "base_url2") + "perquisite/queryPerquisite"
        base_url2 = cf.get("db", "base_url2") + "perquisite/updatePerquisite"
        data1 = {"name": "",
                 "pageNum": 1,
                 "pageSize": 10}
        r = RequestHandler.get(self, url=base_url, headers=headers, params=data1).json()
        u = r["data"][0]["id"]
        print(u)
        data2 = {"id": u, "name":'eeeee', "rule": "1", "limitAmount": 4, "amount": 4,
                 "merchantId": 158, "deleteState": "A", "updateTime": "2021-07-28T07:36:39.556+0000",
                 "createTime": "2021-07-28T07:36:39.556+0000", "startTime": "15:07", "endTime": "16:07",
                 "isModify": "1",
                 "time": ["2021-07-28T07:07:00.000Z", "2021-07-28T08:07:00.000Z"]}
        r = RequestHandler.post(self, url=base_url2, headers=headers, json=data2).json()
        self.logger.info(r)
        assert r["resultMessage"] == "名称已存在"