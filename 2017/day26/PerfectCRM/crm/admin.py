from django.contrib import admin
# 在此文件注册model后 在django管理后台可见
# Register your models here.
# 看不到表需要执行 syncdb
from crm import models
admin.site.register(models.Customer)
admin.site.register(models.FollowUpRecord)
admin.site.register(models.Enrollment)
admin.site.register(models.Course)
admin.site.register(models.ClassList)
admin.site.register(models.StudyRecord)
admin.site.register(models.UserProfile)
admin.site.register(models.Branch)
admin.site.register(models.Role)
admin.site.register(models.Menu)
admin.site.register(models.CourseRecord)

