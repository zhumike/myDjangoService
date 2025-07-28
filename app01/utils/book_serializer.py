# # -*- coding: utf-8 -*-
# """
# -------------------------------------------------
# # @Project  :myDjangoService
# # @File     :book_serializer
# # @Date     :2025/7/28 10:20
# # @Author   :zhuzhenzhong
# # @Description :PyCharm
# -------------------------------------------------
# """
# from app01.models import Publish
# from rest_framework import serializers
#
#
# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Publish
#         fields = ['id', 'title', 'author']  # 指定字段
