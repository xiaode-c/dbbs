# coding:utf-8

from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    '''
    文章表
    '''
    title = models.CharField(max_length=255, unique=True)
    # verbose_name在admin前端显示的文字
    category = models.ForeignKey('Category', verbose_name=u"版块")
    head_imag = models.ImageField(upload_to='uploads')
    content = models.TextField()
    author = models.ForeignKey('UserProfile')
    summary = models.CharField(max_length=255)

    # auto_now自动创建为当前时间
    pub_date = models.DateTimeField(auto_now=True)
    hidden = models.BooleanField(default=False)
    # 显示的优先级
    level = models.IntegerField(default=1000)

    def __str__(self):
        return "<%s - author:%s>" % (self.id, self.author)

class ThumbUp(models.Model):
    '''
    点赞表
    '''
    article = models.ForeignKey(Article)
    user = models.ForeignKey('UserProfile')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<User: %s>" % self.user



class Comment(models.Model):
    '''
    评论表
    '''
    article = models.ForeignKey(Article)
    user = models.ForeignKey("UserProfile")
    pub_date = models.DateTimeField(auto_now=True)
    comment = models.TextField(max_length=1000)
    # blank是指admin可以不选，null是指数据库可以为空
    parent_comment = models.ForeignKey('self', related_name="parent", blank=True, null=True)
    # parent_comment = models.ForeignKey('Comment', )

    def __str__(self):
        return "<Comment: %s>" % self.id


class Category(models.Model):
    '''
    版块表
    '''
    name = models.CharField(max_length=64, unique=True)
    manager = models.ManyToManyField('UserProfile')

    def __str__(self):
        return "<Category: %s>" % self.name


class UserProfile(models.Model):
    '''
    用户信息表
    '''
    name = models.CharField(max_length=32)
    user = models.OneToOneField(User)
    groups = models.ManyToManyField('UserGroup')

    def __str__(self):
        return "<User: %s>" % self.name


class UserGroup(models.Model):
    '''
    用户组
    '''
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return "<UserGroup: %s>" % self.name


