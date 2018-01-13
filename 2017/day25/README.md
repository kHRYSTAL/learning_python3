### CMDB后台管理
- 资产列表(CURD)
- 业务线列表(CURD)
- 用户列表(CURD)
- 组列表(CURD)
- ...

公共组建: 删改查(models.py)

* 查:
        资产列表

        配置文件: key代指查询条件, value为查询表的列名
        config = [
            {'q': 'id'},
            {'q': 'name'},
            ]
        --------
        values_list = ['id', name] 作为column传入下方查询参数
        查询:
            querySet = model.TB.objects.filter([condition]).values([column name])[start, end]
                --> [{},{},{}]

            querySet = model.TB.objects.filter([condition]).values(*values_list)

        标配: 配置 + 数据库操作

* 前端插件定制表结构

        定制td内容以及属性

        参考 app01/views.py ServerView, ServerJsonView

* Django 静态资源浏览器缓存与服务器端不一致问题

        1. 在url后面加问号 可以在url相同的情况下对资源进行刷新请求,从而更新浏览器缓存的静态资源
        2. 加?time=时间戳
        3. 使用md5维护服务器静态资源:
            参考:http://blog.thehumangeo.com/2013/05/01/dynamically-cache-static-files-using-django-and-nginx/


### Base Algorithm

> 算法(Algorithm) 一个计算过程 解决问题的方法
