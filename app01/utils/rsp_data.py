# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :app01
# @File     :rsp_data
# @Date     :2025/5/29 14:33
# @Author   :zhuzhenzhong
# @Description :PyCharm
-------------------------------------------------
"""
from django.http import JsonResponse
from app01.utils.json_status import Code
import os
import sys
import django


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
# 将配置文件的路径写到django_settings_module环境变量中
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app01.settings")
django.setup()


class  Rsp_Data:


    #标准接口响应函数
    @staticmethod
    def result(code=Code.ok, message=' ', data=None, **kwargs):
        json_dict = {"code": code, 'msg': message, "data": data}
        if kwargs and isinstance(kwargs, dict):
            json_dict.update(kwargs)
        return JsonResponse(json_dict)

    @staticmethod
    def params_error(message='参数错误',data=None):
        '''
         参数错误
        :param message:传给前端的信息
        :param data: 传给前端的数据，字典类型
        :return: Json响应
        '''
        return Rsp_Data.result(code=Code.params_error, message=message, data=data)

    @staticmethod
    def un_auth_error(code=Code.un_auth_error, message='权限异常', data=None):
        '''
        权限错误
        :param code:
        :param message:
        :param data:
        :return:
        '''
        return Rsp_Data.result(code=code, message=message, data=data)

    @staticmethod
    def server_error(code=Code.server_error, message='服务器错误', data=None):
        '''
        服务器错误
        :param code:
        :param message:
        :param data:
        :return:
        '''
        return Rsp_Data.result(code=code, message=message, data=data)


if __name__ == "__main__":
    rp=Rsp_Data.result(code=2, message="ok", data="good")
    rp2 = Rsp_Data.server_error()
    rp3 = Rsp_Data.un_auth_error()
    rp4 = Rsp_Data.params_error()


    print(rp.content.decode('utf-8'))
    print(rp2.content.decode('utf-8'))
    print(rp3.content)
    print(rp4.content)




