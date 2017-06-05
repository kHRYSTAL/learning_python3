### 常用模块
* 定义: 用来从逻辑上组织py代码(变量 函数 类 逻辑, 目的是为了实现功能) 本质就是.py结尾的python文件

    包是从逻辑上组织模块的

* 导入方法

* import 模块 本质(路径搜索与搜索路径)

    将import文件中的所有代码赋给了变量
    在导入package的文件中把代码解释了一遍

* import package(包) 本质就是去解释包下的__init__文件

* 导入优化

* 模块的分类

* 导入包

标注库:
1. time与datetime
    时间戳 格式化时间字符串 struct_time(以元组表示的时间)
    时间戳 time.time() 1970到现在的秒数
    time.struct_time()

