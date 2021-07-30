import configparser

cf = configparser.ConfigParser()
filename = cf.read(r"C:\Users\许加权\Desktop\新建文件夹 (5)\face-payment\denglu\config\config.ini",encoding="utf-8")
sec = cf.get("db","base_url")
print(sec)
