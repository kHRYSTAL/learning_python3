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

        4.$(this).next()
            获取当前标签的下一个标签
          $(this).nextAll()
            获取当前标签后续的所有同级标签
          $(this).nextUntil('#i1')
            带条件 获取直到指定标签的所有标签
            参考s3.html
        5.$(this).prev()
            $(this).prevAll()
            $(this).prevUntil()
            获取当前标签的上一个标签
        6.$(this).parent()
            获取当前标签的父标签
          $(this).parents()
            获取所有祖先标签
          $(this).parentsUntils(".c1")
            获取直到class=c1为止的所有祖先标签

        7.$(this).children()
            获取当前标签的子标签集合

        8.获取兄弟标签 不包括自己
            $('#i1').siblings()
            参考s4.html

        9. addClass() removeClass()
            增加删除class 不需要加"."

        10. $(this).find(".content")
            获取当前标签下 包含class=content的子标签

        11. $(this).hasClass("class")
        12. $(this).eq(index|-index)

        13. $("#i2").toggleClass("hide");
            如果没有class则添加如果有则移除

    7. 文本内容操作

        $().text() #获取文本
        $().text("xsssd") # 设置文本内容
        如果包含html不解析
        $().html() # 获取html
        $().html("<A>ASASDD</A>") # 设置html
        如果包含html 解析

        // input 系列 textarea
        var value = $("#i2").val()
        $("#i2").val("设置的值")

        参考s7.html

    8. 属性操作
        $().attr()
            用于操作自定义属性

            获取#i1标签type的值
            $("#i1").attr('type');

            设置属性 如果重复会被覆盖
            $('#i1').attr('name', 'khrystal');

            删除属性
            $('#i1').removeAttr('name');

        $().prop()  专门用于checkbox, radio
            因为在jQuery 3.x版本以下使用attr属性控制不彻底 存在bug
                 $('#i1').attr('checked', 'checked'); 选中
                 $('#i1').removeAttr('checked'); 取消选中
                 再执行选中 就不执行了

             获取在匹配的元素集中的属性值。
             或设置元素集的属性
                $('#i1').prop('checked'); 获取值
                $(':checkbox').prop('checked', true); 将每一个checkbox遍历设置值
                $('#i1').prop('checked', true); 设置值


             参考s2.html


#### demo

    1. 使用attr自定义属性实现模态框优化
        参考s8.html

    2. 使用自定义属性实现 tab菜单切换
        主要练习 attr siblings click
            siblings指除自己外的所有兄弟标签
            click是遍历设置点击事件
            children是子标签 可以加过滤参数
        参考s9.html

    3. 使用索引实现 tab菜单切换
        主要练习 .index() 获取自己是一组序列中的第几个
                通过索引值查找"eq(index)" 从0开始
        参考s10.html

    4. 文档处理 append 从标签内追加内容或对象
            // 添加到标签内尾部
            $('#u1').append(html);
            // 添加到标签内顶部
            $('#u1').prepend(html);
            // 添加到标签外后方
            $('#u1').after(html);
            // 添加到标签外前方
            $('#u1').before(html);
            参考s11
    5. 文档处理 删除与清空 复制
            .remove() 删除标签内容
            .empty() 清空标签内容
            .clone() 克隆标签
                var cloneTag = $('#u1').children().eq(index).clone();
                $('#u1').append(cloneTag);
            参考s12

    6. css处理
        $('').css('样式名称', '样式value');
        练习 .css setInterval 创建标签 移除标签 移除定时器
        例子: 点赞处理
        参考s14.html

    7. 位置与尺寸
        scrollXXX
            获取滚动距离窗体顶部距离
            $(window).scrollTop()
            获取滚动距离div顶部距离
            $('div').scrollTop()
            返回创图顶部
            $(window).scrollTop(0);
            返回div顶部
            $('div').scrollTop(0);
            ...
            $('div').scrollLeft(0);

        offset()
            指定标签在html(root布局)中的坐标
            $('#l1').offset()
            $('#l1').offset().left
            $('#l1').offset().top

            参考s16.html

        position()
            指定标签相对于父标签(relative)的坐标

        height()
            获取标签高度 纯高度
        innerHeight()
            边框+纯高度
        outerHeight()
        outerHeight(true)
        纯高度 边框 外边距 内边距


    8. 绑定事件

        DOM 中有三种绑定方式: onclick="function..", tag.onclick=function(){};, addEventListener.

        在jQuery中:
            1.  $('.c1').click(...)

            2.  $('.c1').bind('click', function(){}) 绑定
                $('.c1').unbind('click', function(){}) 解除绑定

            3.  对class=c1下的所有a标签绑定事件
                $('.c1').delegate('a', 'click', function(){})
                解绑
                $('.c1').undelegate('a', 'click', function(){})

                这种方式有特殊的功能
                参考s17.html

            4.  $('.c1').on('click', function(){}) 绑定
                $('.c1').off('click', function(){}) 解绑





[更多参考](http://jquery.cuishifeng.cn/)