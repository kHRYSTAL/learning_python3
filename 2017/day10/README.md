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

    添加主键:
        主键只能作用在一个列上 添加主键时需要确保该列默认不为空
        alter table student MODIFY name char(16) not null;
        设置为主键
        alter table student ADD PRIMARY KEY(name)

    删除主键
        alter table student DROP PRIMARY KEY
        删除主键不需要指定列名


##### 模糊匹配

    %表示模糊匹配


##### 外键关联

    外键创建

        1.创建学生考勤表
            create table study_record(
                id int auto_increment primary key, # 可以在声明的时候直接在后面声明主键
                day int not null,
                status char(32) not null default Yes,
                stu_id int not null,

                key 'fk_student_key' ('stu_id'), # 声明stu_id为外键, 别名为fk_student_key
                constraint 'fk_student_key' foreign key ('stu_id') reference student ('stu_id')
                # 约束 该表的stu_id字段 参考student表的stu_id, 即这个表的stu_id是外键 依赖student表的stu_id
            )

        查看表结构
            desc study_record;
            表结构中 KEY 列 显示stu_id 为MUL 表示stu_id为外键

        2.插入数据
            insert into study_record (day, status, stu_id) values (1, YES, 1)
            注意 因为stu_id是外键, 具有参照完整性, 不能插入student表中不存在的stu_id
            即study_record表的stu_id需要参照(引用)student表的stu_id;

            ##########
            注意! 如果此时执行删除student表的数据
            如 delete from student where stu_id=1;
            如果此时student表中的数据被study_record表的数据引用 则会报错不能删除, 需要先删除study_record表的数据
            使引用不被持有 才可以删除
            ##########
##### 空值处理

        IS NULL: 当列的值为空时返回true
        IS NOT NULL: 当列的值不为空时返回true
        < = >: 当比较的两个值为空时 返回true

        在MySQL中 NULL值与任何其他值的比较 永远返回false 即时NULL = NULL

        例句 select * from student where name is null;


##### 连接查询

        两个活多个表连接查询, 得到的结果集合方式
        left join 获取左表的所有记录, 即使右表没有匹配对象
        right join 获取右表所有记录, 即使左表没有匹配对象
        inner join 内连接  获取两个表中字段匹配关系的记录
        full join

        A表      B表
        a        b
        -        -
        1        3
        2        4
        3        5
        4        6

        1.inner join: 交集查询
          select * from a INNER JOIN b on a.a = b.b  # on 后为声明两个表的连接点 即连接条件
          select a.*, b.* from a, b where a.a = b.b
          两句等价

          返回
          a b
          3 3
          4 4

        2.left join
          select * from A left join B on A.a = B.b;
          先查询表A所有数据, 在查询表B中符合连接条件的数据 B符合条件的数据与A中对应的数据同行

        3.right join
          select * from A right join B on A.a = B.b;
          先查询表B所有数据, 在查询表A中符合连接条件的数据
          相当于: select * from B left join A on A.a = B.b;

        4.full join
          求并集, 查询表A 和表B所有数据 符合条件的数据处于同一行
          MySQL 不直接支持并集 因为没用

          select * from A left join B on A.a = B.b UNION select * from A right join B on A.a = B.b;
          相当于查询表A所有数据与B符合条件的数据获取的结果
          与查询表B所有的数据与A符合条件的数据获取的结果, 去重后联合显示

##### 事务 Transaction

    事务用于处理频繁操作或数据量大的操作 避免频繁连接或修改表 一次性执行所有操作
    同时也是完整性的体现, 要么全部执行 要么全部不执行
    MySQL 中只有使用了Innodb数据库引擎的数据库或表才支持事务
    事务可以管理insert, update, delete的写操作

    事务回滚与提交

    1.
    begin;
    insert into student (name, register_date, gender) values ("kHRYSTAL", 1990-08-31, "M");
    insert into student (name, register_date, gender) values ("Matt", 1990-08-31, "M");
    # 此时查看表中是存在这两个数据的 数据实际存在内存中 并没有刷新到硬盘存储上 但是id实际上已经写入了

    rollback;
    # 回滚 事务结束 再次查看表中不存在这两行数据

    2.
    begin;
    insert into student (name, register_date, gender) values ("kHRYSTAL", 1990-08-31, "M");
    insert into student (name, register_date, gender) values ("Matt", 1990-08-31, "M");
    commit; # 结束事务并保存提交


##### 索引

        索引能够优化查询,建立索引后不需要改变任何查询操作, 使用B+树原理查找, 效率更高
        索引分为单列索引和组合索引,
            单列索引, 即一个索引只包含单个列, 一个表可以有多个单列索引
            组合索引, 即一个索引包含多个列

        创建索引时 需要确保是应用在SQL查询语句的条件(一般作为WHERE 子句的条件)
            即查询时 按照索引去查找, 如身份证号为索引 但查找时却按照性别去查找, 实际上查询并没有根据索引实现优化

        缺点 使用索引 会导致读快写慢
            滥用会导致更新表的速度, 对表进行写操作(增删改), 表进行刷新时 MySQL 不仅要保存数据 还要保存索引文件
            (对存储的数据进行排序 这样可以在查询时优化 但是写操作会花费更多的时间)
            同时,建立索引会占用磁盘空间


        操作:

            查看表中的索引
                show index from [table name];\G
            有一列indexType, 是索引类型 显示BTree
                默认主键也是一种索引
            创建索引
                第一种方式
                    CREATE INDEX [indexName] ON [table name]([column_name]([indexlength]));
                    例: create index index_name on student(name(32));
                    # indexlength为索引的长度 意思是说列的数据进行hash处理生成的长度不超过多少位, 一般建议是不超过字段的长度
                第二种方式
                    alter student add index index_name on (name(32));
                第三种方式
                    创建表的时候直接指定

                    create table student(
                        id int auto_increament primary key,
                        name varchar(16) not null,
                        index index_name (name(16))
                    );

            删除索引 drop index index_name on student


        唯一索引:
            主键就是唯一索引的一种, 与普通索引不同的是 列的每个数据的值都是唯一的, 允许有空值
            如果索引是组合索引 则列的数据的值的组合hash必须是唯一的

            创建索引:
                CREATE UNIQUE INDEX [index_name] on [table_name]([column_name](length));
                例子: create unique index index_stu_name on student(name(32));
                如果name为重复的 则不能创建

                第二种方式
                alter student add index index_name on (name(32));

                第三种方式
                创建表的时候直接指定

                    create table student(
                        id int auto_increament primary key,
                        name varchar(16) not null,
                        UNIQUE index_name (name(16))
                    );

#### MySQL 与 python 交互

    python3.x 可以使用pymysql这个lib实现交互

### python ORM框架 SQLAlchemy
    ORM Object Relational Mapping 对象关系映射
    alchemy	英[ˈælkəmi] 魔法 魔力
    将数据库/表/行数据 映射成python对象
    通过操作对象 执行操作数据库的操作

![](http://images2015.cnblogs.com/blog/720333/201610/720333-20161019162806842-1144462684.png)

    SQLAlchemy
    根据配置文件的不同调用不同的数据库API，从而实现对数据库的操作，如：

    MySQL-Python
        mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>

    pymysql
        mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]

    MySQL-Connector
        mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>

    cx_Oracle
        oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]

    ###################################
    # 操作                            #
    #    参考sqlalchemy_basic.py      #
    ###################################





##### 外键关联查询

    class User(Base):
        __tablename__ = 'user'  # 表名
        id = Column(Integer, primary_key=True)
        name = Column(String(32))
        password = Column(String(64))

        def __repr__(self):
            return "<%s name: %s>" % (self.id, self.name)

    class Address(Base):
        __tablename__ = 'addresses'
        id = Column(Integer, primary_key=True)
        email_address = Column(String(32), nullable=False)
        user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

        user = relationship("User", backref="addresses")  # 关联两个对象, 并不是数据库真实存在的列, 而是orm操作存储在内存中的
        # 即在查询address数据时 orm会通过外键去获取user的数据 并赋值给user这个变量
        # 相当于 user = Session.query(User).filter(Address.user_id == User.id).first()
        # 这句话的意思是, 可以通过user字段获取表User关联的数据, User表可以通过addresses字段获取Address表的数据

        def __repr__(self):
            return "<Address(email_address='%s', UserName= '%s')>" % (self.email_address, self.user.name)

    # 连表查询
    ret = Session.query(User, Address).filter(User.id == Address.user_id).all()
    print(ret)

    ret = Session.query(User).join(Address).all()  # 这种写法必须要求两个表之间有外键关联
    print(ret)

##### 多对一外键关联查询

    class Customer(Base):
    """
    消费表 包含外键账单地址id和收货地址id 两个id都是外键关联address表id
    """
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    billing_address_id = Column(Integer, ForeignKey("address.id"))  # 外键关联address表id
    shipping_address_id = Column(Integer, ForeignKey("address.id"))  # 外键关联address表id
    # 由于是多外键, address在反查customer时分不清使用的是哪个id, 因此需要指明通过哪个id反查
    billing_address = relationship("Address", foreign_keys=[billing_address_id])
    shipping_address = relationship("Address", foreign_keys=[billing_address_id])


    class Address(Base):
        __tablename__ = 'address'
        id = Column(Integer, primary_key=True)
        street = Column(String)
        city = Column(String)
        state = Column(String)


##### 多对多外键关联查询

    """
    多对多关联
    如每本书可以有多个作者
    每个作者可以有多本书
    这种情况下为了减少数据冗余 应建立三张表
    作者表 书表 作者与书的关系表

    第三张表用于主动关联前两张表
    书表和作者表没有直接的关联关系
    """
    import sqlalchemy
    from sqlalchemy import Table, Column, Integer, String, DATE, ForeignKey
    from sqlalchemy.orm import relationship
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    Base = declarative_base()

    # 书与作者的关系表 这张表不应手动创建 因为我们不会去手动向这张表插入数据, 只需要在存储书的时候指明作者 或存储作者的时候指明书
    # orm自己去维护这张表 谁都不用去关心 实际上这个表只是指明了book和author的关联关系 用于book反查user和user反查book
    # 存储时会自动关联, 将id存储到这个表里
    # 只是告诉orm去哪张表查数据
    book_m2m_author = Table('book_m2m_author', Base.metadata,
                            Column('book_id', Integer, ForeignKey('books.id')),
                            Column('author_id', Integer, ForeignKey('authors.id')),
                            )


    # 书表
    class Book(Base):
        __tablename__ = 'books'
        id = Column(Integer, primary_key=True)
        name = Column(String(64))
        pub_date = Column(DATE)
        # 通过书与作者的关系表 在这张表里能查到authors, 在Author表能通过books查到Book表的数据
        # secondary 间接的
        authors = relationship('Author', secondary=book_m2m_author, backref='books')

        def __repr__(self):
            return self.name


    # 作者表
    class Author(Base):
        __tablename__ = 'authors'
        id = Column(Integer, primary_key=True)
        name = Column(String(32))

        def __repr__(self):
            return self.name


    engine = sqlalchemy.create_engine("mysql+pymysql://root:yyg1990918@localhost/awesome",
                                      encoding='utf-8', echo=True)
    Base.metadata.create_all(engine)













