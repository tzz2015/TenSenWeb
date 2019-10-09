from django.db import models


# Create your models here.

# 用户信息
class UserModel(models.Model):
    appId = models.CharField(max_length=20, null=False, unique=True, help_text='用户的appId')
    realName = models.CharField(max_length=20, null=True, unique=True, help_text='用户的真实姓名')
    nickName = models.CharField(max_length=20, null=True, unique=False, help_text='用户的微信名')
    avatarUrl = models.CharField(max_length=200, null=True, unique=True, help_text='头像地址')
    tag = models.CharField(max_length=20, null=True, unique=False, help_text='标记')
