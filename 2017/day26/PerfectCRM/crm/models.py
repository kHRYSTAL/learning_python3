from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    """客户信息表"""
    name = models.CharField(max_length=32)
    qq = models.CharField(max_length=64, unique=True)
    # blank 如果为True，字段允许为空，默认不允许。
    # Null 如果为True，空值将会被存储为NULL，默认为False。
    """
    一句话概括
    null 是针对数据库而言，如果 null=True, 表示数据库的该字段可以为空。
    blank 是针对表单的，如果 blank=True，表示你的表单填写该字段的时候可以不填，比如 admin 界面下增加 model 一条记录的时候。直观的看到就是该字段不是粗体
    """
    weixin = models.CharField(max_length=64, blank=True, null=True)
    # 只能输入正数
    phone = models.PositiveIntegerField(blank=True, null=True)
    # 来源映射
    source_choice = ((0, 'Badidu商桥'),
                     (1, '51CTO'),
                     (2, 'QQ群'),
                     (3, '知乎'),
                     (4, 'SOGO'),
                     (5, '转介绍'),
                     (6, '其他')
                     )
    source = models.SmallIntegerField(choices=source_choice)
    # 谁转介绍的 Customer 关联 Customer my_referrals用于反向查找自己介绍了哪些人 非必填
    referral_from = models.ForeignKey("self", related_name="my_referrals", blank=True, null=True, verbose_name='转介绍')
    # 咨询课程 m2m
    consult_courses = models.ManyToManyField("Course")
    # 报名状态
    status_choices = (
        (0, '已报名'),
        (1, '未报名'),
        (2, '已退学')
    )
    status = models.SmallIntegerField(choices=status_choices)
    # 来自哪个销售
    consultant = models.ForeignKey("UserProfile", verbose_name="课程顾问")
    # 销售过程描述
    consult_content = models.TextField(max_length=1024)
    # 新增到表时的时间
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    """学员表 注册表
    1.方便维护与管理
    2.销售管理与学员管理分开 只写与学生相关的属性"""
    # 学员关联客户
    customer = models.ForeignKey("Customer")
    # 学员关联班级 班级关联课程
    class_grade = models.ForeignKey("ClassList")
    enrollment_date = models.DateField()

    def __str__(self):
        return self.customer

    class Meta:
        # 多个字段联合唯一约束 客户不同重复报名同一个班级
        unique_together = ("customer", "class_grade")


class FollowUpRecord(models.Model):
    """跟踪记录"""
    customer = models.ForeignKey("Customer")
    content = models.TextField(max_length=1024)
    status_choice = (
        (0, "绝无报名计划"),
        (1, "一个月内报名"),
        (2, "2周内报名"),
        (3, "已报名其他机构")
    )
    status = models.SmallIntegerField(choices=status_choice)
    date = models.DateTimeField(auto_now_add=True)
    # 来自哪个销售 一个月后未报名 其他人可跟进
    consultant = models.ForeignKey("UserProfile", verbose_name="课程顾问")

    def __str__(self):
        return "%s" % self.customer


class Course(models.Model):
    """课程表"""
    name = models.CharField(unique=True, max_length=64)
    price = models.PositiveIntegerField(default=19800)
    # 课程大纲
    outline = models.TextField()

    def __str__(self):
        return self.name


class ClassList(models.Model):
    """班级列表"""
    course = models.ForeignKey("Course")
    # 班级是课程的第几期 学期
    semester = models.PositiveSmallIntegerField()
    # 开课日期
    start_date = models.DateField()
    end_date = models.DateField()
    # 一个班级多个老师 一个老师可以有多个班级
    teachers = models.ManyToManyField("UserProfile")
    class_type_choices = (
        (0, '脱产'),
        (1, '周末'),
        (2, '网络')
    )
    class_type = models.PositiveSmallIntegerField(choices=class_type_choices)
    branch = models.ForeignKey("Branch")

    def __str__(self):
        return self.course


class CourseRecord(models.Model):
    """每节课上课记录"""
    # 关联班级
    class_grade = models.ForeignKey("ClassList")
    day_number = models.SmallIntegerField(verbose_name='节次')
    # 当日老师
    teacher = models.ForeignKey("UserProfile")
    CourseContent = models.TextField(verbose_name='上课内容', max_length=1024)
    # 是否有作业
    has_homework = models.BooleanField(default=True)
    # 作业标题
    homework_title = models.CharField(max_length=128, blank=True, null=True)
    # 作业需求
    homework_requirement = models.TextField(max_length=128, blank=True, null=True, verbose_name='作业需求')

    def __str__(self):
        return "%s daynum: %s" % (self.class_grade, self.day_number)

    class Meta:
        unique_together = ("class_grade", "day_number")


class StudyRecord(models.Model):
    """每个学生上的每节课的成绩记录"""
    course_record = models.ForeignKey("CourseRecord")
    student = models.ForeignKey("Enrollment")
    # 成绩记录
    score_choices = (
        (100, "A+"),
        (90, "A"),
        (85, "B+"),
        (80, "B"),
        (75, "B-"),
        (70, "C+"),
        (65, "C"),
        (40, "C-"),
        (-2, "D"),  # 不交作业
        (-50, "COPY"),
        (0, "N/A"),  # 没作业
    )
    score = models.SmallIntegerField(choices=score_choices)
    # 考勤记录
    show_status_choices = (
        (0, "缺勤"),
        (1, "已签到"),
        (2, "迟到")
    )
    show_status = models.SmallIntegerField(choices=show_status_choices)
    # 成绩批注 成绩评价
    grade_comment = models.TextField(max_length=1024)

    class Meta:
        unique_together = ('student', 'course_record')

    def __str__(self):
        return "%s daynum:%s" % (self.student, self.course_record)


class UserProfile(models.Model):
    """
    用来定义一对一关系。笼统地讲，它与声明了 unique=True 的 ForeignKey 非常相似，不同的是使用反向关联的时候，
    得到的不是一个对象列表，而是一个单独的对象。在某个 model 扩展自另一个 model 时，这个字段是非常有用的；
    例如： 多表继承 (Multi-tableinheritance) 就是通过在子 model 中添加一个指向父 model 的一对一关联而实现的。
    """
    """账户信息 继承django提供的用户认证model"""
    # 当使用django user获取对象时 内部的crm_user属性为userProfile
    # 如果不写related_name 从django的user反查userProfile 为user.userprofile
    user = models.OneToOneField(User, related_name="crm_user")  # 相当于外键(一对多)并设置unique(一对一) 相当于使用django自带的user表维护userprofile
    name = models.CharField(max_length=32)
    roles = models.ManyToManyField("Role")

    def __str__(self):
        return self.name


class Role(models.Model):
    """角色表"""
    name = models.CharField(unique=True, max_length=32)
    menus = models.ManyToManyField("Menu")

    def __str__(self):
        return self.name


class Branch(models.Model):
    """分校"""
    name = models.CharField(unique=True, max_length=128)

    def __str__(self):
        return self.name


class Menu(models.Model):
    """动态菜单"""
    name = models.CharField(unique=True, max_length=32)
    url_type = models.SmallIntegerField(choices=(
        (0, 'relative_name'),  # django中相对的url路径
        (1, 'absolute_url')  # 外链等绝对url路径
    ))
    # 菜单项关联的url
    url_name = models.CharField(unique=True, max_length=128)

    def __str__(self):
        return self.name
