import math
from django.shortcuts import render

# Create your views here.
from .models import *
from django.core.paginator import Paginator

# 查询所有方法
def queryView(request, num=1):
    num = int(num)
    # 查询所有信息
    postList = Post.objects.all().order_by('-created')

    # 创建分页对象
    pageObj = Paginator(postList, 1)

    # 获取当前页数据
    prePageList = pageObj.page(num)

    # 获取页码编号(从开始页到结束页)
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 0:
        begin = 1

    end = begin + 9
    if end > pageObj.num_pages:
        end = pageObj.num_pages

    if end <= 10:
        begin = 1
    else:
        end = begin + 9

    pageList = range(begin, end + 1)

    return render(request, 'index.html', {'blogList': prePageList, 'pageList': pageList, 'curNum': num})

# 查看全文
def detailView(request, postid):
    postid = int(postid)
    # 根据id查询全部
    post = Post.objects.get(id=postid)
    return render(request, 'detail.html', {'post': post})

# 显示类别下的全部文章
def categoryView(request, cateid):
    cateid = int(cateid)
    postList = Post.objects.filter(category_id=cateid)
    return render(request, 'article.html', {'postList': postList})

# 根据时间显示全部文章
def archiveView(request, year, month):
    print(year, month)
    postList = Post.objects.filter(created__year=year, created__month=month)
    return render(request, 'article.html', {'postList': postList})