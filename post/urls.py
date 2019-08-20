#coding=utf-8
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.queryView),
    re_path(r'^page/(\d+)', views.queryView),
    re_path(r'^post/(\d+)', views.detailView),
    re_path(r'^category/(\d+)', views.categoryView),
    re_path(r'^archive/(\d+)/(\d+)', views.archiveView),
]