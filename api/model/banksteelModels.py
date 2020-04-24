# -*- coding: utf-8 -*-
from django.db import models
from django.utils.timezone import now
# now = timezone.now()

class News(models.Model):
  # 分类
  title = models.CharField(max_length=100,verbose_name='文章标题')
  # createTime = models.CharField(max_length=10,verbose_name='时间')
  createTime = models.DateTimeField(verbose_name='时间')
  url = models.CharField(max_length=100, verbose_name='来源')
  content = models.TextField(default='', verbose_name=u'正文')
  def __str__(self):
    return str(self.id)


class Product(models.Model):
  breedCode = models.CharField(max_length=100)
  breedName = models.CharField(max_length=100)
  cityCode = models.CharField(max_length=100)
  cityName = models.CharField(max_length=100)
  factoryCode = models.CharField(max_length=100)
  factoryName = models.CharField(max_length=100)
  fluctuationPrice = models.SmallIntegerField()
  fluctuationSign = models.SmallIntegerField()
  materialCode = models.CharField(max_length=100)
  materialName = models.CharField(max_length=100)
  price = models.SmallIntegerField()
  priceTime = models.CharField(max_length=100)
  priceType = models.CharField(max_length=100)
  specName = models.CharField(max_length=100)
  weightWay = models.SmallIntegerField()
  createTime = models.DateField(default=now)

class Order(models.Model):
  amt = models.PositiveIntegerField()
  weight = models.PositiveIntegerField()
  time = models.CharField(max_length=50)
  timeStamp = models.PositiveIntegerField(default=0)
  createTime = models.DateField(default=now)
  
class WeekOrder(models.Model):
  week = models.IntegerField()  
  mark = models.CharField(max_length=50)  
  count = models.PositiveIntegerField()
  weight = models.PositiveIntegerField()
  createTime = models.DateField(default=now)