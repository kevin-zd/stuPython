"""
了解面向对象编程的基本概念，例如类、对象、继承、多态等
"""

'''
在Python中，面向对象编程是一种重要的编程范式，它将数据和行为封装在一个对象中，以实现代码的重用和模块化。
以下是Python中面向对象编程的基本概念：
'''

# 1.类：类是一种用户自定义的数据类型，用于封装数据和行为。可以通过class关键字定义一个类，并在类中定义属性和方法。

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

person = Person("John", 30)
person.greet()  # 输出Hello, my name is John

'''
在上面的示例中，我们定义了一个名为Person的类，并在类中定义了两个属性name和age，以及一个方法greet()。
在类的实例化过程中，我们通过调用类的构造函数__init__()来初始化对象的属性。然后，我们使用对象的greet()方法打印出对象的名字。
'''

# 2.对象：对象是类的实例，它具有类定义的属性和方法。可以使用类名加括号的方式创建一个对象。
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

person = Person("John", 30)
person.greet()  # 输出Hello, my name is John
'''
在上面的示例中，我们使用Person类创建了一个名为person的对象，并通过调用对象的greet()方法打印出对象的名字。
'''

# 3.继承：继承是一种机制，用于创建一个新类，并从一个或多个现有类中继承属性和方法。可以使用子类来扩展或修改父类的行为。
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def study(self):
        print(self.name, "is studying in grade", self.grade)

student = Student("Alice", 20, 12)
student.greet()  # 输出Hello, my name is Alice
student.study()  # 输出Alice is studying in grade 12

'''
在上面的示例中，我们定义了一个名为Student的子类，并从父类Person中继承了属性和方法。
在子类中，我们还添加了一个新的属性grade和方法study()，以扩展父类的行为。
在子类的实例化过程中，我们使用super()函数调用父类的构造函数，并初始化子类自己的属性。
'''

# 4.多态：多态是一种机制，用于在不同的对象上调用相同的方法，并产生不同的行为。可以通过方法重写和方法重载来实现多态。
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

def make_animal_sound(animal):
    animal.make_sound()

dog = Dog()
cat = Cat()

make_animal_sound(dog)  # 输出Woof!
make_animal_sound(cat)  # 输出Meow!

'''
在上面的示例中，我们定义了一个名为Animal的父类，并在其中定义了一个抽象方法make_sound()。
然后，我们定义了两个子类Dog和Cat，并分别重写了make_sound()方法。
最后，我们定义了一个函数make_animal_sound()，它接受一个Animal类型的参数，并在其中调用make_sound()方法。
通过传入不同类型的对象，我们可以产生不同的行为，实现多态性。

通过上面的示例，我们可以看到，在Python中进行面向对象编程非常简单、直观。
面向对象编程可以使代码更加清晰、易于维护、易于扩展，是Python编程中非常重要和常见的一部分。
'''




