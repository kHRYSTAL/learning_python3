- 博客系统
- CMDB 资产管理系统 如何去实现
    * 资产采集 放到资产数据库
    * 将采集的数据通过api放到数据库, 认证
    * 统计图, 可视化管理

- 组合搜索组件

    * 组合搜索: 在页面上通过一类或多类标签进行过滤数据库查询
    * 难点: 多类标签时 选择一类标签时需要固定其他类的标签选择
    * 优化: html中可以使用自定义函数 优化标签代码 (参考templatetags/custom_tpl_func.py)


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


- JSONP 跨域请求的 jQuery 实现

        Ajax直接请求普通文件存在跨域无权限访问的问题(浏览器会拦截你的请求 防止恶意代码)，甭管你是静态页面、动态网页、web服务、WCF，只要是跨域请求，一律不准；
        不过我们又发现，Web页面上调用js文件时则不受是否跨域的影响（不仅如此，我们还发现凡是拥有"src"这个属性的标签都拥有跨域的能力，比如<script>、<img>、<iframe>）；

        于是可以判断，当前阶段如果想通过纯web端（ActiveX控件、服务端代理、属于未来的HTML5之Websocket等方式不算）跨域访问数据就只有一种可能，那就是在远程服务器上设法把数据装进js格式的文件里，供客户端调用和进一步处理；
        恰巧我们已经知道有一种叫做JSON的纯字符数据格式可以简洁的描述复杂数据，更妙的是JSON还被js原生支持，所以在客户端几乎可以随心所欲的处理这种格式的数据；
        这样子解决方案就呼之欲出了，web客户端通过与调用脚本一模一样的方式，来调用跨域服务器上动态生成的js格式文件（一般以JSON为后缀），显而易见，服务器之所以要动态生成JSON文件，目的就在于把客户端需要的数据装入进去。
        客户端在对JSON文件调用成功之后，也就获得了自己所需的数据，剩下的就是按照自己需求进行处理和展现了，这种获取远程数据的方式看起来非常像AJAX，但其实并不一样。
        为了便于客户端使用数据，逐渐形成了一种非正式传输协议，人们把它称作JSONP，该协议的一个要点就是允许用户传递一个callback参数给服务端，然后服务端返回数据时会将这个callback参数作为函数名来包裹住JSON数据，这样客户端就可以随意定制自己的函数来自动处理返回数据了。

        原理实际上就是在head里快速的增加一端js代码 代码参数为请求的json 然后快速删除
        告诉浏览器 这段伪js可以请求到

        (只能发GET请求)

        参考jsonp.html


