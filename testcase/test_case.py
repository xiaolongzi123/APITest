#coding=utf-8
import os
import time
import sys

current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)
from common.operate_excel import *
import unittest
from parameterized import parameterized
from common.send_request import RunMethod
import json
from common.logger import MyLogging
import jsonpath
from common.is_instance import IsInstance
from HTMLTestRunner import HTMLTestRunner

lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data"))
file_path = lib_path + "/" + "接口自动化测试.xlsx"  # excel的地址
sheet_name = "测试用例"
host_sheet_name="host"
log = MyLogging().logger
host=ExcelData(file_path,host_sheet_name).readHost()#读取host地址


def getExcelData():
    list = ExcelData(file_path, sheet_name).readExcel()
    return list


class MyTestCase(unittest.TestCase):
    @parameterized.expand(getExcelData())
    def test_api(self, rowNumber, caseRowNumber, testCaseName, priority, parentsPath, url, method, parmsType, data,checkCode,
                 checkPoint, isRun,  executeResult):
        url=host+parentsPath+url
        if isRun == "Y" or isRun == "y":
            log.info("【开始执行测试用例：{}】".format(testCaseName))
            headers = {"Content-Type": "application/json"}
            if(parmsType=='json'):
                data = json.loads(data)  # 将字符串传化为字典格式
                data=json.dumps(data) #再转换为json格式
            elif(parmsType=='None' or parmsType=='none'):
                data=None
            elif(parmsType=='text'):
                data=data.encode() #重新编码一下，不然含中文会报错
            log.info("请求url：%s" % url)
            log.info("请求参数：%s" % data)
            r = RunMethod()

            res = r.run_method(method, url, data, headers)
            # res = r.run_method(method, url, data)
            log.info("返回结果：%s" % res)
            log.info(res.text)

            flag = None
            result=res.text
            if res.status_code==int(checkCode) and checkPoint in result:
                flag=True
            if flag:
                log.info("【测试结果：通过】")
                ExcelData(file_path, sheet_name).write(rowNumber + 1, 13, "Pass")
            else:
                log.info("【测试结果：失败】")
                ExcelData(file_path, sheet_name).write(rowNumber + 1, 13, "Fail")
            # 断言
            self.assertTrue(flag, msg="检查点数据与实际返回数据不一致")
        else:
            unittest.skip("不执行")

# # if __name__ == '__main__':
# #     unittest.main()
#     # Alt+Shift+f10 执行生成报告
#
#     # # 报告样式1
#     # suite = unittest.TestSuite()
#     # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCase))
#     # now = time.strftime('%Y-%m-%d %H_%M_%S')
#     # path=os.path.abspath(os.path.join(os.path.dirname(__file__), "../report"))
#     # report_path =path+ "/report.html"
#     # with open(report_path, "wb") as f:
#     #     runner = HTMLTestRunner(stream=f, title="iServer接口测试报告", description="测试用例执行情况", verbosity=2)
#     #     runner.run(suite)
