### start html&css

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

### 简易实现一个socket服务端 模拟http操作

    参考http_sample

    这个例子是为了演示浏览器请求网页 服务端接收后返回数据并断开的操作

#### html 标签 s1~s9

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

    规范写法
        <table border="1">
        <!--表头-->
            <thead>
                <tr>
                    <th>表头1</th>
                    <th>表头2</th>
                    <th>表头3</th>
                    <th>表头4</th>
                </tr>
            </thead>
            <!--表体-->
            <tbody>
                <tr>
                    <th>表体1</th>
                    <th>表体2</th>
                    <th>表体3</th>
                    <th>表体4</th>
                </tr>
            </tbody>
        </table>

    合并单元格
            <tr>
                <td>表体1</td>
                <!--占两列-->
                <td colspan="2">表体2</td>
                <td>表体4</td>
            </tr>

            <tr>
                <!--占两行-->
                <td rowspan="2">表体1</td>
                <td>表体2</td>
                <td>表体4</td>
            </tr>

5. label 用于input控件获取焦点 行内标签

    <label for="username">用户名:</label>
    <input type="text" name="user" id="username">

6. fieldset 不常用 实现文字框包裹内容





=====================修饰/功能标签end=======================
```

#### css s10~

    在标签上设置style属性 如:
    <div style="background-color: #2459a2; height: 48px;">1</div>

    style的重用
    1.head中的id选择器 通过找到标签的id设置style 并不常用 因为id不允许重复
        <head>
        <meta charset="UTF-8">
        <title>Title</title>
        <style>
            #i1, #i2, #i3{
                background-color: #2459a2;
                height: 48px;
            }
        </style>
        </head>
        <body>
            <div id="i1">1</div>
            <div id="i2">2</div>
            <div id="i3">3</div>
        </body>


    2. ################################################
        常用 class选择器 通过找到标签的class设置标签的style
            常用, 允许重复
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
            <style>
                .c2 {
                    background-color: rebeccapurple;
                    height: 20px;
                }
            </style>
            </head>
        <body>
            <div id="i1">1</div>
            <div class="c2">2</div>
            <div id="i3">3</div>
        </body>

    3.标签选择器 用于通用标签style设置
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
            <style>
                div{
                    background-color: black;
                    color: white; /** 这里的color 其他的选择器并没有设置 因此color会实现 但是background因为优先级被其他选择器覆盖*/
                }
            </style>
        </head>
        <body>
            <div id="i1">1</div>
            <div class="c2">2</div>
            <div class="c2">3</div>
        </body>

    4.关联选择器
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
            <style>
                span div{
                    background-color: aqua;
                    color: #cdcdcd;
                }
            </style>
        </head>
        <body>
            <span>asasasasd
                <div>sadsadasd</div>
                sdasdasd
            </span>
        </body>

        ------------------ 层级选择器 c2下的c3下的div
        <head>
        <style>
            .c2 .c3 div{
                background-color: aqua;
                color: #cdcdcd;
            }
        </style>
        </head>
        <body>
            <div class="c2">
                <span class="c3">asasasasd
                    <div>sadsadasd</div>
                    sdasdasd
                </span>
            </div>
        </body>

    5. 组合选择器
        #i1, #i2, #i3 {
               xxx
        }

        #i1, .c1, div {
            xxx
        }

    6. 属性选择器
        找到type为text的input标签
        input[type="text"]{width:100px; height:200px;}
         /*bbb为自定义属性 相当于自定义k-v*/
        input[bbb='asd']{background-color: #333333}
         /*c1可以进行一次style设置 然后根据标签的属性再进行一次筛选*/
        .c1 [bbb='asd']{background-color: #333333}

##### style的优先级
    优先级 如果标签上有style 则style优先
    head里有多个style, 标签均使用了, 则为并集使用style
        重复的属性按照就近原则使用(相同属性使用靠下的属性)

##### 导入css

    <head>
        <meta charset="UTF-8">
        <title>Title</title>
        <!--导入css-->
        <link rel="stylesheet" href="commons13.css">
    </head>
    <body>
        <div class="c1 c2">asasasa</div>
    </body>

##### 其他css 配置

    1.边框 可以加到所有body的标签中
        <div style="border: 1px solid red;">asasas</div>
        <div style="border: 1px dotted red;">asasas</div>
        <div style="border-left: 10px dotted red;">asasas</div>

        <div style="height: 48px;width: 200px;border: 1px solid pink">asasas</div>

    2.float

        浮动属性 块级标签合并一行
        <!--从左向右绘制 屏幕宽度的20%-->
        <!--从左向右绘制 屏幕宽度的20%-->
        <div style="width: 20%; background-color: red; float: left">1</div>
        <!--从右向⬅️绘制 屏幕宽度的80%-->
        <div style="width: 80%; background-color: black; float: right">2</div>

        <!--注意 如果相加超过100% 会另起一行 不会叠加-->

        <!-- 由于子标签float 父标签没有float 会导致父控件压不住 需要加这句话 意思是让父标签包裹所有子标签-->
        <div style="clear: both;"></div>
        参考s15

    3.height width line-height color font-size font-weight
        <!--屏幕宽度的80%-->
        <div style="height: 48px;width: 80%;border: 1px solid pink">asasas</div>

        <br/>
        <!--文字水平居中-->
        <div style="height: 48px;width: 80%;border: 1px solid pink; font-size: 16px;text-align: center">asasas</div>
        <br/>
        <!--垂直方向居中 根据height高度居中-->
        <div style="height: 48px;width: 80%;border: 1px solid pink; font-size: 16px;text-align: center; line-height: 48px">asasas</div>

        <br/>
        <!--文字加粗-->
        <div style="height: 48px;
            width: 80%;
            border: 1px solid pink;
            font-size: 16px;
            text-align: center;
            line-height: 48px;
            font-weight: bold">asasas</div>

    4.display 用于块标签与行内标签转换

         <div style="background-color: red; display: inline">块标签</div>
         <span style="background-color: black; display: block; color: white"> 行内标签</span>

         ### 注意 行内标签(<span><a>)无法设置高度/宽度/间距/内边距
         ### 块级标签可以, 块级标签默认占父级标签的100%
         ### 可以使用display: inline-block 使标签即具有行内标签属性也具有block标签属性
             设置这个属性 行内标签就支持宽度/高度margin/padding
         ### display:none 为让标签消失 以后会经常用 用于控制控件的隐藏和显示

         参考s16.html

    5.padding margin(0, auto)

        margin 外边距
            margin-top
            margin-bottom
            margin-left
            margin-right
        padding 内边距
            padding-top
            padding-bottom
            padding-left
            padding-right

        style="margin: 0 auto;" 上下间距是0 左右间距根据屏幕剩余宽度平均分割

        参考s17.html


##### 问题

    1. 页面在浏览器调整大小后变形:

        应在最外层div写上绝对宽度 当浏览器宽度小于绝对宽度后 会出现滚动条
        再次, 设置margin:0, auto 两侧间距宽度自适应平均分配 这样在浏览器宽度
        小于屏幕宽度且大于绝对宽度时 可以不显示滚动条压缩margin宽度

    2. 页面的自适应

        后面会说, head 的style里可以加判断 在宽度小于多少时 某些style不生效
        @media(min-width=768px)
        {
            display:none;
        }

    3. <a><img></img></a> 在ie浏览器有蓝色边框 如何去掉?

        需要设置
        img {
            border:0;
        }


##### css的补充

        1. position
        fixed 相对于屏幕的上层的固定位置
        页面上某些控件不管页面滑动到什么位置 永远固定在浏览器的某个可见位置
        如 菜单/返回按钮/返回顶部按钮等等

        这时需要用到position: fixed

        <body>
            <!--position: fixed 表示标签固定在某个位置 页面滑动不跟随滚动 实现层叠样式-->
            <!--top bottom left right 表示position后 距离上下左右的高度-->
            <div style="width: 50px;height: 50px; background-color: black; color: white;
            position: fixed;
            right: 20px;
            bottom: 20px;
            ">
                返回顶部
            </div>
            <div style="height: 5000px; background-color: #dddddd;"></div>
        </body>

        2. absolute 相对于 relative父标签的上层的固定位置
            <!--position: absolute 表示标签固定在首屏某个位置 页面滑动也会跟随滚动 实现层叠样式 与position: relative结合使用-->
            <!--top bottom left right 表示position后 距离上下左右的高度-->
            <!--常用于页面点赞时 点赞动画所在的标签是子标签 使用position:absolute ,
                父标签使用 position: relative 表示内部的position是相对于自己的位置
            跟随item显示在某个相对item的位置-->

            <!--fixed是相对屏幕固定的位置-->
            <!--position: absolute是相对于position: relative的绝对位置-->


           <div style="position: relative; width: 980px; height: 1000px; margin-top: 100px; background-color: red">
               <!--子标签相对于父标签固定位置 且在父标签上层-->
               <div style="background-color: green; position: absolute; top: 200px; left: 100px">asdf</div>
           </div>


        3. 遮罩 实际上有三层 最底层是正常页面 中间层是遮罩 最上层是类似dialog的控件

                <!--遮罩上的对话框-->
                <div style="position: fixed; background-color: white;
                    /* z轴高度 越大越在上层 */
                    z-index: 10;
                    height: 400px;
                    width: 500px;
                    top: 50%;
                    left: 50%;
                    /*绘制是从左上角开始的 因此需要将这个标签居中处理*/
                    margin-top: -200px;
                    margin-left: -250px;
                    "></div>
                <!--遮罩-->
                <div style="position: fixed; background-color: black;
                    z-index: 9;
                    top: 0;
                    bottom: 0;
                    right: 0;
                    left: 0;
                    /*opacity 表示透明度 0为全透明 1为不透明*/
                    opacity: 0.5;"></div>
                <div style="height: 5000px; background-color: green">asasasas</div>

            参考s21.html

        4. overflow 属性

            <!--overflow: hidden 超出的范围隐藏-->
            <div style="width: 50px; height: 50px; overflow: hidden">
                <img src="1.jpeg">
            </div>
            <br/>
            <!--overflow: auto/scroll 超出的范围支持滚动-->
            <div style="width: 50px; height: 50px; overflow: auto">
                <img src="1.jpeg">
            </div>
            <br/>
            <!--正常操作-->
            <div style="width: 50px; height: 50px;">
                <img src="1.jpeg" style="width: 50px; height: 50px">
            </div>

            参考s22.html

        5. hover属性 鼠标移动到指定标签上的事件
            当鼠标移动到标签时 以下css生效
            /* hover 鼠标移动到这个标签上 样式会发生变化 */
            .pg-header .menu:hover {
                background-color: blue;
            }

            参考s23.html

        6. 设置背景图片

            background-image:url('1.jpeg');
            图片为自身大小 如果div宽高大于图片宽高, 则图片重复放置

            重复放置方式
            background-repeat: repeat-y y轴重复放置

        7.  background-position-y 移动背景图

            <div style="background: url('2.png') no-repeat;border: 1px solid red; height: 18px; width: 20px;"></div>
            <!--背景图的y轴向上移动-->
            <div style="background: url('2.png') no-repeat;border: 1px solid red; height: 18px; width: 20px;
                background-position-y: -20px;"></div>
            <div style="background: url('2.png') no-repeat;border: 1px solid red; height: 18px; width: 20px;
                background-position-y: -40px;"></div>
            <div style="background: url('2.png') no-repeat;border: 1px solid red; height: 18px; width: 20px;
                background-position-y: -60px;"></div>

            <!--优化写法 最后两个值表示x y轴偏移量-->
            <div style="border: 1px solid red; height: 18px; width: 20px;
                background: url('2.png') no-repeat 0 -80px;"></div>

            参考s25.html

        8. 实现登陆框
            <!-- 内部position使用相对布局 -->
            <div style="width: 400px; height: 35px;  position: relative">
                <!--使用 position: absolute 相对于父容器位置-->
                <span style="background: url('login.png') no-repeat;height: 16px; width: 16px; display: inline-block;
                    position: absolute; right: 10px; top: 10px;
                    "></span>
                <input style="width: 370px; height: 100%; padding-right: 30px"/>
            </div>

            参考s26.html






