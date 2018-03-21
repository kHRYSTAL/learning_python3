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

6. 创建后台管理root用户
    python manage.py createsuperuser 创建project的后台root用户

### 配置模版路径
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    在views中使用:
        def login(request):
            # 使用render一行解决 去模版文件夹寻找模版文件
            return render(request, 'login.html')


### 配置静态文件路径
    # 静态文件前缀 在template中使用的静态文件都会通过前缀去找寻STATICFILES_DIRS下的文件
    STATIC_URL = '/static/'

    # 配置静态文件目录路径
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

    在html中使用:
        <link rel="stylesheet" href="/static/commons.css">

### CSRF 跨站请求伪造
    目前需要注释