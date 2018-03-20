from django.db import models


# Create your models here.

class Customer(models.Model):
    """客户信息表"""
    pass


class Enrollment(models.Model):
    """学员表 注册表
    1.方便维护与管理
    2.销售管理与学员管理分开 只写与学生相关的属性"""
    pass


class FollowUpRecord(models.Model):
    """跟踪记录"""
    pass


class Course(models.Model):
    """课程表"""
    pass


class ClassList(models.Model):
    """班级列表"""
    pass


class CourseRecord(models.Model):
    """每节课上课记录"""
    pass


class StudyRecord(models.Model):
    """每个学生上的每节课的成绩记录"""
    pass


class UserProfile(models.Model):
    """账户信息"""


class Role(models.Model):
    """角色表"""
    pass


class Branch(models.Model):
    """分校"""
    pass


class Menu(models.Model):
    """动态菜单"""
    pass
