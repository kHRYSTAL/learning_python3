### 补充以及后续路线
    1. js正则
        test    用于判断字符串是否符合规定的正则表达式, 只要内部含有就返回true
        exec    获取匹配的数据

        1. 创建正则表达式对象 需要使用/.../ 不需要加""
            如 匹配数字的正则:
                var reg = /^\d+$/; \d+表示字符串为全为数字 需要加开始和终止 否则只要包含就返回true
               判断
                reg.test("asdfg12"); 返回值为false

        2. 获取匹配数据
            var str = asdf_12_asdf_34;
            var reg = /\d+/;
            reg.exec(str) 由于惰性 所以只返回[12] 拿不到34

            2.1 分组 二级匹配
            var str = "JavaScript is more fun than Java or JavaBeans";
            var reg = /\bJava(\w+)\b/; ()表示分组, \b表示字母
            此时进行匹配, 会先进行整体匹配, 由于惰性, 只获取JavaScript, 然后再从匹配到的字符串中再获取括号中的内容
            结果为
            [JavaScript, Script]

            2.2 全局匹配
                在正则表达式尾部加g为全局匹配 非惰性:
                var str = "JavaScript is more fun than Java or JavaBeans";
                var reg = /\bJava\w+\b/g;
                // exec为迭代器匹配
                reg.exec(str); ["JavaScript"]
                reg.exec(str); ["Java"]
                reg.exec(str); ["JavaBeans"]
                reg.exec(str); null
                reg.exec(str); 重新一轮匹配, ["JavaScript"]

            2.3 分组+全局匹配
                var str = "JavaScript is more fun than Java or JavaBeans";
                var reg = /\bJava(\w+)\b/g;
                // exec为迭代器匹配
                reg.exec(str); ["JavaScript", "Script"]
                reg.exec(str); ["Java", ""]
                reg.exec(str); ["JavaBeans", "Beans"]
                reg.exec(str); null
                reg.exec(str); 重新一轮匹配, ["JavaScript", "Script"]

            2.4 其他
                /.../i 不区分大小写
                /.../m 多行匹配 注意 js正则本身默认就是多行匹配
                        加上m后 是为了解决有^存在的正则 同时字符串是多行, 检测多行的开头 而不是字符串的开头
                        如:
                        var str = "JavaScript is more fun than \nJava or JavaBeans"
                        var reg = /^Java(\w+)/g;
                        reg.exec(str); ["JavaScript", "Script"]
                        reg.exec(str);  null 此时返回为空 因为只会匹配这个str字符串整体开头为Java的部分
                                            后面都不会匹配 因为不是开头

                        解决方式
                        var str = "JavaScript is more fun than \nJava or JavaBeans"
                        var reg = /^Java(\w+)/mg;

                        reg.exec(str); ["JavaScript", "Script"]
                        reg.exec(str); ["Java", ""]
                        reg.exec(str); null 因为只匹配行的开头 不会匹配JavaBeans 因为不是行的开头








    2. 组件
        面临选择
            1. 所有页面自己实现重头开发
                优点 写完了能够知道全部实现
                缺点 重复造轮子

            2. 实现已经封装好的ui组件
                常用:BootStrap 包含css, js的封装
                    jQueryUI 包含css, js的封装
                    EasyUI ...

                都需要学习组件实现的规则

    3. web框架
        自己实现一个简易的web框架

    4. Django
        python实现web网站功能最齐全(orm, web, 模版等)的框架


