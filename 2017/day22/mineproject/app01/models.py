from django.db import models


# Create your models here.
class UserType(models.Model):
    caption = models.CharField(max_length=32)

    def __str__(self):
        # 在前端页面选择器显示的为caption 而不是usertype对象
        return self.caption


class UserGroup(models.Model):
    """
    用户组 与userinfo实现多对多
    """
    name = models.CharField(max_length=32)


class UserInfo(models.Model):
    # verbose_name 用于后台管理和modelform的label显示
    username = models.CharField(verbose_name='用户名', max_length=32)
    email = models.EmailField()
    user_type = models.ForeignKey(to='UserType', to_field='id')
    u2g = models.ManyToManyField(UserGroup)
