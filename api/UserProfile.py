# -*- coding: utf-8 -*-
from django.db import models
#引入系统用户的分类
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class UserProfile(AbstractUser):
#     """
#     用户类拓展
#     """
#     name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名" )
#     avatar = models.CharField(max_length=100, null=True, blank=True, verbose_name="头像")
#     role = models.CharField(max_length=10, default="员工", verbose_name="角色")

#     class Meta:
#         verbose_name = "用户"
#         verbose_name_plural = verbose_name

#     def __str__(self):
#         return self.username
# class UserInfo(AbstractUser):
#   role_choices = (
#     (1, '普通用户'),
#     (2, '会员'),
#     (3, '系统管理员')
#   )
#   role = models.IntegerField(choices = role_choices, verbose_name="角色")
#   username = models.CharField(max_length = 20, unique = True, verbose_name="用户名")
#   avatar = models.CharField(max_length=100, null=True, blank=True, verbose_name="头像")

#   class Meta:
#     verbose_name = "用户"
#     verbose_name_plural = verbose_name

#   def __str__(self):
#     return self.username

class UserProfile(AbstractUser):
  role_choices = (
    (1, '普通用户'),
    (2, '会员'),
    (3, '系统管理员')
  )
  role = models.IntegerField(choices = role_choices)
  username = models.CharField(max_length = 20, unique = True)
  password = models.CharField(max_length = 20)

  class Meta:
    verbose_name = "用户"
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.username
