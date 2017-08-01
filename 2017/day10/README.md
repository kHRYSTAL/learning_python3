#### MySQL 关系型数据库

1. 数据冗余 当需要查询的数据需要关联多个表时 数据冗余可以增加数据查询的速度

2. 主键是唯一的 用于区分相同数据, 一般使用自增字段(列)id表示是唯一(不重复)的

3. 外键用于关联两个表 一个表的某个字段 用于关联另一个表的某个字段 即两个字段的属性是相同的
    用于关联两个表的数据 如: student表中的class_id 关联class表的id 这样就可以查询到student
    所在的class的相关数据

4. 复合键 将多个列作为一个索引键(联合主键), 用于复合索引查询

5. 索引 用于快速查询数据, 在查询中 比如要查name为'matt'的某个数据, 实际上可以通过预先
    在表中插入name的hash值作为一列 如 列名为hash_name, 存储的为name的哈希值(数字)
    在查询的时候 先通过hash(name)获取hash值, 将表中所有的数据按hash排序, 这样可以通过二分法查询
    数据, 这样的速度比遍历查询更快. 相当于对name字段进行了优化, hash_name就是name的索引

    在MySQL中 索引实际上使用的是B+树查询

6. 参照完整性, 在数据库表的设计中 不允许引入不存在的实体, 如某个student的class_id 是class表中不存在的


##### 常用命令

    mysql 启动mysql
    mysqladmin -u root password [password] 创建root密码
    mysqladmin -u root -p password [password] 修改root密码
    mysql -u root -p 以root用户密码启动mysql 只有以root用户登录才能看到所有库

    SHOW DATABASES; 列出所有数据库
    use [database name]; 进入数据库
    show tables; 显示指定库中的表
    desc [table name]; 显示表的结构
    select * from [table name]\G 格式化列出表中的数据


    查看是否启用进程
    ps -ef | grep mysql
    创建用户 注意 应以admin用户登录 否则看不到user表
    第一种:
        向user表中插入数据, 如:
        INSERT INTO `user` VALUES ('localhost','matt','','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','','','','',0,0,0,0);

    第二种
        创建并授权: 授权用户在所有ip地址下对某个数据库下的表拥有所有权限, []表示可修改, *表示库下的所有表
        grant [all] on [database name].* to '[username]'@'[ipaddress]' identified by '[user password]';

    查看用户权限
    show grants for [username];

    刷新数据库
    flush privileges;




