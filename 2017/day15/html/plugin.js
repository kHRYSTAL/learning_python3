/**
 * Created by kHRYSTAL on 17/8/30.
 */
// 自执行函数 也就是立即执行函数 作用有两点
// 1 让编译器立即执行函数中的代码
// 2. 隔离作用域 如status 如果不是立即执行函数 那么status就成为全局变量了 会导致冲突
(function ($) {

    var status = 1;

    $.extend({
        'pluginExtendFunction': function () {
            return "这是自定义扩展方法"
        }
    });

    $.fn.extend({
        'pluginSelectorFunction': function () {
            return "这是自定义扩展筛选器调用方法 "
        }
    });
})($);

// 加上();就是执行函数 参数为$为jQuery对象

