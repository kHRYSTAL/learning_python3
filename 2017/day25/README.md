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



### Base Algorithm

> 算法(Algorithm) 一个计算过程 解决问题的方法
