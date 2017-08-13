### start html

1. html就是一个赤裸裸的人
2. css就是华丽的衣服
3. javascript就是人的行为

```
    HTML 与 css 是静态网页的基础
    HTML 常用的标签大概20个 需要全部记住
    css 需要记住常用的效果 颜色, 位置等

    开发后台程序:
        HTML:
            一套浏览器认识的规则 服务器发送有格式的字符串 客户端能够解析
            充当模版作用
            数据库获取数据 然后替换到html指定位置(Web框架)

            标签分类
                自闭和标签<meta xxx> <link>
                主动闭合标签<xxx/>或<xxx></xxx>
```


```
head中的标签

Meta:
    1. 页面编码:
        <meta http-equiv="content-type" content="text/html;charset=utf-8">
    2. 刷新和跳转
        <meta http-equiv="Refresh" content="30">
        <meta http-equiv="Refresh" content="5; Uri=http://www.baidu.com">
    3. 供搜索引擎爬虫使用
        <meta name="keywords" content="星际2,星际老男孩,专访,F91,小色,JOY">
    4. 描述
        <meta name="description" content="xxx">
    5. X-UA-Compatible
        用于兼容IE浏览器
        由于IE6规则与其他浏览器不同 会导致很多适配问题 因此需要兼容浏览器规则
        <meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7">
        <meta http-equiv="X-UA-Compatible" content="IE=IE9">
        当电脑版本号低于设置的版本号时 可以按顺序适配:
        <meta http-equiv="X-UA-Compatible" content="IE=IE9;IE=IE8;IE=IE7">
        强制指定网页在IE浏览器上 按照那种模式打开 不允许手动设置兼容模式

Title:
    网页标题

link: 网页关联文件 相当于import
    rel: relation 是页面的什么元素
    1. css:
        <link rel="stylesheet" type="text/css" href="css/common.css"/>
    2. icon 设置图标
        <link rel="shortcut icon" href="image/favicon.ico"/>
style: 在页面中直接写样式css
    如:
    <style type="text/css">
        .bb{
            background-color: red;
        }
    </style>
script: 在页面中直接写js脚本

```

```
body中的常用标签
    标签分为 块级标签与行内标签(内联标签)
        块级标签会占满一行
        行内标签只占用自己本身的大小
        标签之间可以嵌套

    标签存在的意义:
        1.便于定位获取内容
        2.便于js, css操作标签

    chrome 审查元素的使用
        -定位某个元素
        -查看样式

1. 符号
    文字图标
    空格 &nbsp;
    大于号 &gt;
    小于号 &lt;
2. <p>xxx</p> 分割段落 段落有间距
3. <br> 换行 也可以是<br/> <BR> <BR/>  最好加上'/'
4. <h[1-6]></h[1-6]> 文字大小加粗
5. <span></span> 是行内标签 可扩展标签 自身没有特性 spannable
                    跨度 用于包裹自身内部元素分割实现不同功能

6. <div></div> 重要, 最常用的标签 块级标签 自身没有特性 通常用于div+css
7. <input/> 行内标签
        <input type="text" name="username"/><br/>
        <input type="password" name="password"/><br/>
        <input type="button" value="登录1"/><br/>
        <input type="submit" value="登录2"/>
8
```

### 简易实现一个socket服务端 模拟http操作

    参考http_sample

    这个例子是为了演示浏览器请求网页 服务端接收后返回数据并断开的操作