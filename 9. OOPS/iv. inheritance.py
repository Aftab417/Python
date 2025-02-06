
# Inheritance : Inheritance allows us to build a class that inherit all the properties and methods from another class.

# Parent Class : It is the class that is being inherithed. It is also called base class.

# Child class : It is the class that inherit from another class. It is also called derived class.



# Example:



# Parent class:

# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

#     def printname(self):
#         print(f"Hello, {self.fname} {self.lname}")

# p1 = Person("Aftab", "Ahmad")

# # p1.printname()






# Child class:

# class Student(Person):                     # When we want to inherit from another class we pass the name of parent class as argument in child class.
#     pass                                   # if we don't want to add anyother method or properties we use 'pass' statement.

# s1 = Student("Taha", "Sultan")

# s1.printname()









# We can add __init__() Function to chile class. But when we add __init__() to child class it will no longer take __init__() properties of parent class.

# class Student(Person):
#     def __init__(self, fname, lname):

         



# To keep the inheritnace to the parent's  __init__() Function add a call to parent __init__()


# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)













#  Super() Function :   Python also have super function that will make the child class to inherite all the properties and method from their parents.

# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

#     def printname(self):
#         print(f"Hello, {self.fname} {self.lname}")



# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)                  # To inherit parent __init__()

# s1 = Student("Aftab", "Ahmad")

# s1.printname()











#  Adding Properties in Child class :   We add __init__() in child class so that we can add properties and method to child class that are not in parent class.

# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

#     def printname(self):
#         print(f"Hello, {self.fname} {self.lname}")

# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year                     # Adding a new property to child class

# s1 = Student("Aftab", "Ahmad", 2029)

# s1.printname()
# print(s1.graduationyear)









# Adding methods to child class :  We can also extra methods to child class and use them.


# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

#     def printname(self):
#         print(f"Hello, {self.fname} {self.lname}")


# class Student(Person):
#     def __init__(self, fname, lname, age):
#         super().__init__(fname, lname)
#         self.age = age

#     def welcome(self):                                         # Adding a new method to child class.
#         print(f"Welcome, {self.fname} {self.lname}")


# s1 = Student("Aftab", "Ahmad", 18)

# s1.welcome()

# print(s1.age)












# Examples :



# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"{self.name} makes a sound."


# class Dog(Animal):  # Inherits from Animal
#     def speak(self):
#         return f"{self.name} barks."


# class Cat(Animal):  # Inherits from Animal
#     def speak(self):
#         return f"{self.name} meows."


# dog = Dog("Rex")
# cat = Cat("Whiskers")
# print(dog.speak())  # Output: Rex barks.
# print(cat.speak())  # Output: Whiskers meows.

 








# class Car:
#     def __init__(self, name):
#         self.name = name

#     @staticmethod
#     def start():
#         print("Car is Started.")

#     @ staticmethod
#     def stop():
#         print("Car is Stoped")


# class ToyotaCar(Car):
#     pass

# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Prius")


# print(car1.name)
# print(car2.name)

# car1.start()
# car2.stop()










#####################------------  Types of Inheritance  -----------------#########################

# There are Five types of Inheritance.


#####################------------  Single Inheritance  -----------------#########################

#  A child class inherits from a single parent class.



# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def sound(self):
#         print(f"Make some sound")




# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def sound(self):
#         print(f"{self.name} Barks")

# dog = Dog("Buddy")

# dog.sound()









#####################------------  Multiple Inheritance  -----------------#########################

# A child class Inherits from  more than one parent class.

# class Father:
#     def skill(self):
#         print("Driving")


# class Mother:
#     def hobby(self):
#         print("Painting")


# class baby(Father, Mother):
#     pass

# c1 = baby()

# c1.skill()
# c1.hobby()











#####################------------  Multilevel Inheritance  -----------------#########################


# A child class inherits from another child class creating a chain.


# class Grandparents:
#     def legacy(self):
#         print('Family Values.')


# class Parents(Grandparents):
#     def wisdom(self):
#         print("Experience")


# class Child(Parents):
#     pass


# c1 = Child()

# c1.legacy()
# c1.wisdom()










#####################------------  Heirarchical Inheritance  -----------------#########################


#  Multiple child  classes inherits from  a single parent class.


# class Parents:
#     def profession(self):
#         print("Doctor")


# class Child1(Parents):
#     pass


# class Child2(Parents):
#     pass


# c1 = Child1()
# c2 = Child2()

# c1.profession()
# c2.profession()











#####################------------  Hybrid Inheritance  -----------------#########################


# It is the combination of two or more types of inheritance.

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

# obj = D()

# obj.method_A()
# obj.method_B()
# obj.method_C()
# obj.method_D()
