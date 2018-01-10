from django.db import models


# Create your models here.
class UserInfo(models.Model):
    """用户表"""
    name = models.CharField(max_length=32)
    age = models.IntegerField()


class BusinessUnit(models.Model):
    """业务线表"""
    name = models.CharField(max_length=32)


class Server(models.Model):
    """服务器表"""
    server_type_choices = {
        (1, 'WEB'),
        (2, '存储'),
        (3, '缓存'),
    }
    server_type = models.IntegerField(choices=server_type_choices)
    hostname = models.CharField(max_length=32)
    port = models.IntegerField()
    business_unit = models.ForeignKey('BusinessUnit')  # 所属业务线
    user = models.ForeignKey('UserInfo')  # 服务器管理员
