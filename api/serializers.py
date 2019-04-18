from rest_framework import serializers
from api.models import UserInfo, Category, Tags, Blog, Comment
# from api.models import *


# Serialisers 定义了API的表现形式
# 使用ModelSerialiser来序列化model层
class UserInfoSerialisers(serializers.ModelSerializer):
  class Meta:
    model = UserInfo #指定要序列化的模型
    fields = ('role', 'username', 'avatar') #指定要序列化的字段


# class UserTokenSerialisers(serializers.ModelSerializer):
#   class Meta:
#     module = UserToken
#     fields = ('user', 'token')

class CategorySerializers(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = "__all__"

class TagsSerializers(serializers.ModelSerializer):
  class Meta:
    model = Tags
    fields = "__all__"

class BlogSerializers(serializers.ModelSerializer):
  tags = TagsSerializers()
  category = CategorySerializers()
  class Meta:
    model = Blog
    fields = "__all__"