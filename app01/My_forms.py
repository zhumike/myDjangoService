# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :app01
# @File     :My_forms
# @Date     :2021/10/10 6:21 下午
# @Author   :zhuzhenzhong
# @Software :PyCharm
-------------------------------------------------
"""
from django import forms
from django.core.exceptions import ValidationError
from app01 import models

class EmpForm(forms.Form):
    name = forms.CharField(min_length=2, label="姓名", error_messages={"required": "该字段不能为空!", "min_length": "用户名太短。"})
    age = forms.IntegerField(label="年龄")
    salary = forms.DecimalField(max_digits=10, decimal_places=2, label="工资")
    r_salary = forms.DecimalField(max_digits=10, decimal_places=2, label="请再输入工资")


    def clean_name(self):  # 局部钩子
        val = self.cleaned_data.get("name")


        if val.isdigit():
            raise ValidationError("用户名不能是纯数字")
        elif models.Emp.objects.filter(name=val):
            raise ValidationError("用户名已存在！")
        else:
            return val

    def clean(self):  # 全局钩子 确认两次输入的工资是否一致。
        val = self.cleaned_data.get("salary")
        r_val = self.cleaned_data.get("r_salary")


        if val == r_val:
            return self.cleaned_data
        else:
            raise ValidationError("请确认工资是否一致。")