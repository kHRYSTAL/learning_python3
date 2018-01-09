from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()


class BusinessUnit(models.Model):
    name = models.CharField(max_length=32)


class Server(models.Model):
    server_type_choices = {
        (1, 'WEB'),
        (2, '存储'),
        (3, '缓存'),
    }
    server_type = models.IntegerField(choices=server_type_choices)
    hostname = models.CharField(max_length=32)
    port = models.IntegerField()
    business_unit = models.ForeignKey('BusinessUnit')
    user = models.ForeignKey('UserInfo')
