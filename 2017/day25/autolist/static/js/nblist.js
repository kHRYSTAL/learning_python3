/**
 * Created by kHRYSTAL on 18/1/10.
 */

(function (jq) {

    String.prototype.format = function (args) {
        return this.replace(/\{(\w+)\}/g, function (s, i) {
            return args[i];
        });
    };

    function init(url) {
        // 获取要显示的列
        // 获取数据
        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'JSON',
            success: function (arg) {
                if (arg.status) {
                    // 创建表格标题
                    console.log("获取表格标题成功");
                    createTableHead(arg.data.table_config);
                    // 创建表格内容 arg.data.data_list
                    createTableBody(arg.data.table_config, arg.data.data_list);
                } else {
                    alert(arg.message);
                }
            },
            error: function (e) {
                // 发生未知错误时执行 如500, 404, 返回数据类型与dataType不符合等
                console.log('ajax error:', e)
            }
        });
    }

    function createTableHead(config) {
        /**
         * head
         * [{'q': 'hostname',
         *   'title': '主机名',
         *   'display': 1
         *   'text': {'content': '{n}-{m}', 'kwargs': {'n':'hostname', 'm':'@hostname'}}
         *   },
         *  {'q': 'port', 'title': '端口','display': 1},
         *  {'q': None, 'title': '操作','display': 1}]
         * body
         * [{'port': 11, 'hostname': 'c1.com'}, {'port': 22, 'hostname': 'c2.com'}]
         */
        var tr = document.createElement('tr');
        $.each(config, function (k, v) {
            // k 为 序号, v 为item对象
            if (v.display) {
                var th = document.createElement('td');
                th.innerHTML = v.title;
                $(tr).append(th);
            }
        });

        $('#thead').append(tr);
    }

    function createTableBody(tableConfig, dataList) {
        // 遍历行每行的每一个字段通过列的格式和属性进行操作操作
        $.each(dataList, function (k, row) {
            var tr = document.createElement('tr');
            // 遍历列判断每行的每个字段是否显示等状态
            $.each(tableConfig, function (k1, column) {
                if (column.display) {
                    var td = document.createElement('td');
                    var kwargs = {};

                    //region 处理内容显示
                    // 遍历kwargs参数, 用于格式化需要显示的字符串
                    $.each(column.text.kwargs, function (key, value) {
                        if (value.startsWith('@')) {
                            var temp = value.substring(1, value.length);
                            kwargs[key] = row[temp]; // 开头有@ 表明需要获取data_list中行的某个属性
                        } else {
                            kwargs[key] = value;
                        }
                    });
                    // 赋值给td 可以是html也可以是字符串
                    td.innerHTML = column.text.content.format(kwargs);
                    //endregion

                    //region 处理标签属性
                    $.each(column.attr, function (attr_key, attr_value) {
                        if (attr_value.startsWith('@')) {
                            var temp = attr_value.substring(1, attr_value.length);
                            td.setAttribute(attr_key, temp);
                        } else {
                            td.setAttribute(attr_key, attr_value);
                        }

                    });
                    //endregion
                    $(tr).append(td);
                }
            });

            // 将每行添加到tbody中
            $('#tbody').append(tr);
        })
    }

    jq.extend({
        'initNBList': init
    })
})(jQuery);
