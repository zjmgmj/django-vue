# -*- coding: utf-8 -*-
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [    
    path(r'test_api/', views.test_api, name='api'),
    path(r'tokenAuth/', obtain_jwt_token),
    path(r'Register/', views.RegisterView.as_view(), name='api'),
    path(r'login/', views.LoginView.as_view(), name='api'),
    path(r'userList/', views.UserList.as_view(), name='api'),
    path(r'addCategory/', views.CategoryView.as_view()),
    path(r'delCategory/', views.CategoryView.as_view()),
    path(r'editCategory/', views.CategoryView.as_view()),
    path(r'getCategory/', views.CategoryView.as_view()),
    path(r'addTags/', views.TagsView.as_view()),
    path(r'addBlog/', views.BlogView.as_view()),
    path(r'delBlog/', views.BlogView.as_view()),
    path(r'editBlog/', views.BlogView.as_view()),
    path(r'getBlog/', views.BlogView.as_view()),
]