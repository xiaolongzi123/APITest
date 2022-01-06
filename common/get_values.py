#coding=utf-8
import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)
class getvales():
    def getdict(dict1, values):
        global values1,va #定义全局变量
        values1 = values
        for k, v in dict1.items(): #把字典的key和values变成数组
            if k == values:
                va = v

            elif list is type(v): #判断类型是不是list
                getvales.getlsit(v)

            elif type(v) is dict:
                getvales.getdict(v, values1)

            else:
                print(str(k) + ":----" + str(v))

        return va

    def getlsit(list1):
        for i in list1:
            if list is type(i):
                getvales.getlsit(i)

            elif dict is type(i):
                getvales.getdict(i, values1)
            else:
                print(list1)


if __name__ == "__main__":
    dict1 = {'result': {'content': [
        {'areaCode': '4XXXXXXX00', 'branchFee': 100.0, 'checkStatus': 'check_no', 'completionRate48': False,
         'consignee': '刘先生', 'consigneeTel': '1XXXXXXXX64', 'countdown': 0, 'createDate': '2017-12-01 14:52:52',
         'goods': '布皮艺沙发', 'id': 'WAQ2Wm2AjlEdwlRU', 'installFee': 40.0, 'items': 1, 'jingdong': False,
         'jingdongConfirm': False, 'matchType': '人工匹配', 'matchingFailureReason': '此单xXXXXXX后再做安排',
         'msfCheck': '未核销', 'orderSourceCode': '', 'orgName': '一智XXXXXXXX业部', 'packingNumber': 2, 'payArrive': 0.0,
         'payCash': 0.0, 'payMonth': 120.0, 'payReturn': 0.0, 'payType': '月结', 'pickUpAddress': 'XXXXXXX库',
         'pickUpTel': '13532120095', 'pickUpTime': '', 'readOnly': False, 'receiveAddress': '广东省广州市增城区XXXX',
         'remark': '', 'replaceCharge': 0.0, 'serviceType': '配送到家并安装', 'shipper': 'XXXXX有限公司', 'taskStatus': '待分配',
         'taskStatusShow': '待分配', 'taskType': '调度任务', 'tmail': False, 'trunkEndDate': '2017-12-01 15:27:06',
         'volumes': 1.3, 'waybillId': '1zt18824149564', 'weights': 0.0, 'worker': 'XXX', 'workerTel': '13XXXXXXXX37'}],
        'first': True, 'last': True, 'number': 0, 'numberOfElements': 1, 'size': 10, 'totalElements': 1,
        'totalPages': 1}}
    abc = getvales.getdict(dict1, "waybillId")
    print(abc)