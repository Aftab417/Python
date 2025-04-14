

# Polymorphism
# Polymorphism helps in designing flexible system by allowing one interface to be use for different data types. Instead
# of writting seprate code for each data types, we write a generalized code that works for defferent objects.

# This increase flexibility, code reusability    and extensibility


# Polymorphism can be achieved by four methods:
# i.    Method Overriding
# ii.   Method Overloading
# iii.  Operator Overloading
# iv.   Functions using different objects with same methods





#####################------------   TYPES OF POLYMORHISM ---------------############################




#####################------------  Method Overriding  ---------------############################

# It occures when a child class provides specific implementation of method that is already defined in parent class.
# The method in child class must have  same name and parameters as the method in parent class.




# Example:

# class Animal:
#     def speak(self):
#         return "some generic sound"

# class Dog(Animal):
#     def speak(self):
#         return "Barks"

# class Cat(Animal):
#     def speak(self):
#         return "Meows"


# animals  = [Cat(), Dog(), Animal()]

# for animal in animals:
#     print(animal.speak())












# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def sound(self):
#         return f"{self.name} makes a sound"

# class Dog(Animal):
#     def sound(self):
#         return f"{self.name} Barks"

# class Cat(Animal):
#     def sound(self):
#         return f"{self.name} Meows"





# cat = Cat("Rex")
# dog = Dog("Whisker")

# print(cat.sound())
# print(dog.sound())







# def animal_sound(animal):
#     print(animal.sound())

# dog = Dog("Rex")
# cat = Cat("Whisker")

# animal_sound(dog)
# animal_sound(cat)


 













#####################------------  Method Overloading  ---------------############################

# Method Overloading in python can be done in three ways;
# i.   default arguments
# ii.  arbitrary arguments  (*argu)
# iii. conditional statements


# Example:

# Default arguments

# class Calculator:
#     def add(self, a, b, c = 0):
#         return a + b + c
    
# math = Calculator()

# print(math.add(2, 3))
# print(math.add(2, 3, 4))







# arbitrary arguments

# class calculator:
#     def add(self, *num):
#         return sum(num)

# math = calculator()

# print(math.add(2, 3))

# print(math.add(2, 3, 4, 5))

# print(math.add(2, 3, 5, 6, 6, 7))








# Conditional statement:

# class Printer:
#     def print_message(self, message = None):
#         if message is None:
#             print("No message provided")
#         else:
#             print(f"Message: {message}")

# p = Printer()

# p.print_message("Hello, world")





# class Display:
#     def show(self, value):
#         if isinstance(value, int):
#             print(f"Interger : {value}")
#         elif isinstance(value, float):
#             print(f"Float : {value}")
#         elif isinstance(value, str):
#             print(f"String : {value}")
#         else:
#             print("Unsupported data type")

# d = Display()
# d.show(5)
# d.show(5.3)
# d.show("Aftab")













#####################------------  Operator Overloading  ---------------############################

# Operator Overloading allows us to redefined the behaviour of operators (+, -, *, /)  when used with user-defined objects.
# Python allows Operators (+, -, *, /)  to be costomized for user-defined objects using dunder methods (magic methods)


# Magic Method for operators:

#   __add__()  ------>    +
#   __sub__()  ------>    -
#   __mul__()  ------>    *
#  __truediv__() ---->   /
#  __mod__()  ----->     %
#   __eq__()   ----->    ==
#  __ne__()    ----->    !=
#   __gt__()   ----->     >
#   __lt__()   ----->     <
#  





# Examples: 


# class point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return point(self.x + other.x, self.y + other.y)

# p1 = point(1, 3)
# p2 = point(4, 5)
# result = p1 + p2

# print(result.x, result.y)









# class Multipliar:
#     def __init__(self, value):
#         self.value = value

#     def __mul__(self, other):
#         return Multipliar(self.value * other)    

# m = Multipliar(5)

# result = m * 3
 
# print(m.value)

# print(result.value)









# class Box:
#     def __init__(self, volume):
#         self.volume = volume

#     def __gt__(self, other):
#         return self.volume > other.volume
    
# box1 = Box(50)
# box2 = Box(30)

# print(box1 > box2)
# print(box2 > box1)









# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __eq__(self, other):
#         return (self.name == other.name and self.age == other.age)
    
# p1 = Person("Aftab", 18)
# p2 = Person("Aftab", 18)
# p3 = Person("Taha", 20)

# print(p1 == p2)
# print(p1 == p3)













#####################------------ Polymorphism with Function and Objects  ---------------############################


# Python allows functions to use objects of different types as long as they have same method.



# Examples:


# class Birds:
#     def fly(self):
#         return f"Birds are flying"
    
# class Airplane:
#     def fly(self):
#         return f"Airplane is flying"
    
# class Rocket:
#     def fly(self):
#         return f"Rocket is flying"
    

# def make_it_fly(entity):
#     print(entity.fly())


# make_it_fly(Birds())
# make_it_fly(Airplane())
# make_it_fly(Rocket())











#####################------------  Real-world example of polymorphism  ---------------############################


# class Payment:
#     def pay(self):
#         pass

# class Creditcard(Payment):
#     def pay(self):
#         return f"Payment is made with Creditcard"
    
# class Paypal(Payment):
#     def pay(self):
#         return f"Payment is made with Paypal"
    
# class Bitcoin(Payment):
#     def pay(self):
#         return f"Payment is made with Bitcoin"
    

# def payment_process(payment_method):
#     print(payment_method.pay())


# payment_process(Creditcard())
# payment_process(Bitcoin())
# payment_process(Paypal())












# class Shape:
#     def draw(self):
#         raise NotImplementedError("Subclass must implement draw method")
    
# class Circle(Shape):
#     def draw(self):
#         return f"Drawing a circle"

# class Rectangle(Shape):
#     def draw(self):
#         return f"Drawing a Rectangle"
    
# class Triangle(Shape):
#     def draw(self):
#         return f"Drawing a Triangle"


# shapes = [Circle(),Rectangle(), Triangle()]

# for shape in shapes:
#     print(shape.draw())












# class Database:
#     def connect(self):
#         raise NotImplementedError("Subclass must implement the connect method")
    
# class Mysql(Database):
#     def connect(self):
#         return f"Mysql is connected"

# class MongoDB(Database):
#     def connect(self):
#         return f"MongoDB is connected"



# dbs = [Mysql(), MongoDB()]

# for db in dbs:
#     print(db.connect())









