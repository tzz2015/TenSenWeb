from django.db import models


# Create your models here.

# 用户信息
class UserModel(models.Model):
    appId = models.CharField(max_length=20, null=False, unique=True, help_text='用户的appId')
    realName = models.CharField(max_length=20, null=True, unique=True, help_text='用户的真实姓名')
    nickName = models.CharField(max_length=20, null=True, unique=False, help_text='用户的微信名')
    avatarUrl = models.CharField(max_length=200, null=True, unique=True, help_text='头像地址')
    tag = models.CharField(max_length=20, null=True, unique=False, help_text='标记')
    phone = models.CharField(max_length=20, null=True, unique=False, help_text='联系手机')


# 轮播图
class BannerModel(models.Model):
    imageUrl = models.CharField(max_length=255, null=True, unique=True, help_text='banner图片地址')
    des = models.CharField(max_length=20, null=True, unique=False, help_text='描述')


# 感慨语录
class FeelingsModel(models.Model):
    word = models.CharField(max_length=100, null=True, unique=False, help_text='语录')
    form = models.ForeignKey("UserModel", null=False, on_delete=models.CASCADE, help_text='来源')


# 需求收集
class DemandModel(models.Model):
    form = models.ForeignKey("UserModel", null=False, on_delete=models.CASCADE, help_text='来源')
    demand = models.CharField(max_length=255, null=True, unique=False, help_text='需求')
    start = models.IntegerField(default=0, null=False, help_text='点赞数')
