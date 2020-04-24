from rest_framework import serializers
from api.model.banksteelModels import *
# from api.models import *


# Serialisers 定义了API的表现形式
# 使用ModelSerialiser来序列化model层
class NewsSerialisers(serializers.ModelSerializer):
  class Meta:
    model = News #指定要序列化的模型
    fields = ('title', 'createTime', 'content') #指定要序列化的字段


class ProductSerializers(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = ('breedCode', 'breedName', 'cityCode', 'cityName', 'factoryCode', 'factoryName', 'fluctuationPrice','fluctuationSign','materialCode','materialName','price','priceTime','priceType','specName','weightWay','createTime') #指定要序列化的字段

class OrderSerializers(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = ('time', 'amt', 'weight', 'createTime', 'timeStamp')

class WeekOrderSerializers(serializers.ModelSerializer):
  class Meta:
    model = WeekOrder
    fields = ('week', 'mark', 'count', 'weight', 'createTime')