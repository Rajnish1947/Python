# -------------------------------------
# 1. Basic Class with Class Variable
# -------------------------------------
class MyClass:
    x = "This is my class"

p1 = MyClass()
print("1:", p1.x)

# -------------------------------------
# 2. Class with Constructor (__init__) and Instance Variables
# -------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p2 = Person("Rajnish", 21)
print("2: Name:", p2.name, "| Age:", p2.age)

# -------------------------------------
# 3. Class with a Method
# -------------------------------------
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("3: Hello", self.name)

s1 = Student("Pooja")
s1.greet()

# -------------------------------------
# 4. Class with Default Parameter
# -------------------------------------
class Car:
    def __init__(self, brand="Tata"):
        self.brand = brand

c1 = Car()
c2 = Car("Mahindra")
print("4:", c1.brand)
print("4:", c2.brand)

# -------------------------------------
# 5. Class with Multiple Methods
# -------------------------------------
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b

c = Calculator(4, 5)
print("5: Add:", c.add())
print("5: Multiply:", c.multiply())

# -------------------------------------
# 6. Class Inheritance
# -------------------------------------
class Animal:
    def speak(self):
        print("6: Animal speaks")

class Dog(Animal):
    def bark(self):
        print("6: Dog barks")

d = Dog()
d.speak()
d.bark()

# -------------------------------------
# 7. Class with Static Method
# -------------------------------------
class Math:
    @staticmethod
    def add(x, y):
        return x + y

print("7: Static Add:", Math.add(5, 7))

# -------------------------------------
# 8. Class with Class Method
# -------------------------------------
class Info:
    college = "AVIT"

    @classmethod
    def get_college(cls):
        return cls.college

print("8: College:", Info.get_college())

# -------------------------------------
# 9. Private Variable and Name Mangling
# -------------------------------------
class Secret:
    def __init__(self):
        self.__data = "Hidden Info"

    def show(self):
        print("9: Data:", self.__data)

sec = Secret()
sec.show()
# Access using name mangling (not recommended)
print("9: Accessed privately:", sec._Secret__data)

# -------------------------------------
# 10. Passing Object as Function Argument
# -------------------------------------
class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

def print_area(obj):
    print("10: Area is:", obj.area())

r = Rectangle(4, 5)
print_area(r)
