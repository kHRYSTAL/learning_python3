## jQuery 使用
[http://jquery.cuishifeng.cn/](http://jquery.cuishifeng.cn/)

    jQuery是一个类库 是对javascript, DOM/BOM的封装
    用于快速开发 快速达到页面动效
    主要用于
        1. 查找元素
            DOM中只有10个左右的选择器
            jQuery 有各种各样的选择器用于查找标签和元素, 免去遍历的麻烦

        2. 操作元素



### 使用jQuery
[下载地址](https://code.jquery.com/jquery/)

    1.版本
        1.x 兼容性更好 (推荐使用1.12)
        2.x 忽略低版本IE
        3.x

        调用jQuery的api
            1.jQuery.xxx
            2.$.xxx
        $("#i1")[0] 相当于document.getElementById("i1") jQuery获取的对象是一个列表 应取[0]
            console.log($("#i1")); //[div#i1, context: document, selector: "#i1"]
            console.log($('#i1')[0].innerText);

    2.对象转换
            console.log($('#i1')[0] === document.getElementById("i1")); //true

            console.log($(document.getElementById("i1"))); // [div#i1, context: div#i1]
            console.log($('#i1')); // [div#i1, context: document, selector: "#i1"]

        将dom对象转换为jQuery对象
        var tag = document.getElementById('i1');
        var jquertTag = $(tag);

        参考s1.html

    3. 层级筛选器
        1. 通过id获取
            $('#id')
        2. 通过class获取
            $('.c1')
        3. 通过标签获取
            $('div')
        4. 获取多类型标签(组合选择器) 使用逗号
            $('#id, .c1, div')

        5. 找到i1标签下的所有a标签 使用空格
            $('#i1 a')

        6. 找到i1下的儿子a标签(没有中间标签) 使用">"
            $('#i1>a')

        7. 找到label后的所有input兄弟标签(同层) 使用"+"
            $("label + input")

        8. 找到label的下一个兄弟input标签 使用"~"
            $("label ~ input")

    4. 基本筛选器
        1. 找到第一个li标签 ":first" 最后一个":last"
            $('li:first');
           找到class=c1下所有a标签的第一个
            $('.c1>a:first')

        2. 奇数 偶数 :even :odd

        3. 通过索引值查找"eq(index)" 从0开始

            <table>
              <tr><td>Header 1</td></tr>
              <tr><td>Value 1</td></tr>
              <tr><td>Value 2</td></tr>
            </table>

            $("tr:eq(1)")

        4. 大于 小于索引数 :gt(index) :lt(index)

    5.
        1.属性选择器 重要
            <div keyname='khrystal'></div>
            <div keyname='matt'></div>
            根据属性名称查找标签
            $('[keyName]') 列表
            根据属性key和value查找标签
            $('[keyName="matt"]')

            找到所有type=text的input标签
            $('input[type="text"]')

        2. disabled enabled 不可编辑与可编辑属性

            找到所有不可编辑的标签
            <input type="text" disabled></input>

            $(':disabled')

        3. 表单相关
            $(":checkbox") 查找input type=checkbox的标签


    6. jQuery操作

        1.prop
            获取在匹配的元素集中的第一个元素的属性值。
            或设置元素集的属性

            参考s2.html
        2.each
            批量循环
            参考s2.html

        3.三元运算
            var v = 条件 ? 真值 : 假值


[更多参考](http://jquery.cuishifeng.cn/)