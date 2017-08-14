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
=====================能提交到后台的标签start=======================
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

        单选 radio name 相同为互斥 提交的为value checked="checked"为默认选中
             <form>
                <div>
                    <p>请选择性别</p>
                    男:<input type="radio" name="sex" value="1" checked="checked"><br/>
                    女:<input type="radio" name="sex" value="2"><br/>
                </div>
                <input type="submit" value="提交">
             </form>

        多选 checkbox name可以相同也可以不同
            <form>
                <p>请选择爱好</p>
                篮球:<input type="checkbox" name="interest" value="1" checked="checked"><br/>
                足球:<input type="checkbox" name="interest" value="2"><br/>
                网球:<input type="checkbox" name="interest" value="3"><br/>
                <input type="submit" value="提交">
            </form>

        上传文件 file 依赖form表单的属性 enctype="multipart/form-data" 表示分block上传
            <form enctype="multipart/form-data">
                <p>上传文件</p>
                 <input type="file" name="fname">
                <input type="submit" value="提交">
            </form>

        重置 reset 需要写到表单里
            <input type="reset" value="重置"/>

8.  textarea  行内标签 多行文本输入
    <textarea name="multi_text">default value</textarea>

9. 下拉菜单
    <select name="city">
        <option value="1">北京</option>
        <option value="2">上海</option>
        <option value="3">广州</option>
        <option value="4"  selected="selected">天津</option>
    </select>

    默认尺寸
    <select name="city" size="10">
        <option value="1">北京</option>
        <option value="2">上海</option>
        <option value="3">广州</option>
        <option value="4"  selected="selected">天津</option>
    </select>

    多选
    <select name="city" size="4" multiple="multiple">
        <option value="1">北京</option>
        <option value="2">上海</option>
        <option value="3">广州</option>
        <option value="4" selected="selected">天津</option>
    </select>

    分组
    <select name="city" size="4">
        <optgroup label="直辖市">
            <option value="1">北京</option>
            <option value="2">上海</option>
            <option value="3">南京</option>
            <option value="4">天津</option>
        </optgroup>
        <optgroup label="山东省">
            <option value="5">济南</option>
            <option value="6">蓬莱</option>
            <option value="7">泰安</option>
        </optgroup>
    </select>
=====================能提交到后台的标签end=======================

=====================修饰/功能标签start=======================
在html中 id是不能重复的 name是可以重复的
        id是页面内的操作的标记 name是与服务器交互的标记key
1. a标签
    跳转
        <a href="http://www.baidu.com">百度</a>
        <!--在空白页打开-->
        <a href="http://www.baidu.com" target="_blank">百度</a>

    锚点-在当前页面导航 跳转到指定位置 #某个标签的id id不能重复
        <a href="#i1">第一章</a>
        <a href="#i2">第二章</a>
        <a href="#i3">第三章</a>
        <a href="#i4">第四章</a>

        <div id="i1" style="height: 600px;">第一章的内容</div>
        <div id="i2" style="height: 600px;">第二章的内容</div>
        <div id="i3" style="height: 600px;">第三章的内容</div>
        <div id="i4" style="height: 600px;">第四章的内容</div>

2. img 在图片路径错误或解析失败显示alt的内容 在鼠标放到图片上显示title的内容
     <a href="http://www.baidu.com">
        <img src="1.jpeg" style="height: 200px; width: 200px" alt="保利尼奥" title="暴力鸟>
     </a>

3.列表
    1.显示点
        <ul>
            <li></li>
        </ul>
    2.显示数字序号 order
        <ol>
            <li></li>
        </ol>
    3.分层缩进
        <dl>
            <dt>ttt</dt> 不缩进
            <dd>ddd</dd> 缩进
            <dd>ddd</dd>
            <dd>ddd</dd>
            <dt>ttt</dt>
            <dd>ddd</dd>
            <dd>ddd</dd>
            <dd>ddd</dd>
        </dl>

4.表格

    <table border="1">
        <!--一行-->
        <tr>
            <td>第一行,第一列</td>
            <td>第一行,第二列</td>
            <td>第一行,第三列</td>
        </tr>
        <tr>
            <td>第二行,第一列</td>
            <td>第二行,第二列</td>
            <td>第二行,第三列</td>
        </tr>
    </table>

=====================修饰/功能标签end=======================
```

### 简易实现一个socket服务端 模拟http操作

    参考http_sample

    这个例子是为了演示浏览器请求网页 服务端接收后返回数据并断开的操作