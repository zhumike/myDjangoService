# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :app01
# @File     :view
# @Date     :2021/10/4 10:03 上午
# @Author   :zhuzhenzhong
# @Software :PyCharm
-------------------------------------------------
"""
import json

from django.core import serializers

from .utils.rsp_data import Rsp_Data
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from django.db.models import Avg,Max,Min,Count,Sum  #   引入函数
from django.db.models import Q
from django.shortcuts import render, HttpResponse
from app01.My_forms import  EmpForm
from app01 import models
from django.core.exceptions import ValidationError
from django.forms.models import model_to_dict

#插入数据
def add_book(request):
    book = models.Book(title="菜鸟教程2",price=300,publish="菜鸟出版社",pub_date="2021-10-01")
    book.save()
    return HttpResponse("<p>数据添加成功！</p>")

#查找所有数据
def query_book(request):
    books = models.Book.objects.all()
    print(books,type(books)) # QuerySet类型，类似于list，访问 url 时数据显示在命令行窗口中。

    # for i in books:
    #     print(i.title)
    # 方法1: 使用Django的serializers模块
    # data = serializers.serialize("json", books)
    # return HttpResponse(data)

    #方法二，使用JsonResponse ，参考：https://blog.csdn.net/weixin_63779518/article/details/147876499
    # return JsonResponse(list(books.values()),safe=False,status=200)

    #方法三，使用自定义封装工具类
    # a=Rsp_Data.result(message="success", data=list(books.values()))
    data_dict_list = [model_to_dict(item) for item in books]
    # print(data_dict_list[0]['title'])

    return Rsp_Data.result(message="success",data=data_dict_list)


def query_publish(request):
    #  获取出版社对象
    pub_obj = models.Publish.objects.filter(pk=1).first()
    #  给书籍的出版社属性publish传出版社对象
    book = models.Book2.objects.create(title="菜鸟教程", price=200, pub_date="2010-10-10", publish=pub_obj)
    print(book, type(book))
    return HttpResponse(book)



def query_author(request):
    #  获取作者对象
    chong = models.Author.objects.filter(name="令狐冲").first()
    ying = models.Author.objects.filter(name="任盈盈").first()
    #  获取书籍对象
    book = models.Book2.objects.filter(title="菜鸟教程").first()
    #  给书籍对象的 authors 属性用 add 方法传作者对象
    book.authors.add(chong, ying)
    return HttpResponse(book)


def query_authors_add(request):
    book_obj = models.Book2.objects.get(id=10)
    author_list = models.Author.objects.filter(id__gt=2)
    book_obj.authors.add(*author_list)  # 将 id 大于2的作者对象添加到这本书的作者集合中
    return HttpResponse("ok")

def query_avg_price(request):
    res = models.Book2.objects.aggregate(Avg("price"))
    print(res, type(res))
    return HttpResponse("书籍的平均价格是%f"%res['price__avg'])

def query_book_multi(request):
    res = models.Book2.objects.aggregate(c=Count("id"),max=Max("price"),min=Min("price"))
    print(res, type(res))
    return HttpResponse("书籍的总数是%d,最高价是%d,最低价是%d"%(res['c'],res['max'],res['min']))

def query_publish_min(request):
    # res = models.Publish.objects.values("name").annotate(in_price=Min("book__price"))
    res = models.Publish.objects.values("name","city")

    print(res)
    return HttpResponse(res)

def query_book_dync(request):
    res = models.Book.objects.filter(Q(price__gt=350) | Q(title__startswith="菜")).values("title", "price")
    print(res)
    return HttpResponse(res)


'''表单提交'''
def add_emp(request):
    if request.method == "GET":
        form = EmpForm()  # 初始化form对象
        return render(request, "add_emp.html", {"form":form})
    else:
        form = EmpForm(request.POST)  # 将数据传给form对象
        if form.is_valid():  # 进行校验
            data = form.cleaned_data
            data.pop("r_salary")
            models.Emp.objects.create(**data)
            return redirect("/index/")
        else:  # 校验失败
            clear_errors = form.errors.get("__all__")  # 获取全局钩子错误信息
            return render(request, "add_emp.html", {"form": form, "clear_errors": clear_errors})