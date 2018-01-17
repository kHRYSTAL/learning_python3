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

        前端插件开发流程:
            1. 开发表格配置文件, 基类
                   table_config 表格配置
                   condition_config 条件配置 用于页面显示过滤器
            2. 拷贝html页面
            3. RESTful 接口操作数据库并返回



* Django 静态资源浏览器缓存与服务器端不一致问题

        1. 在url后面加问号 可以在url相同的情况下对资源进行刷新请求,从而更新浏览器缓存的静态资源
        2. 加?time=时间戳
        3. 使用md5维护服务器静态资源:
            参考:http://blog.thehumangeo.com/2013/05/01/dynamically-cache-static-files-using-django-and-nginx/
                https://www.zhihu.com/question/20790576



### Base Algorithm

> 算法(Algorithm) 一个计算过程 解决问题的方法

1. 递归

        调用自身
        结束条件
        def func(x)
            if x > 0
                # print(x)  # 5 4 3 2 1
                func(x - 1)
                print(x)  # 1 2 3 4 5

        尾递归与尾递归优化

        递归在通常情况下是比循环慢的 如果不在最后一行执行递归的话, 还会持有上一次递归的上下文
            导致内存溢出, 为解决溢出问题, 可以使用位递归, 即在最后一行执行递归, 且递归函数不持有上次递归的上下文
            为解决慢的问题 可以return 递归函数

2. 复杂度

        时间复杂度

            时间复杂度是用来估计算法运行时间的一个式子(单位)

            一般来说 时间复杂度高的算法比时间复杂度低的算法跑的慢 O(1) < O(log n) < O(n) < O(n * log n) < O(n^2) < O(n^2 * log n) < O(n^3)
            O(1)是常数复杂度

            不常见的时间复杂度:
            O(n!) O(2^n) O(n^n) 时间复杂度都很大

            循环减一般 就是log
            几层循环 就是n的几次方


        空间复杂度

            用来评估算法内存占用大小的一个式子

            "空间换时间"



        列表查找

                从列表中查找指定元素
                    输入: 列表|待查找元素
                    输出: 元素下标|"未查找到元素"


                顺序查找:
                    从列表第一个元素开始, 顺序进行搜索 直到找到为止

                二分查找
                    从有序列表的候选区data[0:n]开始, 通过对待查找的值与候选区的中间值比较, 可以使候选区减少一半


                    def binary_search(data_list, val):
                        low = 0
                        high = len(data_list) - 1
                        while low <= high:
                            mid = (low + high) // 2  # 整除
                            if data_list[mid] == val:
                                return mid
                            elif data_list[mid] < val:
                                low = mid + 1
                            else:
                                high = mid - 1

                        return "can not find index in list"

3. 排序

    * 列表排序
        - 将无序列表变为有序列表

    * 应用场景
        - 各种榜单
        - 各种表格
        - 给二分查找用
        - 给其他算法用

    * 输入:无序列表 输出:有序列表
    * 关键点
        - 有序区
        - 无序区
    * 种类:
        - 冒泡排序
        - 选择排序
        - 插入排序

        - 快速排序

        - 堆排序
        - 归并排序

        - 基数排序
        - 希尔排序
        - 桶排序



