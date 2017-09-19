from django.db import models

# Create your models here.
"""
索引 用于快速查询数据, 在查询中 比如要查name为'matt'的某个数据, 实际上可以通过预先
    在表中插入name的hash值作为一列 如 列名为hash_name, 存储的为name的哈希值(数字)
    在查询的时候 先通过hash(name)获取hash值, 将表中所有的数据按hash排序, 这样可以通过二分法查询
    数据, 这样的速度比遍历查询更快. 相当于对name字段进行了优化, hash_name就是name的索引
"""


class Business(models.Model):
    """ 主机所在的业务线 为枚举 id为django默认创建"""
    # 中文业务名称
    caption = models.CharField(max_length=32)
    # 英文业务名称 允许为空
    # 新增一列 默认不能为空 可以设置默认为空或默认值 或在makemigrations时给以前没有该列的数据设置一个默认值
    english = models.CharField(max_length=32, null=True)


class Host(models.Model):
    """主机表"""
    # 自定义主键
    nid = models.AutoField(primary_key=True)
    # 主机名 db_index = true 为设置索引 查询速度增快
    hostname = models.CharField(max_length=32, db_index=True)
    # ip地址protocol 可以为ipv4 ipv6 both 不符合规则不能在django后台添加 默认为both
    ip = models.GenericIPAddressField(protocol='both', db_index=True)
    # 端口
    port = models.IntegerField()
    # 外键关联 to指代关联的表名 to_field 指代关联的列名
    business = models.ForeignKey(to='Business', to_field='id')
