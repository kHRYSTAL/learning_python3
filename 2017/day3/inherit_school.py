#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @version: ??
# @usage: inherit test
# @author: kHRYSTAL
# @license: Apache Licence 
# @contact: khrystal0918@gmail.com
# @site: https://github.com/kHRYSTAL
# @software: PyCharm
# @file: inherit_school.py
# @time: 17/6/7 上午10:53


class SchoolMember(object):

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        """
        个人信息
        """
        pass


class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []

    def enroll(self, stu_obj):
        """
        注册
        """
        print('为学员%s 办理注册手续' % stu_obj.name)
        self.students.append(stu_obj)

    def hire(self, staff_obj):
        """
        雇佣
        """
        print('雇佣新员工 %s' % staff_obj.name)
        self.staffs.append(staff_obj)


class Teacher(SchoolMember):

    def __init__(self, name, age, sex, salary, course):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        ----- info of Teacher:%s -----
        Name: %s
        Age: %s
        Sex: %s
        Salary: %s
        Course: %s
        ''' % (self.name, self.name, self.age, self.sex, self.salary, self.course))

    def teach(self):
        """
        教课
        """
        print('%s is teaching course [%s]' % (self.name, self.course))


class Student(SchoolMember):

    def __init__(self, name, age, sex, stu_id, course):
        super(Student, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.course = course

    def tell(self):
        print('''
        ----- info of Student: %s -----
        Name: %s
        Age: %s
        Sex: %s
        StudentId: %s
        Course: %s
        ''' % (self.name, self.name, self.age, self.sex, self.stu_id, self.course))

    def pay_tuition(self, amount):
        """
        交学费
        """
        print('%s has paid tuition for $%s' % (self.name, amount))


school = School('zhisland', 'university center')
t1 = Teacher('Alex', 56, 'MF', 200, 'Linux')
t2 = Teacher('Jack', 22, 'M', 300, 'PythonDevOps')

s1 = Student('Khrystal', 23, 'M', 1001, 'PythonDevOps')
s2 = Student('Andy', 19, 'M', 1002, 'Linux')

t1.tell()
s1.tell()

school.enroll(s1)
school.enroll(s2)
school.hire(t1)

print(school.students)
print(school.staffs)

school.staffs[0].teach()

for stu in school.students:
    stu.pay_tuition(5000)
