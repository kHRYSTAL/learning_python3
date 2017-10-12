##### 知识点概要

- Session
- CSRF
- Model操作
- Form验证(ModelForm)
- 中间件
- 缓存
- 信号


1. Session

        cookies优点是把存储的压力存储在客户端电脑上
        基于Cookies做用户验证时 不建议将敏感信息(用户名/密码) 存储为cookie
        因为cookie的特性 前端可以查看与修改 这样是非常不安全的
        因此 如果要做敏感信息存储 且不需要频繁查询数据库的话 应当使用Session

        1. 原理
            cookie是保存在用户浏览器端的键值对
            session是保存在服务器端的键值对
                那么 如何验证某个客户端对应服务器内的session?
                    实际上session还是依靠于cookie, 在浏览器客户端的cookie中
                    存储指向服务器session的唯一标识 当浏览器访问服务器时携带cookie
                    服务器通过cookie中的标识去获取这个用户的敏感信息
                    这样 就实现了session的获取与唯一

