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


