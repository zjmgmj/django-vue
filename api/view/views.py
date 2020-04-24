# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, Http404
from django.http import JsonResponse, QueryDict
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
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from api.serializer.serializers import *
# Create your views here.

def index(request):
  return HttpResponse("Hello API !")

def test_api(request):
  return JsonResponse({'result': 0, "msg": "执行成功"})

class UserList(APIView):
  # 用户信息
  def post(self, request, *args, **kwargs):
    ret = {'code': 1000, 'msg': None}
    try:
      print(request._request.POST)
      username = request._request.POST.get('username')
      id = request._request.POST.get('id')
      is_active = request._request.POST.get('is_active')
      password = request._request.POST.get('password')
      search_dict = dict()
      if username:
        search_dict['username'] = username
      if password:
        search_dict['password'] = password
      if id:
        search_dict['id'] = id
      if is_active:
        search_dict['is_active'] = is_active
      UserInfoObj = serializers.serialize("json", User.objects.filter(**search_dict))
      # UserInfoObj = UserInfoSerialisers(User.objects.filter(**search_dict), many=True)
      ret['list'] = UserInfoObj
    except Exception as e:
      ret['code'] = 102
      ret['msg'] = 'error'
    # res =  UserInfoSerialisers(ret, many=True)
    return JsonResponse(ret)


class RegisterView(APIView):
  # 注册
  def post(self, request, *args, **kwargs):
    ret = {'code': 1000, 'msg': None}
    try:
      username = request._request.POST.get('username')
      pwd = request._request.POST.get('password')
      role = request._request.POST.get('role')
      obj = User.objects.filter(username=username).first()
      if not obj:
        user = User.objects.create_user(username = username, password = pwd)
        user.save()
        ret['code'] = 100
        ret['msg'] = 'success'
      else:
        ret['code'] = 101
        ret['msg'] = '用户名存在'
    except Exception as e:
      ret['code'] = 102
      ret['msg'] = 'error'
      print(e)
    return JsonResponse(ret)


class LoginView(APIView):
  # 登录
  def post(self, request, *args, **kwargs):
    ret = {'code': 1000, 'msg': None}
    try:
      username = request._request.POST.get('username')
      password = request._request.POST.get('password')
      user = authenticate(username=username, password=password)
      print(user)
      if user is not None:
        if user.is_active:
          login(request, user)
      else:
        ret['code'] = 1001
        ret['msg'] = '用户名或密码错误'
    except Exception as e:
      ret['code'] = 1002
      ret['msg'] = '登录时获取前端提交用户名和密码错误或者是数据库读写错误'
      print(e)
    return JsonResponse(ret)


class CategoryView(APIView):
  # 分类
  def get(self, request, *args, **kwargs):
    # 获取分类
    ret = {'code': 1000, 'msg': None}
    try:
      obj = Category.objects.all()
      res = CategorySerializers(obj, many=True)
      ret['list'] = res.data
    except Exception as e:
      ret['code'] = 1002
      ret['msg'] = 'error'
      print(e)
    return JsonResponse(ret)
  def post(self, request, *args, **kwargs):
    ret = {'code': 1000, 'msg': None}
    try:
      name = request._request.POST.get('name')
      id = request._request.POST.get('id')
      if id:
        # 修改
        Category.objects.filter(id=id).update(name=name)
        ret['code'] = 1000
        ret['msg'] = '修改成功'
      else:
        # 新增
        obj = Category.objects.filter(name=name).first()
        if not obj:
          saveCategory = Category(name=name)
          saveCategory.save()
          res = CategorySerializers(saveCategory)
          ret['code'] = 1000
          ret['msg'] = 'success'
          ret['data'] = res.data
        else:
          ret['code'] = 1002
          ret['msg'] = '分类已存在'
    except Exception as e:
      ret['code'] = 1002
      ret['msg'] = 'error'
      print(e)
    return JsonResponse(ret)

  def delete(self, request, *args, **kwargs):
    ret = {'code': 1000, 'msg': None}
    try:
      print('del')
      delObj = QueryDict(request.body)
      name = delObj.get('name')
      Category.objects.get(name=name).delete()
      ret['code'] = 1000
      ret['msg'] = 'success'
    except Exception as e:
      ret['code'] = 1002
      ret['msg'] = 'error'
      print(e)
    return JsonResponse(ret)

class TagsView(APIView):
  # 标签
  def post(self, request):
    ret = {'code': 1000, 'msg': None}
    try:
      name = request._request.POST.get('name')
      obj = models.Tags.objects.filter(name = name).first()
      if not obj:
        models.Tags.objects.create(name = name)
        ret['code'] = 1000
        ret['msg'] = 'success'
      else:
        ret['code'] = 1001
        ret['msg'] = '标签已存在'
    except Exception as e:
      ret['code'] = 1002
      ret['msg'] = e
    return JsonResponse(ret)

class BlogView(APIView):
  # 文章
  def get(self, request, *args, **kwargs):
    # 获取文章
    ret = {'code': 1000, 'msg': None}
    try:
      title = request._request.GET.get('title')      
      category = request._request.GET.get('category')
      tags = request._request.GET.get('tags')      
      search_dict = dict()
      if title:
        search_dict['title'] = title
      if category:
        search_dict['category'] = category        
      if tags:
        tagsListId = tags.split(',')
      list = Blog.objects.filter(**search_dict)
      resList = []
      for item in list:
        item.tag = []
        for tag in item.tags.all():
          item.tag.append(tag)
        resList.append(item)      
      # ret['list'] = serializers.serialize("json", resList)
      ret['list'] = BlogSerializers(resList, many=True)
      ret['code'] = 1001
      ret['msg'] = 'success'
      print(ret['list'])
    except Exception as e:
      ret['code'] = 1002
      ret['msg'] = 'error'
      print(e)
    # print(ret)
    # return JsonResponse(ret)
    # resData = BlogSerializers(ret, many=True)
    return JsonResponse(ret)

  def post(self, request, *args, **kwargs):    
    ret = {'code': 1000, 'msg': None}
    try:
      title = request._request.POST.get('title')
      content = request._request.POST.get('content')
      category = request._request.POST.get('category')
      tags = request._request.POST.get('tags')
      id = request._request.POST.get('id')
      tagsListId = tags.split(',')
      tagsListObj = []      
      if not id:        
        # 新增文章
        # blog = Blog(title=title, content=content, category_id=category)
        # blog.save()
        # ret['data'] = BlogSerializers(blog)
        blogObj = Blog.objects.create(title=title, content=content, category_id=category)
      else:
        # 修改文章
        blogObj = Blog.objects.filter(id=id).first()
        blogObj.tags.clear()
        Blog.objects.filter(id=id).update(title=title, content=content, category_id=category)
      for i in tagsListId:
        tag = Tags.objects.get(id = int(i))
        tagsListObj.append(tag)
      blogObj.tags.add(*tagsListObj)
      ret['code'] = 1001
      ret['msg'] = 'success'
    except Exception as e:
      ret['code'] = 1002
      ret['msg'] = e
    return JsonResponse(ret)

  def delete(self, request, *args, **kwargs):
    # 删除
    ret = {'code': 1000, 'msg': None}
    try:
      delObj = QueryDict(request.body)
      id = delObj.get('id')
      blogObj = models.Blog.objects.filter(id=id).first()
      blogObj.tags.clear()
      blogObj.delete()
      ret['code']=1001
      ret['msg']='success'
    except Exception as e:
      ret['code'] = 1002
      ret['msg'] = 'error'
      print(e)
    return JsonResponse(ret)