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

    user_type_choices = (
        (1, "超级用户"),
        (2, "普通用户"),
        (3, "未注册用户"),
    )
    # 设置枚举类型 即在管理后台中该项添加或修改时可以进行单选菜单选择 数据库存储的是数字 但文字存储在内存中
    user_type_id = models.IntegerField(choices=user_type_choices)

    # 外键关联 参数为表名 关联的表唯一值 默认值
    # to_field 可以不写 默认管理表的id
    user_group = models.ForeignKey('UserGroup', to_field='gid', default=1)


class UserGroup(models.Model):
    # 创建一个自增的列 并设置为主键 django将不再设置默认的id列
    gid = models.AutoField(primary_key=True)
    # 标题
    caption = models.CharField(max_length=32)
    # 允许为空 自动设置为当前时间 且只做添加操作 如果该字段有值 则不会添加
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    # 允许为空 自动设置为当前时间 该字段不管有没有值 都会覆盖
    update_time = models.DateTimeField(auto_now=True, null=True)


# 注意 在这种方式下更新数据内容, update_time不会更新时间
# obj = UserGroup.objects.filter(id=1).update(caption="adfg")
# 应使用
# obj = UserGroup.objects.filter(id=1).first()
# obj.caption = "asdf"
# obj.save()
