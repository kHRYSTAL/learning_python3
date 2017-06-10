类

	属性

		实例变量

		类变量

		私有属性__var

	方法

		构造方法

		析构函数

		私有方法__function(*args, **kwargs)


继承

	继承的方式(继承/ 组合)
	代码的重用
	单继承
	多继承
		2.7 经典类 深度优先
			新式类 广度优先
		3.x 经典类／新式类 广度优先

	调用父类方法

```
class Foo(Boo):
    def __init__(self, name, age, sex, salary, course):
        super(Foo, self).__init(name, age, sex) # [继承]父类需要的参数
        self.boo = Boo(name, age, sex) # [组合]	新加属性指向父类对象
```


对象 实例化一个类之后得到的对象

接口 统一接口 用于多个子类去实现

```
class Animal:
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def talk(self):
        pass

    @staticmethod
    def animal_talk(obj):
        """
        该函数为接口 一个接口多种实现
        """
        print(obj.talk())

Animal.animal_talk(d)
Animal.animal_talk(c)
```

多态:

	接口重用 一个接口 多种实现



方法:

	静态方法

		只是名义上归类管理 实际上在静态方法里访问不了类和实例的任何属性

	类方法

		只能访问类变量 不能访问实例变量

	属性方法

		把一个方法变成静态属性 需要装饰器 @property @method.setter @method.deleter @method.getter
		作用是隐藏实现细节

反射

    __getattr__()
    __setattr__()
    __hasattr__()
    __delattr__()


异常

    异常捕获与自定义异常
    raise # 抛出异常

    try:
        pass
    except Exception as e:
        pass
    else:
        pass
    finally:
        pass
使用type创建类

```
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func(self):
        """装配到类的函数"""
        print('hello class %s' % self.name)

    '''类名 父类 类的变量和函数'''
    Foo = type('Foo', (object,), {'talk': func, '__init__': __init__})
    print(type(Foo))
    f = Foo('Hello', 22)
    f.talk()
```

类的实例化过程

    元类__metaclass__
    类中由一个属性__metaclass__
    其用来表示该类由谁来实例化创建
    所以 我们可以为__metaclass__设置一个type类的派生类
    从而查看类的创建过程
    __new__
    __init__

动态导入

    1.内置方法__import__('str')
    2.improt importlib

内置方法

    __new__()
    __call__() : obj = Dog(), obj() 会执行call方法
    __metaclass__ : 定义类是由何种方法去创建对象
    __setitem__
    __getitem__
    __delitem__

断言

    assert 如果不通过抛出异常

