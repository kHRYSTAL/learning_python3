/**
 * Created by kHRYSTAL on 18/1/10.
 */

(function (jq) {

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
         * [{'q': 'hostname', 'title': '主机名','display': 1},{'q': 'port', 'title': '端口','display': 1},{'q': None, 'title': '操作','display': 1}]
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
        // 遍历行
        $.each(dataList, function (k, row) {
            var tr = document.createElement('tr');
            // 遍历列判断每行的每个字段是否显示等状态
            $.each(tableConfig, function (k1, column) {
                var td = document.createElement('td');
                if (column.q) {
                    td.innerHTML = row[column.q];
                }
                $(tr).append(td);
            });

            // 将每行添加到tbody中
            $('#tbody').append(tr);
        })
    }

    jq.extend({
        'initNBList': init
    })
})(jQuery);
