

# Create a simple Car class with attributes brand and model, and a method display_info() to print these details. # Create an object of the Car class and call its method.


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def display_info(self):
#         return f"Brand: {self.brand},  Model: {self.model}"
    
# car1 = Car("Toyota", "Civic")

# print(car1.display_info())














# Create a class Person with a private attribute __age. Add a method to get and set the value of __age using getter and setter methods.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age


#     @property
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self, new_age):
#         if isinstance(new_age, int):
#             self.__age = new_age
#         else:
#             raise TypeError("Value must be an integer.")


# p1 = Person("Aftab", 17)

# print(p1.age)

# p1.age = 18

# print(p1.age)




 








# Create a Circle class with an instance method area() that returns the area of the circle.

# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)

# c1 = Circle(5)

# print(c1.area())














# Define a class with a class method and static method. Explain the difference between them in your code comments.


# class Student:
#     class_grade = 12

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def print_class_grade(cls):
#         print(cls.class_grade)

#     @staticmethod
#     def welcome():
#         print(f"You are welcome")

# s1 = Student("Aftab", 17)

# print(s1.name)

# s1.print_class_grade()

# s1.welcome()



















#  Create a class BankAccount with private attributes __balance. Implement methods to deposit and withdraw money while ensuring balance doesn’t go negative.


# class BankAccount:
#     def __init__(self, owner, balance= 0):
#         self.owner = owner
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"{amount} is successfully deposited to your account.")
#         else:
#             print(f"Amount must be positive.")


#     def withdraw(self, amount):
#         if amount > self.__balance:
#             print("Insufficent Balance!")
#         else:
#             self.__balance -= amount
#             print(f"You have made another withdraw of {amount}")

#     def get_balance(self):
#         print(self.__balance)


# account = BankAccount("Aftab", 100000)

# account.get_balance()
# account.deposit(10000)
# account.get_balance()
# account.withdraw(50000)
# account.get_balance()













# Implement a Student class with instance attributes name and marks. Use @classmethod to keep track of the total number of students.


# class Student:
#     total_students = 0

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         Student.student_increment()

#     @classmethod
#     def student_increment(cls):
#         cls.total_students += 1

#     @classmethod
#     def get_total_student(cls):
#         return cls.total_students
    

# s1 = Student("Aftab", 98)
# s2 = Student("Taha", 99)

# print(Student.get_total_student())











# Create an abstract class Shape with an abstract method area(). Inherit it in Rectangle and Circle classes and implement area().

# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
    
#     @abstractmethod
#     def area(self):
#         pass
        


# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__()
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)


# class Rectangle(Shape):
#     def __init__(self, length, width):
#         super().__init__()

#         self.length = length
#         self.width = width

#     def area(self):
#         return  self.length * self. width


# r1 = Rectangle(5, 5)
# c1 = Circle(5)

# print(r1.area())
# print(c1.area())













# Implement multiple inheritance by creating a class Employee and another class Manager, and then derive a class TeamLead from both.

# class Manager:
#     def authority(self):
#         return f"Has authority to assign tasks to others."



# class Employee:
#     def resposibility(self):
#         return f"Has resposibility to complete task on time."


# class Teamlead(Manager, Employee):
#     pass


# t1 = Teamlead()

# print(t1.authority())
# print(t1.resposibility())







# Alternative:

# class Employee:
#     def __init__(self, name, ID):
#         self.name = name
#         self.ID = ID

#     def show_details(self):
#         return f"Name: {self.name}, ID: {self.ID}"
    

# class Manager:
#     def __init__(self, name, department):
#         self.name = name
#         self.department = department

#     def show_department(self):
#         return f"Manages Department: {self.department}"


# class Teamlead(Employee, Manager):
#     def __init__(self, name, ID, department, Team_size):
#         Employee.__init__(self, name, ID)
#         Manager.__init__(self, name, department)

#         self.Team_size = Team_size

#     def show_Teamsize(self):
#         return f"Leads a team of {self.Team_size} members."


# tl = Teamlead("Aftab", 365, "DevOps", 10)

# print(tl.show_details())
# print(tl.show_department())
# print(tl.show_Teamsize())













# Implement a hierarchical inheritance where Mammal is the parent class and Dog and Cat are child classes.

# class Mammal:
#     def feed_method(self):
#         return f"Feed his childs with milk."
    

# class Cat(Mammal):
#     pass

# class Dog(Mammal):
#     pass


# cat = Cat()
# dog = Dog()

# print(cat.feed_method())
# print(dog.feed_method())






# Alternative:

# class Mammel:
#     def __init__(self, name):
#         self.name = name

#     def characteristics(self):
#         return f"{self.name} is a warm blodded mammel."

# class Dog(Mammel):
#     def sound(self):
#         return f"{self.name} says Woof Woof!"
    
# class Cat(Mammel):
#     def sound(self):
#         return f"{self.name} says Meow Meow!"
    


# dog = Dog("Whisker")
# cat = Cat("Rex")

# print(dog.sound())
# print(dog.characteristics())

# print(cat.sound())
# print(cat.characteristics())













 
# Implement a hybrid inheritance structure using at least four classes.

# class A:
#     def method_A(self):
#         print("Method_A")

# class B(A):
#     def method_B(self):
#         print("Method_B")


# class C(A):
#     def method_C(self):
#         print("Method_C")


# class D(B, C):
#     def method_D(self):
#         print("Method_D")



# d = D()

# d.method_A()
# d.method_B()
# d.method_C()
# d.method_D()






# Alternative:

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def show_name(self):
#         print(f"Name: {self.name}")


# class Mammel(Animal):
#     def __init__(self, name, is_warm_blodded = True):
#         super().__init__(name)

#     def show_characteristics(self):
#         print(f"{self.name} is a warm blodded animal.")


# class Birds(Animal):
#      def fly(self):
#          print(f"{self.name} can fly")


# class Bat(Mammel, Birds):
#     def show_ability(self):
#         print(f"{self.name} is a Mammel that can fly.")


# bat = Bat("Batty")

# bat.show_name()
# bat.show_characteristics()
# bat.fly()
# bat.show_ability()

















# Create a Vehicle class with a max_speed attribute. Use method overriding in Car and Bike subclasses to display different speed limits.


# class Vehicle:
#     def __init__(self, max_speed):
#         self.max_speed = max_speed

#     def show_speed_limit(self):
#         print(f"General Vehicle speed limit is {self.max_speed} KM/h")


# class Bike(Vehicle):
#     def show_speed_limit(self):
#         print(f"General Bikes speed limit is {self.max_speed} KM/h")


# class Car(Vehicle):
#     def show_speed_limit(self):
#         print(f"General Car speed limit is {self.max_speed} KM/h")


# bike = Bike(120)
# car = Car(350)


# car.show_speed_limit()
# bike.show_speed_limit()

















# Implement operator overloading for + in a Vector class to add two vectors.


# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
    
#     def __str__(self):
#         return f"{self.x}, {self.y}"


# v1 = Vector(5, 8)
# v2 = Vector(3, 6)
# v3 = v1 + v2

# print(v3)












# Implement operator overloading for == in a Point class to compare two points.


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         if isinstance(other, Point):
#             return self.x == other.x and self.y == other.y
#         else:
#             return False


# p1 = Point(4, 5)
# p2 = Point(4, 5)
# p3 = Point(2, 3)

# print(p1 == p2)














# Demonstrate method overloading using default arguments in Python.


# class Calculator:
#     def add(self, a, b, c=0):
#         return a + b + c
    
# calcu = Calculator()

# print(calcu.add(2, 3, 4))
# print(calcu.add(2, 3))














# Create a Person class and override the __str__ method to return a meaningful string representation.


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Name: {self.name}  Age: {self.age}"


# p1 = Person("Aftab", 18)

# print(p1)













# Implement a method where a function operates on different objects having the same method name.


# class Bird:
#     def fly(self):
#         return "Birds are flying."
    

# class Airplane:
#     def fly(self):
#         return "Airplane is flying"


# class Rocket:
#     def fly(self):
#         return "Rocket is flying"


# def can_fly(obj):
#     print(obj.fly())


# can_fly(Bird())
# can_fly(Airplane())
# can_fly(Rocket())





# Alternative:

# class Dog:
#     def sound(self):
#         return f"Woof Woof"
    

# class Cat:
#     def sound(self):
#         return f"Meow Meow"
    

# class Cow:
#     def sound(self):
#         return f"Moo Moo"
    

# def animal_sound(animal):
#      print(animal.sound())
    

# dog = Dog()
# cat = Cat()
# cow = Cow()


# animal_sound(dog)
# animal_sound(cat)
# animal_sound(cow)


















# Create a Smartphone class with a __battery_life private attribute and define getter, setter, and deleter methods.


# class Smartphone:
#     def __init__(self, brand, battery_life):
#         self.brand = brand
#         self.__battery_life = battery_life

    
#     @property
#     def battery_life(self):
#         return self.__battery_life
    

#     @battery_life.setter
#     def battery_life(self, new_value):
#         if not isinstance(new_value, (int, float)) or new_value < 0:
#             raise ValueError(f"Battery_life must be a positive value.")
#         self.__battery_life = new_value


#     @battery_life.deleter
#     def battery_life(self):
#         confirm = input("Do you really want to delete battery_life value? (Yes/No): ")
#         if confirm.lower() == "yes":
#             print(f"Battery_life value is deleted.")
#             del self.__battery_life
#         else:
#             print(f"Deletion canceled!")
        
       
# phone = Smartphone("IPhone", "4 Hours")

# print(phone.battery_life)

# phone.battery_life = 90

# print(phone.battery_life)

# del phone.battery_life













# Create a program that maintains a list of different shapes (Circle, Square, Triangle) and uses polymorphism to call the area() method on each object.




# import math

# class Shape:
#     def area(self):
#         pass


# class Triangle(Shape):
#     def __init__(self, base, height):
#         super().__init__()
#         self.base = base
#         self.height = height

#     def area(self):
#         return 1/2 * (self.base * self.height)



# class Square(Shape):
#     def __init__(self, side):
#         super().__init__()
#         self.side = side

#     def area(self):
#         return self.side * self.side
    


# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__()
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)




# tri = Triangle(4, 6)

# squ = Square(5)

# cir = Circle(5)



# shapes = [tri, squ, cir]

# for shape in shapes:
#     print(f"{shape.__class__.__name__} area: {shape.area()}")














# Implement a class that enforces encapsulation strictly using private attributes and only allows controlled access via methods.


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age

#     def show_age(self):
#         return f"The age is {self.__age} Year."
    

# p1 = Person("Aftab", 18)
# print(p1.show_age())





# Alternative:

# class Secure_data:
#     def __init__(self, data):
#         self.__data = data

#     def get_data(self):
#         return self.__data
    
#     def set_data(self, new_data):
#         if not isinstance(new_data, str):
#             raise ValueError('Data must be a string value')
#         self.__data = new_data

#     def delete_data(self):
#         del self.__data
#         print("The secret data is deleted.")


# data_obj = Secure_data("This is secret data")

# print(data_obj.get_data())

# data_obj.set_data("This is new secret data.")

# print(data_obj.get_data())

# data_obj.delete_data()