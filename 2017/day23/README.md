- 博客系统
- CMDB 资产管理系统 如何去实现
    * 资产采集 放到资产数据库
    * 将采集的数据通过api放到数据库, 认证
    * 统计图, 可视化管理

- 组合搜索组件

        urls.py:

            url(r'^article-(?P<article_type_id>\d+)-(?P<category_id>\d+).html', views.article, name='article')

        views.py:
        def article(request, *args, **kwargs):
            # 获取当前url
            print(request.path_info)
            # 通过url别名反向获取url
            from django.urls import reverse
            url = reverse('article', kwargs=kwargs)
            print(url)

            """
            :param request:
            :param args: 用于接收没有指明key的正则参数
            :param kwargs: 用于接受指明key的正则参数 字典
                {'article_type_id': '1', 'category_id': '0'}
            :return:
            """
            condition = {}  # 空字典为默认值, 相当于没有增加文章查询条件
            for k, v in kwargs.items():
                if v == '0':  # 数据库id是从1开始的, 所以当为0时 认为是查询全部
                    pass
                else:
                    condition[k] = v

            article_type_list = models.ArticleType.objects.all()
            category_list = models.Category.objects.all()
            # 字典解包,当作参数传递
            article_list = models.Article.objects.filter(**condition)
            return render(request, 'article.html', {
                'article_type_list': article_type_list,
                'category_list': category_list,
                'article_list': article_list
            })
