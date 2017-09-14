from django.db import models


# Create your models here.

class UserInfo(models.Model):
    # 默认创建一个id列 自增 主键
    # 用户名列 字符串类型 指定长度
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=60)
    # gender = models.CharField(max_length=10, null=True)  # 允许为空
    admin_column = models.EmailField(max_length=20)


class UserGroup(models.Model):
    # 创建一个自增的列 并设置为主键 django将不再设置默认的id列
    gid = models.AutoField(primary_key=True)
    # 标题
    caption = models.CharField(max_length=32)