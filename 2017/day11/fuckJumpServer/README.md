#### 堡垒机项目

##### 表结构关联关系

    流程: 堡垒机账户 通过密码或SSHkey 连接远程机器账户

        堡垒机账户   可登录ip地址       远程机器账户(权限)
        matt        192.168.1.10     root
        matt        192.168.1.11     mysql
        khrystal    192.168.1.10     root
        khrystal    10.6.4.33        mysql
        khrystal    10.6.4.33        web

* 连接的主机表 host

        ip      hostname    port

* 用户信息 user_profile

        username(堡垒机账户)    password

* 远程机器用户表 remote_user

        username(远程机器账户)    password    auth_type(passwd或rsa_key)
        root                    abc         ssh-password
        root                    123         ssh-key
        mysql                   abc
        mysql                   123

* 主机组表 host_group

        name


  主机组表与主机表关系, 一个主机组可以关联多个主机 一个主机可以属于多个组




* 审计日志表 auditlog

    date    堡垒机账户   cmd     ip      remote_user(远程机器账户)