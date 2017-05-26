#!/usr/bin/env python3
# -*-coding:utf-8 -*-


'''
(object)，表示该类是从哪个类继承下来的，
继承的概念我们后面再讲，通常，
如果没有合适的继承类，就使用object类，
这是所有类最终都会继承的类
'''
class Student(object):
    pass

bart = Student()

print(bart)

print(Student)
#可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：
bart.name = 'Bart Simpson'
print(bart.name)


'''
由于类可以起到模板的作用，因此，可以在创建实例的时候，
把一些我们认为必须绑定的属性强制填写进去。
通过定义一个特殊的__init__方法，在创建实例的时候，
就把name，score等属性绑上去：
'''

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score


'''
注意到__init__方法的第一个参数永远是self，表示创建的实例本身，
因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

有了__init__方法，在创建实例的时候，就不能传入空的参数了，
必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：
'''

bart = Student('Bart Simpson', 59)

print(bart.name, bart.score)


#数据封装

'''
面向对象编程的一个重要特点就是数据封装。在上面的Student类中，
每个实例就拥有各自的name和score这些数据。我们可以通过函数来访问这些数据，
比如打印一个学生的成绩：

>>> def print_score(std):
...     print('%s: %s' % (std.name, std.score))
...
>>> print_score(bart)
Bart Simpson: 59
但是，既然Student实例本身就拥有这些数据，要访问这些数据，
就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，
这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，
我们称之为类的方法：
'''

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s : %s' % (self.name, self.score))
        return None

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

matt = Student('matt', 80)


print(matt.get_grade())
matt.print_score()
print(matt.name,matt.score)

'''
类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
'''