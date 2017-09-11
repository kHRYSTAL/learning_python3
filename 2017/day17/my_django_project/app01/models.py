from django.db import models


# Create your models here.

class UserInfo(models.Model):
    # 默认创建一个id列 自增 主键
    # 用户名列 字符串类型 指定长度
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
