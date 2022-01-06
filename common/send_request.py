#coding=utf-8
import requests
import json
from common import get_values
from common.logger import MyLogging
log = MyLogging().logger

import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)


class RunMethod:
    # post请求
    def do_post(self, url, data, headers=None):
        res = None
        if headers != None:
            res = requests.post(url=url, data=data, headers=headers)
        else:
            res = requests.post(url=url, data=data)
        # return res.json()
        return res

    # get请求
    def do_get(self, url, data=None, headers=None):
        res = None
        if headers != None:
            res = requests.get(url=url, data=data, headers=headers)
        else:
            res = requests.get(url=url, data=data)
        # return res.json()
        return res

    #先post再根据返回的子链接进行get请求
    def do_postAndget(self, url, data=None, headers=None):
        res = None
        if headers != None:
            res = requests.post(url=url, data=data, headers=headers)
            log.info("111"+res.text)
            # 提取出返回的url
            response = res.text
            #json.loads将str转换为dict
            if 'newResourceLocation' in response:
                url = get_values.getvales.getdict(json.loads(response), 'newResourceLocation')
            else:
                pass
            res = requests.get(url=url, data=None)
            print(res.text)
        else:
            res = requests.post(url=url, data=data)
            log.info("111" + res.text)
            # 提取出返回的url
            response = res.text
            log.info(type(response))
            if 'newResourceLocation' in response:
                url = get_values.getvales.getdict(json.loads(response), 'newResourceLocation')
            res = requests.get(url=url, data=None)
            print(res.text)
        return res

    def run_method(self, method, url, data=None, headers=None):
        res = None
        if method == "POST" or method == "post":
            # res = self.do_post(url, data.encode(), headers)
            res = self.do_post(url, data, headers)
        elif method == "postAndget":
            res=self.do_postAndget(url, data, headers)
        else:
            res = self.do_get(url, data, headers)
        return res
