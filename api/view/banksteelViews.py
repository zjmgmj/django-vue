# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, Http404
from django.http import JsonResponse, QueryDict
from django.db.models import Q
# from django.views.decorators.http import require_http_methods
# import json
# from api.models import models
# from django.core import serializers
# from rest_framework import serializers
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.parsers import JSONParser
# from rest_framework.response import Response
from rest_framework.utils import json
# from .serializers import UserInfoSerialisers, UserTokenSerialisers
from rest_framework.views import APIView
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from django.contrib.auth import login
from api.serializer.banksteelSerializers import *
from api.public.base import *
import time, datetime
# Create your views here.

def index(request):
  return HttpResponse("Hello API !")

def test_api(request):
  return JsonResponse({'result': 0, "msg": "执行成功"})


class NewsView(APIView):
  # 行业聚焦、行业报告
  def post(self, request, *args, **kwargs):
    ret = {'code': 1000, 'msg': None}
    try:
      reqData = json.loads(request.data)
      title = reqData['title']
      content = reqData['content']
      url = reqData['url']
      createTime = reqData['createTime']
      newsObj = News.objects.filter(title=title).first()
      ret['title'] = title
      if not newsObj:
        News.objects.create(title=title, content=content, createTime=createTime, url=url)
        ret['code'] = 1001
        ret['msg'] = 'success'
      else:
        print(title)
    except Exception as e:
      ret['code'] = 1002
      ret['msg'] = e
      print(e)
    return JsonResponse(ret)

  def get(self, request, *args, **kwargs):
    ret = {'code': 1000, 'msg': None}
    try:
      title = request._request.GET.get('title')
      search_dict = dict()
      if title:
        search_dict['title'] = title
      resList = News.objects.filter(**search_dict)
      resData = NewsSerialisers(resList, many=True)
      # obj = News.objects.all()
      # res = NewsSerialisers(obj, many=True)
      ret['list'] = resData.data
      ret['code'] = 1001
      ret['msg'] = 'success'
    except Exception as e:
      ret['code'] = 1002
      ret['msg'] = 'error'
    return JsonResponse(ret)


class ProductViews(APIView):
  def post(self, request, *args, **kwargs):
    ret = {'code': 1000, 'msg': None}
    try:
      reqData = json.loads(request.data)
      list = []
      for item in reqData:
        obj = Product(
          breedCode = item['breedCode'],
          breedName = item['breedName'],
          cityCode = item['cityCode'],
          cityName = item['cityName'],
          factoryCode = item['factoryCode'],
          factoryName = item['factoryName'],
          fluctuationPrice = item['fluctuationPrice'],
          fluctuationSign = item['fluctuationSign'],
          materialCode = item['materialCode'],
          materialName = item['materialName'],
          price = item['price'],
          priceTime = item['priceTime'],
          priceType = item['priceType'],
          specName = item['specName'],
          weightWay = item['weightWay'],
          # createTime = item['createTime']
        )
        list.append(obj)   
      Product.objects.bulk_create(list)
      ret['code'] = 1001
      ret['msg'] = 'success'
    except Exception as e:
      ret['code'] = 1002
      ret['msg'] = e
      print(e)
    return JsonResponse(ret)

class SearchProductViews(APIView):
  def post(self, request, *args, **kwargs):
    ret = {'code': 1000, 'msg': None}
    try:
      reqData = json.dumps(request.data)
      resData = json.loads(reqData)
      current_page = resData['current_page']
      page_obj = Pager(current_page)
      search_dict = dict()
      for item in resData:
        if item != 'current_page':
          search_dict[item] = resData[item]
          print(item)
      searchRes = Product.objects.filter(**search_dict)
      count = searchRes.count()
      resList = searchRes[page_obj.start : page_obj.end]
      resDataSer = ProductSerializers(resList, many=True)
      ret['list'] = resDataSer.data
      ret['total'] = count
      ret['code'] = 1001
      ret['msg'] = 'success'
    except Exception as e:
      ret['code'] = 1002
      ret['msg'] = e
    return JsonResponse(ret)


class OrderViews(APIView):
  def post(self, request, *args, **kwargs):
    ret = {'code': 1000, 'msg': None}
    try:
      reqData = json.loads(request.data)
      list = []
      now = int(time.time())
      timeArray = time.localtime(now)
      timeStyle = time.strftime("%Y-%m-%d", timeArray)
      for item in reqData['amt']:        
        timeItem = int(time.mktime(time.strptime(timeStyle + ' ' + item, "%Y-%m-%d %H:%M")))
        testEmp = Order.objects.filter(time=item, createTime=timeStyle)
        # if not testEmp and timeItem < now:
        if not testEmp:
          obj = Order(
            time = item,
            amt = reqData['amt'][item],
            weight = reqData['weight'][item],
            timeStamp = timeItem
          )
          list.append(obj)
        else:
          weight = testEmp._result_cache[0].weight
          amt = testEmp._result_cache[0].amt
          print(reqData['weight'][item])
          if weight != reqData['weight'][item] or amt != reqData['amt'][item]:
            testEmp.update(weight = reqData['weight'][item], amt=reqData['amt'][item])
      if len(list) > 0:
        Order.objects.bulk_create(list)
      ret['code'] = 1001
      ret['msg'] = 'success'
    except Exception as e:
      ret['code'] = 1002
      ret['msg'] = e
      print(e)
    return JsonResponse(ret)

class SearchOrderViews(APIView):
  def post(self, request, *args, **kwargs):
    ret = {'code': 1000, 'msg': None}
    try:      
      reqData = json.dumps(request.data)
      resData = json.loads(reqData)
      # current_page = resData['current_page']
      # page_obj = Pager(current_page)
      search_dict = dict()
      if 'createTime' in resData:
        print(resData['createTime'])
        timeArr = time.strptime(resData['createTime'], "%Y-%m-%d")
        print(time.mktime(timeArr))
        yesTime = time.strftime("%Y-%m-%d", time.localtime(time.mktime(timeArr) - 86400))        
        searchRes = Order.objects.filter(Q(createTime=resData['createTime']) | Q(createTime=yesTime)).order_by('timeStamp')
        count = searchRes.count()
        resDataSer = OrderSerializers(searchRes, many=True)
        today = []
        lastDay = []
        for item in resDataSer.data:
          if resData['createTime'] == item['createTime']:
            # time.mktime(time.strptime(item['time'], "%H-%M"))
            today.append(item)
          else:
            lastDay.append(item)
        ret['list'] = dict()
        ret['list']['today'] = today
        ret['list']['lastDay'] = lastDay
        # def sortTime(x, y):
        #   if x<y:
        #     return 1
        #   else:
        #     return -1
        # today.sort(sortTime)
      else:
        for item in resData:
          if item != 'current_page':
            search_dict[item] = resData[item]
        searchRes = Order.objects.filter(**search_dict)
        count = searchRes.count()
        # resList = searchRes[page_obj.start : page_obj.end]
        # resList = searchRes
        resDataSer = OrderSerializers(searchRes, many=True)
        ret['list'] = resDataSer.data
      ret['total'] = count
      ret['code'] = 1001
      ret['msg'] = 'success'
    except Exception as e:
      ret['code'] = 1002
      ret['msg'] = e
      print(e)
    return JsonResponse(ret)

class WeekOrderView(APIView):
  def post(self, request, *args, **kwargs):
    ret = {'code': 1000, 'msg': None}
    try:
      reqData = json.loads(request.data)
      currentWeek = reqData['currentWeek']
      lastWeek = reqData['lastWeek']
      list= []
      for item in currentWeek['count']:
        currentEmp = WeekOrder.objects.filter(week=item, mark='current')
        if not currentEmp:
          obj = WeekOrder(
            week= item,
            mark= 'current',
            count= currentWeek['count'][item],
            weight= currentWeek['weight'][item]
          )
          list.append(obj)
        else:
          weight = currentEmp._result_cache[0].weight
          count = currentEmp._result_cache[0].count
          if weight != currentWeek['weight'][item] or count != currentWeek['count'][item]:
            currentEmp.update(weight = currentWeek['weight'][item], count=currentWeek['count'][item])
      for item in lastWeek['count']:
        lastEmp = WeekOrder.objects.filter(week=item, mark='last')
        if not lastEmp:
          obj = WeekOrder(
            week= item,
            mark= 'last',
            count= lastWeek['count'][item],
            weight= lastWeek['weight'][item]
          )
          list.append(obj)
        else:
          weight = lastEmp._result_cache[0].weight
          count = lastEmp._result_cache[0].count
          if weight != lastWeek['weight'][item] or count != lastWeek['count'][item]:
            lastEmp.update(weight = lastWeek['weight'][item], count=lastWeek['count'][item])
      if len(list) > 0:
        WeekOrder.objects.bulk_create(list)
      ret['code'] = 1001
      ret['msg'] = 'success'
    except Exception as e:
      ret['code'] = 1002
      ret['msg'] = e
    return JsonResponse(ret)


class SearchWeekOrderViews(APIView):  
  def post(self, request, *args, **kwargs):
    def takeSecond(elem):
      print(elem['week'])
      return elem['week']
    ret = {'code': 1000, 'msg': None}
    try:      
      reqData = json.dumps(request.data)
      resData = json.loads(reqData)
      # current_page = resData['current_page']
      # page_obj = Pager(current_page)
      # search_dict = dict()
      # for item in resData:
      #   if item != 'current_page':
      #     search_dict[item] = resData[item]
      # searchRes = WeekOrder.objects.filter(**search_dict)
      # count = searchRes.count()
      # resList = searchRes[page_obj.start : page_obj.end]
      resList = WeekOrder.objects.all()
      resDataSer = WeekOrderSerializers(resList, many=True)
      currentWeek = []
      lastWeek = []
      for item in resDataSer.data:
        if item['mark'] == 'current':
          currentWeek.append(item)
        else:
          lastWeek.append(item)
      ret['list'] = dict()
      ret['list']['currentWeek'] = currentWeek
      ret['list']['lastWeek'] = lastWeek
      # ret['list'] = resDataSer.data
      # ret['total'] = count
      ret['code'] = 1001
      ret['msg'] = 'success'
    except Exception as e:
      ret['code'] = 1002
      ret['msg'] = e
      print(e)
    return JsonResponse(ret)