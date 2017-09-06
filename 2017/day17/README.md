GET 获取数据
POST 提交数据

##### 路由系统URL

##### 视图 View
    1. 请求对象
        request.POST    表单提交都从POST中接收
        request.GET     url提交都从GET接收
        request.FILES   文件提交都从FILE接收 html的form要加enctype="multipart/form-data"

    2. 获取请求数据
        1.获取单个数据:
            single_val = request.POST.get('gender')
        2.获取相同name的多个数据:
            multi_val = request.POST.getlist('favour')

        3.获取上传的文件
            file_obj = request.FILES.get('upload_file')
            if file_obj is not None:
                print('获取上传文件', file_obj, type(file_obj))
                print('文件名称', file_obj.name)
                # 获取上传的文件 保存在服务器
                import os
                file_path = os.path.join('upload', file_obj.name)
                f = open(file_path, mode='wb')
                # chunks 是上传文件的块 是一个生成器 需要迭代
                for block in file_obj.chunks():
                    f.write(block)
                f.close()
            else:
                print('文件为空')



##### 模板 Template

##### Django-ORM操作
      原生sql语句与django orm语句都是有对应关系的
      我们需要学习的就是这套对应关系
      增删改查 1对1 1对多 多对多

        select * from tb where id > 1
        models.tb.objects.filter(id__gt=1)

        select * from tb where id < 1
        models.tb.objects.filter(id__lt=1)

        select * from tb where id = 1
        models.tb.objects.filter(id=1)