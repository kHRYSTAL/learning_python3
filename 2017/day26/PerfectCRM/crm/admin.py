from django.contrib import admin
# 在此文件注册model后 在django管理后台可见
# Register your models here.
from crm import models

""" 自定义admin中的展现形式 """


class CustomerAdmin(admin.ModelAdmin):
    """默认展现列"""
    list_display = ('id', 'name', 'qq', 'consultant', 'source', 'consult_content', 'status', 'date')
    """过滤器"""
    list_filter = ('source', 'status', 'consultant')
    """搜索"""
    search_fields = ('qq', 'name')
    """是否可编辑"""
    list_editable = ('status',)


class CustomerFollowUPAdmin(admin.ModelAdmin):
    """客户跟进表设置"""
    list_display = ('customer', 'content', 'status', 'consultant', 'date')


admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.FollowUpRecord, CustomerFollowUPAdmin)
admin.site.register(models.Enrollment)
admin.site.register(models.Course)
admin.site.register(models.ClassList)
admin.site.register(models.StudyRecord)
admin.site.register(models.UserProfile)
admin.site.register(models.Branch)
admin.site.register(models.Role)
admin.site.register(models.Menu)
admin.site.register(models.CourseRecord)
