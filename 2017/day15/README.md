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

    版本
        1.x 兼容性更好 (推荐使用1.12)
        2.x 忽略低版本IE
        3.x

    调用jQuery的api
        1.jQuery.xxx
        2.$.xxx
    $("#i1")[0] 相当于document.getElementById("i1") jQuery获取的对象是一个列表 应取[0]
        console.log($("#i1")); //[div#i1, context: document, selector: "#i1"]
        console.log($('#i1')[0].innerText);

    对象转换
            console.log($('#i1')[0] === document.getElementById("i1")); //true

            console.log($(document.getElementById("i1"))); // [div#i1, context: div#i1]
            console.log($('#i1')); // [div#i1, context: document, selector: "#i1"]

        将dom对象转换为jQuery对象
        var tag = document.getElementById('i1');
        var jquertTag = $(tag);

        参考s1.html