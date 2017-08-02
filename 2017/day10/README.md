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
    desc [table name]; 显示表的结构 等同于show colunms from [table name];
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

    创建数据库 此时默认语言为拉丁文 latin 不支持中文 且不可修改
    create database [database name];
    创建支持中文存储的数据库
    create database [database name] charset utf-8;

    显示数据库默认字符集
    show create database [database name];

    删除数据库
    drop database [database name];

    显示表的索引信息 包括主键
    show index from [table name];

    创建表
    语法:
        CREATE TABLE table_name(column_name column_type)
    例子
        create table student(
            stu_id INT NOT NULL AUTO_INCREMENT,
            name CHAR(32) NOT NULL,
            age INT NOT NULL,
            register_date DATE,
            PRIMARY KEY ( stu_id ) # 设置为主键 每行的值是唯一的 如果显式插入id重复的数据 会报错
        );

    插入数据
        insert into student (name, age, register_date) values ("matt", 22, "2017-08-02")

    查询数据
        select * from student;
        * 表示一行的所有数据

        SELECT column_name, column_name FROM table_name [WHERE clause] [OFFSET M] [LIMIT N];
            column_name 为指定列名字段的数据
            WHERE 是条件判断 用于条件过滤
            OFFSET 为开始查询数据的偏移量 默认为0 如:为10 则从第10条开始查需要于LIMIT 联合使用
            LIMIT 为结果的限制数量 按照行的从上到下排序
        select name from student where age > 13 and age < 20 offset 1 limit 10
            从学生表查询年龄大于13且小于20 的用户名称, 从第1行开始查 输出10个

        模糊查询:
            select * from student where register_date like "2017-07%";

    修改数据
        UPDATE table_name SET field1=new_value, field2=new_value2 [WHERE clause]

        例: update student set name="khrystal", age="23" where id=1;
        修改id为1的行的name为khrystal, age为23

    删除行
        delete from student where name='khrystal';
        注意一定要加where 否则是删除表中所有数据

    查询排序 按照某列升序降序排列 前面可加条件
        select * from student [where age > 22] order by stu_id [asc|desc];

    分组统计
        select name, count(*) as num from student group by name with rollup;
        按照name进行分组, 输出name和组内个数num(count(*)的别名) count(*)为内置方法 计算组内的数量
        select coalesce(name,"Total age"), sum(age) from student group by name;
        按照name进行分组, 输出name和组内年龄总和, 获得的查询数据最后一行输出每个分组年龄的总和, 总和的名称为Total age
        如果不屑coalesce 则名称为NULL


    删除列/添加列
        alter table student add sex enum("M", "F");
        声明student表新增列sex 类型为枚举
        alter table student drop age; 删除age列

    修改列的类型和关键字
        alter table student modify name char(100);
        将name字段类型改为char(100) 此时name字段可以为null了 所以修改时必须要加上原来需要的关键字
        alter table student modify sex enmu("M", "F") not null;
        修改sex字段为不能为空

        关于MySQL的枚举, 如果设置为not null 插入数据时如果不填写sex, 则默认使用枚举的第一个类型

    修改列的列名(也可修改类型与关键字)
        alter table student change sex gender char(32) not null default "X";
        修改sex列名为gender 数据类型改为char(32) 不允许为空 默认为X

        注意: 如果原来不是not null 而新增了not null的关键字 只对后续数据添加有影响 原来的数据有null的情况存在

    修改表名

        alter table student RENAME TO students;
        修改student表名为students







