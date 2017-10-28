from django.db import models


# Create your models here.
class UserType(models.Model):
    caption = models.CharField(max_length=32)


class UserInfo(models.Model):
    # verbose_name 用于后台管理和modelform的label显示
    username = models.CharField(verbose_name='用户名', max_length=32)
    email = models.EmailField()
    user_type = models.ForeignKey(to='UserType', to_field='id')
