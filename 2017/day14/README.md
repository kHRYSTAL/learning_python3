## javascript的作用域

#### html css补充

    1.body 可以设置背景图
        参考s1.html

    2.position
        fixed - 永远固定在页面的某个位置
        relative - 定义子标签相对当前标签布局, 只写这一个属性没有用
        absolute - 相对于父标签relative布局使用
                    单独使用时 页面初始化是在指定位置 当滑动页面是就不在了 会跟随页面滑动

    3.实现一个管理后台菜单布局
        参考s2.html 滚轮通过fixed实现
        参考s3.html 滚轮通过absolute实现

#### javascript补充

    1.序列化

        pyton中的 序列化 和 反序列化 可以用 json或pickle

        js中的序列化可以用JSON.stringify(arg) 将对象序列化成字符串
            反序列化可以使用JSON.parse(string) 将字符串反序列化成对象

    2. 转义

        如url中不允许存在中文 可以使用转义的方式

        再如 cookies存储
            第一次登录服务器 服务器发送一个字符串当作cookie 客户端js接收后转义字符串并持久化存储
            之后客户端携带cookie 请求服务器 免登录

        支持的api:

        decodeURI( )                   URl中未转义的字符 (将编码后的字符串解码成中文)
        decodeURIComponent( )   URI组件中的未转义字符(解码中文, 特殊字符(: /))
        encodeURI( )                   URI中的转义字符 (将中文编码)
        encodeURIComponent( )   转义URI组件中的字符 (将中文, 特殊字符(: /)编码)
        escape( )                         对字符串转义
        unescape( )                     给转义字符串解码
        URIError                         由URl的编码和解码方法抛出


        模拟点赞操作, 发送请求时携带客户端cookies 使服务器认为帐号是登录状态
            实际上这是一个爬虫操作
        参考 s10.py


    3. eval()
       exec()

       在python中 eval可以把字符串解析为表达式, exec可以把字符串解析为代码
       但没有返回值
        python:
            value = eval("1+1") 得到value = 2
            s = "8*8"
            value = eval(s)
            exec("执行代码")

       在js中eval相当于 eval和exec的合集 使用eval可以执行代码和表达式
            eval("1+1")
            eval("执行代码")


    4. 时间

        Date对象
        var d = new Date() 创建一个时间对象

        d.getMinutes() 获取分钟
        n = d.getMinutes() + 5
        d.setMinutes(n) 增加5分钟

# Javascript 作用域

    1.!!!!python/js是以函数为作用域的 即函数内部有条件语句 条件语句中的变量函数内部都可以使用

        def func():
            if(true):
                name = 'khrystal'

            print(name) # 以函数为作用域


        function func(){
            if(true) {
               var name = 'khrystal';
            }

            console.log(name); // 以函数为作用域

        }


      在java c# 等语言是以方法块为作用域的

        public void func() {
            if(true) {
                name = "khrystal";
            }

            System.out.println(name); // 报错 不能调用到
        }

    2. 函数中变量的作用域在函数未被调用之前, 就已经创建
        在编译时期,
        还没有调用func, name作用域就已被创建

        function func() {
            if(1==1){
                var name = 'khrystal';
            }
            console.log(name)
        }

    3. 函数的作用域存在作用域链, 并且也是在函数调用之前创建
        xo = 'khrystal';
        function func() {
            var xo = 'eric';
            function inner() {
                var xo = 'tony';
                console.log(xo);
            }
            inner();
        }

        func(); // 输出tony


        ////////////////////////////

        function func() {
            var xo = 'eric';
            function inner() {
                console.log(xo);
            }
            return inner
        }

        ret = func(); // 返回inner函数
        // 由于函数创建时变量作用域就确定了, inner中的xo 作用域链就定义好了,
        // xo在inner中没找到 会根据作用域链找到外部的eric

        ret(); // 执行inner 输出eric

        ///////////////////////////

        function func() {
            var xo = 'eric';
            function inner() {
                console.log(xo);
            }
            var xo = 'tony';
            return inner
        }

        ret = func(); // 返回inner函数
        // 创建函数时 就创建了作用域 函数从上到下执行
        // 外部xo的地址从eric修改为了tony
        ret(); // 执行inner 根据作用域链找到xo中的变量 但这个变量已经改为tony


        参考s5.html
        注: 结合最后的词法分析 与作用域(链)结合 可以得到结论


    4. 函数内部局部变量提前声明 参考最后的词法分析

        function func() {
            console.log(x)
            var x = 'khrystal' // 如果不写这句 程序直接报错
        }

        func(); // 输出undefine

        这句代码说明变量提前声明
        相当于
        function func() {
            var x;
            console.log(x);
            x = 'khrystal';
        }

        说明js解释器在函数中不仅会创建作用域
        会找到函数中的所有的局部变量提前声明, 并不赋值

        注意 千万不要把js作用域和java的内部类持有外部引用混淆
        两者不是同一个概念, 因为java内部类可以修改外部引用
        而作用域是只在自己的函数中有效 内部函数不能修改!

        name="lwy";
        function t(){
            var name="tlwy";
            function s(){
                var name="slwy";
                console.log(name);
            }
            function ss(){
                console.log(name);
            }
            s();
            ss();
        }
        t();

        输出为slwy
             tlwy
        ss变量作用域流程 ss()->t()->global name, 因为t中有name 不会再向上找了

# Javascript 面向对象

    关键字this

    function foo(n) {
        this.name = n;
        this.sayName = function() {
            console.log(this.name);
        }
    }

    // 创建对象
    var obj1 = new foo('matt');

    obj1.name;
    obj1.sayName(); 执行对象中的函数
    var obj2 = new foo('khrystal');
    obj2.name;

    1. this 代指对象 相当于python的self
    2. 创建对象时 使用new 函数() 等于创建一个对象

    3. 与python不同的是 js中对象的函数冗余了, 每个对象都包含了一个sayName函数
        在python中 如果一个对象中包含一个函数 会把这个函数抽离单独放到内存中
        这也是为什么python每个对象函数都需要self参数的原因

        因此 为了减少冗余 应该把sayName函数从对象函数中抽离出来:
        这就是函数的原型


        fuction Foo(n) {
            this.name = n;
        }

        // 定义Foo类的原型 只创建一次
        Foo.prototype = {
            'sayName': function(){
                            console.log(this.name)
                        }
        }

        // 解释器从上到下执行 会指定sayName到类中 且只创建一次

        var obj = new Foo('matt');
        obj.sayName();

        //解释器 会先到对象中找方法名, 如果不存在 会到原型中去找, 如果还不存在, 会报错TypeError

# DOM操作补充

### 设置自定义属性

    var obj = document.getElementById("i1");
    // 设置自定义属性
    obj.setAttribute("key", "value");

    // 获取自定义属性
    var value = obj.getAttribute("key");

    // 删除属性
    obj.removeAttribute("key");

    // 获取所有属性 字典
    obj.attributes

### 其他操作

    1.创建标签:
        1.以字符串创建
        2.以标签对象创建

        注:jQuery 没有提供创建标签的api 需要使用document

    参考s8.html

    2.提交表单
        // 在function中调用获取表单对象提交 任何控件点击事件都可以调用这个function
        document.getElementById("id").submit()

    3. 对话框

        1.alert("");
        2.var v = confirm(""); // v = true 确认或 false取消

    4. 页面url操作

       var url = location.href; // 获取当前url
       location.href = "http://www.baidu.com" 重定向跳转
       location.href = location.href; // 刷新
       location.reload(); // 刷新

    5. 定时器操作
        1. setInterval(function, time); 按照时间间隔执行 一直执行
            var obj = setInterval(function(){}, 5000) // 5秒钟执行一次函数
            clearInterval(obj); // 清除定时器 定时器不再执行

            // 要求定时器执行一次后停止
            var obj = setInterval(function(){
                console.log(1);
                clearInterval(obj);
            }, 1000);

        2. setTimeout(function, time); 延时多少毫秒后执行, 指执行一次

            // 1秒后执行
            var obj = setTimeout(function(){
                console.log("timeout");
            }, 1000);


            clearTimeout(obj); //在延时期间内终止定时器

            参考s10

### DOM 事件操作

    1. onblur
        失去焦点

    2. onfocus
         得到焦点

    3. onclick
        点击

    4. onmouseouer onmouseout
        行为 样式 结构分离
        参考s11, s12, s13


    绑定事件的三种方式
        1. 标签中onClick="tagOnClock();"
            1.1 在function中传递标签对象
                标签中onClick="tagOnClick(this);"

        2. script中 document.getElementById("id").onclick=function(){
                // this 指当前触发事件的标签对象
                this.style.backgroundColor="red";
            };

        3. addEventListener("click", function(){}, false)
            // 这种方式可以针对事件重复添加触发函数, 事件触发时
            // 调用的函数都会执行 而不会被覆盖 也就是说 上面两种方式是set覆盖的
            // 这种方式是add 重复叠加的
            参考s14.html

            对于第三个参数 true表示捕捉 false表示冒泡
                捕捉表示从最根部default->document->html->body->父标签->子标签
                依次遍历去捕获事件

                冒泡则相反 从子标签向根部去捕获事件
            默认不写为false, 冒泡
            参考s15.html


### 词法分析(重点)

     function t1(age) {
            console.log(age); // 输出function
            var age = 27;
            console.log(age); // 27
            function age() {

            }
            console.log(age);// 27
        }

     t1(3);

     分析流程 active object 简称AO
        1.形式参数
        2.局部变量
        3.函数内声明表达式 function age(){}

    以下均在词法分析阶段 并不是执行阶段
    1.形式参数
        AO.age = undefine
        分析到实际参数为3
        AO.age = 3
    2.局部变量
        分析存在局部变量age, 但是因为在分析阶段不是执行阶段 会重新定义成undefine
        AO.age = undefine;
    3.函数内声明表达式
        AO.age = function age // 函数内声明表达式在词法分析中优先级最高

    结论 当变量名称相同时 在词法分析中
        函数内声明表达式优先级最高(高于形參赋值与局部变量声明)
        形參赋值与变量声明按照代码顺序赋值


    执行阶段:
        传递词法分析阶段的结果AO.age=function age至t1 输出;
        age赋值为27 输出
        由于function age在词法分析阶段已经声明 跳过
        输出27

    参考s16.html

### 快捷键补充

    table>tr*3>td*3 + tab 键快速创建3行3列表格
    div.test 快速创建class为test的标签
    div.test#test 创建class为test, id为test的标签


    div.test{aaa} 内容为aaa
    table>tr*3>td*3>{aaa}
    table>tr*3>td*3>{aaa$} #内容为aaa1,aaa2,aaa3

    c 生成注释

















