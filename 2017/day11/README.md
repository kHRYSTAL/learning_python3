还没讲的模块

    celery 分布式任务队列
    subprocess 模块
    logging 模块

#### 堡垒机

    很多人觉得堡垒机就是跳板机 其实是不全面的
    跳板功能只是堡垒机所具备的功能属性其中一项而已


###### ladp 集中式认证
        ad域服务器 建一个账户 所有域下的账号都可以登录
            但不能控制用户权限 即所有ad域下的账户能登录域下的所有服务器
            风险性比较高, 使用局域网可以降低风险


###### 堡垒机需要实现的需求

* 用户权限可控
* 用户行为审计 - 记录行为 并可以禁止用户某些行为 如:rm命令 shutdown reboot等等

###### 主流堡垒机

    商业
        齐治 堡垒机
    开源
        jumpserver


###### 使用paramiko实现用户行为审计功能

    该demo 作用与堡垒机 即堡垒机需要使用的代码

    底层使用paramiko paramiko具体看day6 package
    demos文件夹为从github拷贝的paramiko demo; 在interactive.py做了修改(查看todo)

    为了实现堡垒机自动链接 需要在堡垒机配置用户环境变量
    linux--> ~/.bashrc
    mac--> ~/.bash_profile

    写入:
        python3 [demo.py绝对路径]

    保存后刷新环境变量 source .bashrc 或source .bash_profile
    会自动执行 之后每次重新启动机器都会执行

###### 实现数据库关系与命令行交互

    查看fuckJumpServer 数据库交互已实现 在views.start_session中的todo是连接审计记录功能的位置
    未完成