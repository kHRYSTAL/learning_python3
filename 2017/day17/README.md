##### 路由系统URL

##### 视图 View

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