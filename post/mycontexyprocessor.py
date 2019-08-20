#coding=utf-8
from django.db.models import Count

from .models import Post

def getRightInfo(request):
    # 分类
    r_catePost = Post.objects.values('category__cname', 'category').annotate(c=Count('*')).order_by('-c')
    # 近期文章
    r_recPost = Post.objects.all().order_by('-created')[:3]
    # 归档信息
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SELECT created,COUNT('*') from t_post GROUP BY(DATE_FORMAT(created,'%Y-%m')) ORDER BY created desc")
    # fetchall()返回一个元组
    r_filePost = cursor.fetchall()

    return {
        'r_catePost': r_catePost,
        'r_recPost': r_recPost,
        'r_filePost': r_filePost
    }