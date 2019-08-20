from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Category(models.Model):
    cname = models.CharField(max_length=30, unique=True, verbose_name='类别')

    class Meta:
        db_table = 't_category'
        verbose_name_plural = u'类别'

    def __str__(self):
        return u'Category:%s' % self.cname

class Tag(models.Model):
    tname = models.CharField(max_length=30, unique=True, verbose_name='标签')

    class Meta:
        db_table = 't_tag'
        verbose_name_plural = u'标签'

    def __str__(self):
        return u'%s' % self.tname

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='帖子')
    desc = models.CharField(max_length=100)
    content = RichTextUploadingField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    class Meta:
        db_table = 't_post'
        verbose_name_plural = u'帖子'

    def __str__(self):
        return u'Post:%s' % self.title