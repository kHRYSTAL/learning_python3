# Django常用命令

1. 创建Project
    切换到指定目录 执行django-admin startproject [项目名称]

2. 启动项目服务器
    python manage.py runserver [127.0.0.1:8001]

3. 创建项目中的应用(业务模块)
    python manage.py startapp [appname]

4. 更新表结构
    python manage.py makemigrations

5. 同步表结构至数据库
    python manage.py migrate