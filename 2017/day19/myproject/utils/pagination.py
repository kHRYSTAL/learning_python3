#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: 
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: pagination.py
# @time: 17/10/8 下午11:09


class Page(object):

    def __init__(self, current_page, item_count, page_of_count=5, show_page_num=11):
        super().__init__()
        self.current_page = current_page
        self.item_count = item_count
        # 每页显示多少个
        self.page_of_count = page_of_count
        # 显示页码个数
        self.show_page_num = show_page_num
        # 每页5条 求总页数和余数 如果余数大于0 则总页数需要加1
        self.page_count, remainder = divmod(item_count, page_of_count)  # 求商和余数

        if remainder:
            self.page_count += 1

        # 防止查询越界
        if current_page <= 0:
            self.current_page = 1
        elif current_page >= self.page_count:
            self.current_page = self.page_count

    @property
    def start(self):
        return (self.current_page - 1) * self.page_of_count

    @property
    def end(self):
        return self.current_page * self.page_of_count

    def generate_page_str(self, base_url):
        # 计算输出给前端的标签字符串
        page_str_list = []
        # 页数过多时会导致页面上页码占地过多 因此只显示当前页前后5页的页码
        if self.page_count < self.show_page_num:
            start_index = 1
            end_index = self.page_count
        else:
            if self.current_page <= int(self.show_page_num / 2):
                start_index = 1
                end_index = self.show_page_num
            elif self.current_page >= self.page_count - int(self.show_page_num / 2):
                start_index = self.page_count - (self.show_page_num - 1)
                end_index = self.page_count
            else:
                start_index = self.current_page - int((self.show_page_num - 1) / 2)
                end_index = self.current_page + int((self.show_page_num - 1) / 2)

        if self.current_page <= 1:
            prev = '<a class="page" href="#">上一页</a>'
        else:
            prev = '<a class="page" href="%s%s">上一页</a>' % (base_url, self.current_page - 1,)
        page_str_list.append(prev)

        for i in range(start_index, end_index + 1):
            page_str_list.append(
                '<a class="page %s" href="%s%s">%s</a>' % ("active" if i == self.current_page else "", base_url, i, i))

        if self.current_page >= self.page_count:
            next = '<a class="page" href="#">下一页</a>'
        else:
            next = '<a class="page" href="%s%s">下一页</a>' % (base_url, self.current_page + 1,)
        page_str_list.append(next)

        # 增加跳转标签
        jump = """
                <input type="text"/><a onclick="jumpTo(this, '%s');">GO</a>
                <script>
                    function jumpTo(data, url){
                        var page = data.previousSibling.value;
                        location.href = url + page;
                    }
                </script>
            """ % (base_url,)

        page_str_list.append(jump)
        page_str = "".join(page_str_list)
        # 向django表明这段注入的标签字符串是安全的 可以正常显示
        from django.utils.safestring import mark_safe
        page_str = mark_safe(page_str)
        return page_str


if __name__ == '__main__':
    pass