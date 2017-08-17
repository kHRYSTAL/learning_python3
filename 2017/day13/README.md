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
        }

        执行函数
            函数名(1, 2, 3);