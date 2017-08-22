### start javascript

    js是一门独立的语言
    浏览器就是js代码的解释器


#### javascript 代码的存在形式

    一般存在于html中

    <input type="text" id="user">
    <input type="button" value="点击" onclick="getData()">

    <script>
        function getData() {
            var a = document.getElementById("user");
            alert(a.value)
        }
    </script>

    js一般都是让页面动起来的操作
    由于js通过http引入时放在head中 会导致js没有加载完 页面无法展现
    因此建议把js引入操作放到body的最下方 增强用户体验
    但是也要考虑场景

#### 代码注释

    //
    /**/
#### 变量

    声明变量
    python
        name = 'khrystal'
    javascript
        name = 'khrystal' 默认为全局变量
        var name = 'khrystal' 默认为局部变量
#### 基本数据类型

    空值 null

    数字
        a = 18
        a = 1.8
    字符串

        obj.length                           长度
        obj.trim()                           移除空白
        obj.trimLeft()
        obj.trimRight)
        obj.charAt(n)                        返回字符串中的第n个字符
        obj.concat(value, ...)               拼接
        obj.indexOf(substring,start)         子序列位置
        obj.lastIndexOf(substring,start)     子序列位置
        obj.substring(from, to)              根据索引获取子序列
        obj.slice(start, end)                切片
        obj.toLowerCase()                    大写
        obj.toUpperCase()                    小写
        obj.split(delimiter, limit)          分割
        obj.search(regexp)                   从头开始匹配，返回匹配成功的第一个位置(g无效)
        obj.match(regexp)                    全局搜索，如果正则中有g表示找到全部，否则只找到第一个。
        obj.replace(regexp, replacement)     替换，正则中有g则替换所有，否则只替换第一个匹配项，
                                             $数字：匹配的第n个组内容；
                                             $&：当前匹配的内容；
                                             $`：位于匹配子串左侧的文本；
                                             $'：位于匹配子串右侧的文本
                                             $$：直接量$符号

    数组 相当于python的列表

        obj.length          数组的大小
        obj.push(ele)       尾部追加元素
        obj.pop()           尾部获取一个元素
        obj.unshift(ele)    头部插入元素
        obj.shift()         头部移除元素
        obj.splice(start, deleteCount, value, ...)  插入、删除或替换数组的元素
                            obj.splice(n,0,val) 指定位置插入元素 删除为0 等于在这个位置插入
                            obj.splice(n,1,val) 指定位置替换元素 删除后在当前位置插入等于替换
                            obj.splice(n,1)     指定位置删除元素
        obj.slice( )        切片
        obj.reverse( )      反转
        obj.join(sep)       将数组元素连接起来以构建一个字符串
        obj.concat(val,..)  连接数组
        obj.sort( )         对数组元素进行排序

    字典

        a = {'k1':'v1', 'k2':'v2'}
        a['k1']
        a['k2']

    布尔
        true 真
        false 假
        布尔类型仅包含真假，与Python不同的是其首字母小写。

        ==      比较值相等 1 == "1" true
        !=       不等于
        ===   比较值和类型相等 1 === "1" false
        !===  不等于
        ||        或
        &&      且

        switch(i) {
            case x:
                console.log('123');
                break;
            case y:
                break;
            default:
                break;

        }

#### 语法

    条件
        if (条件) {

        } else if {

        } else {

        }



    循环

        var a = [11, 22, 33, 44];
        for(var i in a) { // i 为 index
            console.log(a[i]);
        }

        for(var i=0; i< a.length; i++) { // 类似java的for循环
            console.log(a[i])
        }

        var b = {'k1':'v1', 'k2':'v2', 'k3':'v3'}
        for (var i in b) { // i 为 key
            console.log(b[i])
        }

        continue;
        break;

        while(条件) {

        }


    定时器: 每多少秒执行一次
            setInterval("执行的代码", 间隔时间)
        <script>
            //第一个参数表示要执行什么 string或func 第二个参数表示延时 单位毫秒 即每多少毫秒执行一次
            //  setInterval("alert(123);", 5000)
            function f1() {
                console.log('aaa')
            }
            setInterval("f1();", 5000)
        </script>

    获取标签内容
        <div id="i1">asdfghjk</div>
        <script>
            var tag = document.getElementById("i1");
            var text = tag.innerText
            console.log(text)
        </script>

    设置标签内容 tag.innerText = "xxx"

    实现一个跑马灯: 参考s4.html

    函数:
        括号中为形參
        function 函数名(a, b, c) {
            ...
            return 返回值
        }

        执行函数
            函数名(1, 2, 3);



#### Dom操作

    Dom将整个html转换为文档对象 这样dom就能通过特定的标记获取指定的标签

    这样就能够进行删除 修改内容 修改属性等操作 就能让页面动起来

    1.Dom 直接选择器 直接找到指定的一个或一组标签

        步骤:
            1.找到标签

                document.getElementById('id')
                通过id获取标签
                由于整个html中id不能重复
                因此这种方式获取的标签最多只有一个

                document.getElementsByTag('div')
                通过标签类型获取标签
                这样获取的标签是一个列表

                document.getElementsByClassName('classname')
                通过classname获取标签
                这样获取的标签是一个列表

                document.getElementsByName('name')
                通过标签中name属性获取标签
                这样获取的标签是一个列表

                参考s6.html

    2. Dom 间接选择器 通过一个标签间接的找到另一个或一组标签

         步骤:
            1.找到一个标签对象
                var tag = document.getElementById('id')

            2. 通过这个标签对象获取与他有关系的标签
               支持的api:

                parentNode          // 父节点
                childNodes          // 所有子节点
                firstChild          // 第一个子节点
                lastChild           // 最后一个子节点
                nextSibling         // 下一个兄弟节点
                previousSibling     // 上一个兄弟节点

                parentElement           // 父节点标签元素
                children                // 所有子标签
                firstElementChild       // 第一个子标签元素
                lastElementChild        // 最后一个子标签元素
                nextElementtSibling     // 下一个兄弟标签元素
                previousElementSibling  // 上一个兄弟标签元素

                参考s7.html

    3. 操作标签
        1.innerText/innerHtml/value
            innerText:获取标签中的文本内容 忽略html标签内容
                        标签对象.innerText;

                        对标签内部文本进行重新赋值
                        标签对象.innerText = "xxx"; 不能设置html
                        如 innerText = "<a href="">asas<a>" 是不行的

            innerHtml: 包含标签内的文本和html标签文本

                        可以设置html

            value: 对input/select/textarea标签有效 获取和设置input标签中的内容


        2. className

            对标签设置classname
            tag.className = "c1";

            以列表形式获取className 结果为["c1"]
            tag.classList

            新增一个className
            tag.classList.add("c3");

            删除一个className
            tag.classList.remove("c1");

            通过className的设置可以进行模态对话框 展开菜单的设置
            如菜单: 点击展开的时候 对菜单中的一行增加className 只有这个className
            style效果是展开的

        3. style

            var obj = document.getElementById("i1");
            // 设置color
            obj.style.color="red";
            // 设置font-size
            obj.style.fontSize="16px";
            // 设置背景色
            obj.style.backgroundColor="red";


    例子

    1.实现模态框 输入后新增操作对话框实现
    全选 取消 反选
        获取checkbox是否选中
        checkbox.checked;

        设置checkbox选中或不选中
        checkbox.checked = true;
        checkbox.checked = false;
        参考 s8.html

    2.实现管理后台菜单
        参考 s9.html


#### jQuery 初试

    jQuery简化了Dom操作

    document.getElementById("id")
        $('#id')

    document.getElementsByClassName("c1")
        $('.c1')

    找到相邻标签
    $('.c1').siblings()






