#腾讯云函数版本，直接复制导入即可

import requests
import time
from sys import argv
import os
import sys
import json
import logging
import datetime
logger = logging.getLogger()
logger.setLevel(logging.INFO)
class Req:
    headers = {
        'Accept': '*/*',
        "Host": "student.wozaixiaoyuan.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip,br,deflate",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "Referer": 'https://servicewechat.com/wxce6d08f781975d91/173/page-frame.html',
        "token": "680893a0-020e-461f-952c-c8e408fa599b",  # token
        "JWSESSION": "a99bd3b4a4614e2696725fdf3949ec8e",#session,
        # "Content-Length": "744"
    }

    # 处理打卡结果
    @staticmethod
    def handle_res(res):
        if res and res['code'] == 0:
            logging.info("自动打卡签到结果 : code = {}".format(res['code']))
            Remind().success(" 已经自动为您打卡成功啦~ ")
        elif res and res['code'] == -10:
            logging.error("打卡失败,TOKEN已过期,时间:{}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            Remind().fail(" <b>由于TOKEN过期失效,打卡失败了哦,请及时处理~ </b>")
        else:
            logging.error("打卡失败,时间:{}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            Remind().fail("<b>非常遗憾的通知您,打卡失败了哦,请及时处理~ </b>")


class Inspect(Req):
    saveUrl = "https://student.wozaixiaoyuan.com/health/save.json"
    data = {
        "token_p":"",
        "answers": '["0"]',
        "latitude": "经度",
        "longitude": "纬度",
       "country": "",
        "city": "市",
        "district": "",
        "province": "省",
        "township": "",
        "street": " ",
        "myArea": "",
    }

    # 提交打卡请求
    def submit_insp(self):
        res = requests.post(self.saveUrl, headers=self.headers, data=self.data).json()
        self.handle_res(res)
        print(res)
class Remind:
    data = {
        "token_p":'05203a15adb24362a0feec197a52c777',
        "title": '我在校园自助签到',
        "content": ''
    }
    def __init__(self):
        self.data['content']='<h1>签到提醒</h1><body>'

    def send_msg(self):
        self.data["content"]+='</body>'
        #result=send(self.data['content'],self.data['token_p'],self.data['title'])
        result=requests.get('http://www.pushplus.plus/send?token='+self.data['token_p']+'&title='+self.data['title']+'&content='+self.data['content'])
        if result != None:
            logging.info("推送消息成功")
        else:
            logging.info("推送消息失败了")

    def success(self, desp):
        self.data['content'] += desp
        self.send_msg()

    def fail(self, desp):
        self.data['content'] += desp
        self.send_msg()
def main():
    Inspect().submit_insp()
    return True   
if __name__ == "__main__":
    main()
def main_handler(event, context):
    logger.info('got event{}'.format(event))
    return main()
