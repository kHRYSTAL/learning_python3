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





