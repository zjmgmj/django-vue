# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
class UserInfo(models.Model):
  # 用户信息
  role_choices = (
    (1, '普通用户'),
    (2, '会员'),
    (3, '系统管理员')
  )
  role = models.IntegerField(choices = role_choices, verbose_name="角色")
  username = models.CharField(max_length = 20, unique = True, verbose_name="用户名")  
  avatar = models.CharField(max_length=100, null=True, blank=True, verbose_name="头像")

  def __str__(self):
    return str(self.id)

# class UserToken(models.Model):
#   user = models.OneToOneField(UserInfo, on_delete = models.DO_NOTHING, null = True)
#   token = models.CharField(max_length = 20)

class Category(models.Model):
  # 分类
  name = models.CharField(max_length=20,verbose_name='文章类别')
  number = models.IntegerField(default=1,verbose_name='分类数目')
  def __str__(self):
    return str(self.id)

class Tags(models.Model):
  # 标签
  name = models.CharField(max_length=20,verbose_name='文章标签')
  number = models.IntegerField(default=1, verbose_name='标签数目')
  def __str__(self):
    return str(self.id)

class Blog(models.Model):
  # 文章
  title = models.CharField(max_length=100,verbose_name=u'标题')
  content = models.TextField(default='',verbose_name=u'正文')
  # create_time = models.DateTimeField(default=timezone.now,verbose_name=u'创建时间')
  # modify_time = models.DateTimeField(auto_now=True,verbose_name=u'修改时间')
  # click_nums = models.IntegerField(default=0,verbose_name=u'点击量')
  category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name=u'文章类别')
  tags = models.ManyToManyField(Tags,verbose_name=u'文章标签')
  def __str__(self):
    return str(self.id)

class Comment(models.Model):
  # 评论
  name = models.CharField(max_length=20, default=u'佚名')
  content = models.TextField()
  create_time = models.DateTimeField(auto_now_add=True)
  blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING)
  def __str__(self):
    return str(self.id)
