from django.db import models


# Create your models here.

# class ArticleType(models.Model):
#     """ 文章分类 废弃 使用内存级别type_choice"""
#     caption = models.CharField(max_length=16)


class Category(models.Model):
    """分类标签"""
    # 标题
    caption = models.CharField(max_length=16)


class Article(models.Model):
    """文章"""
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    # article_type = models.ForeignKey(ArticleType)
    type_choice = (
        (1, 'Python'),
        (2, 'OpenStack'),
        (3, 'Linux')
    )
    # 设置枚举类型 数据库存储的是数字 但文字存储在内存中
    # 1 避免跨表操作 2 不变动的数据 放到内存中优化查询 避免浪费资源和时间
    article_type_id = models.IntegerField(choices=type_choice)
