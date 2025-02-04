

###################---------- About Class --------------#####################

# 1. Class:
# A class is a blueprint or template for creating objects.
# It defines a set of attributes (data) and methods (functions) that the objects created from the class will have.
# A class is defined using the "class" keyword.


# Example of a class:

# class Dog:
#     # Class attribute (shared by all instances)
#     species = "Canis familiaris"

#     # Constructor method (initializes object attributes)
#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age    # Instance attribute

#     # Instance method
#     def bark(self):
#         return f"{self.name} says woof!"





###################---------- About Object --------------#####################


# 2. Object:
# An object is an instance of a class.
# When a class is defined, no memory is allocated until an object is created.
# Objects are created using the class name followed by parentheses (and arguments if required).


# Example of creating an object:

# # Creating an object of the Dog class
# my_dog = Dog("Buddy", 5)

# # Accessing attributes and methods
# print(my_dog.name)       # Output: Buddy
# print(my_dog.age)        # Output: 5
# print(my_dog.bark())     # Output: Buddy says woof!
# print(my_dog.species)    # Output: Canis familiaris







# Key Points:

# Class: A blueprint for creating objects.

# Object: An instance of a class with its own attributes and methods.

# Attributes: Variables that belong to an object or class.

# Methods: Functions that belong to an object or class.






###################---------- Constructor  __init__() function --------------#####################


# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, 
# or other operations that are necessary to do when the object is being created:




# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = person("Ali", 20)

# print(p1.name)
# print(p1.age)





###################---------- Constructor  __str__() function --------------#####################

#  The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:



# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name}({self.age})"

# p1 = person("Ali", 20)

# print(p1)
# print(str(p1))







###################---------- Instance Method --------------#####################

# Object Method : Objects can also contain methods. Methods in objects are functions that belong to the object.

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name}({self.age})"
    
#     def greet(self):
#         print(f"Hello, My name is {self.name}")

# p1 = person("Ali", 20)
# p1.greet()










###################---------- Modifing Object Attributes --------------#####################

# Modify object Properties :  We can modigy object properties like this.

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"{self.name}({self.age})"
    
# p1 = person("Ali", 20)

# print(p1.age)

# p1.age = 22

# print(p1.age)








###################---------- Deleting Object Attributes --------------#####################


# Deleting Object Properties :  We can delete object properties using "del" keyword.

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"{self.name}({self.age})"
    
# p1 = person("Aftab", 18)

# print(p1)

# del p1.age

# print(p1)            # It will throw an error because the age parameter is deleted.








###################---------- Deleting Object  --------------#####################

# Deleting an Object :  We can delete an object like this.

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"{self.name}({self.age})"

# p1 = person("Ali", 20)
# p2 = person("Aftab", 18)
# p3 = person("Taha", 18)

# print(p1)
# del p1

# print(p1)                    # It will throw an error because the the object p1 is deleted.










###################---------- Pass Statement --------------#####################

#  Pass Statement :  We can use "Pass" statement if the class is empty to avoid an error.

# class person:
#     pass



# class Dog:
#     species = "Canis familiaris"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def bark(self):
#         return f"{self.name} says woofs"

# my_dog  = Dog("buddy", 5)

# print(my_dog.bark())
# print(my_dog.species)
# print(my_dog.age)





# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.__balance = balance  # Private attribute

#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient funds")

#     def get_balance(self):
#         return self.__balance

# account = BankAccount("Alice", 1000)
# account.deposit(500)
# print(account.get_balance())  # Output: 1500





# class BankAccount:
#     def __init__(self, owner, balance = 0):
#         self.owner = owner
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print(f"Insufficent Balance")

#     def get_balance(self):
#         return self.__balance
    
# account = BankAccount("Aftab", 50000)

# print(account.get_balance())

# account.deposit(10000)

# print(account.get_balance())

# account.withdraw(4000)
# print(account.get_balance())







#########################------------- Types of Methods --------------###########################


# In Python, methods within a class can be categorized into three types based on how they interact with the class and its instances:

# 1. Instance Methods
# 2. Class Methods
# 3. Static Methods

# Here’s a detailed comparison of the three:

# 1. Instance Methods
# Definition: Instance methods are the most common type of methods in a class. 
# They operate on an instance of the class and have access to the instance's data (attributes) and other instance methods.

# First Argument: The first argument is always self, which refers to the instance of the class.

# Usage: Used to perform operations that involve instance-specific data.

# Calling: Can only be called on an instance of the class.

# Decorator: No decorator is needed (default behavior).



# Example:
 
# class MyClass:
#     def instance_method(self):
#         return f"Called instance_method of {self}"

# obj = MyClass()
# print(obj.instance_method())  # Output: Called instance_method of <__main__.MyClass object>



# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hi, My name is {self.name}")

# s1 = student("Ali", 20)

# s1.greet()












# 2. Class Methods
# Definition: Class methods operate on the class itself rather than on instances. 
# They can access and modify class-level data (class variables).

# First Argument: The first argument is always cls, which refers to the class (not the instance).

# Usage: Used for factory methods, alternative constructors, or operations that involve class-level data.

# Calling: Can be called on the class itself or on an instance of the class.

# Decorator: Defined using the @classmethod decorator.




# Example:
 
# class MyClass:
#     class_variable = 10

#     @classmethod
#     def class_method(cls):
#         return f"Called class_method of {cls}, class_variable = {cls.class_variable}"

# print(MyClass.class_method())  # Output: Called class_method of <class '__main__.MyClass'>, class_variable = 10




# class Dog:
#     species = "Canis"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def dog_type(cls):
#         print(f"The Type of Dog is {cls.species}")

# Dog.dog_type()
















# 3. Static Methods
# Definition: Static methods are independent of both the class and its instances.
#  They behave like regular functions but are defined within the class's namespace for organizational purposes.

# First Argument: No self or cls argument. They do not have access to instance or class-specific data.

# Usage: Used for utility functions that are logically related to the class but do not depend on instance or class state.

# Calling: Can be called on the class itself or on an instance of the class.

# Decorator: Defined using the @staticmethod decorator.




# Example:
 
# class MyClass:
#     @staticmethod
#     def static_method():
#         return "Called static_method"

# print(MyClass.static_method())  # Output: Called static_method








# Summary:

# Instance Methods: Work with instance-specific data (self).

# Class Methods: Work with class-level data (cls).

# Static Methods: Work independently of instance or class data.

# Choosing the right type of method depends on whether the functionality depends on instance data, class data, or neither.
 







# Example Combining All Three:
 
# class MyClass:
#     class_variable = 100

#     def __init__(self, instance_variable):
#         self.instance_variable = instance_variable

#     # Instance Method
#     def instance_method(self):
#         return f"Instance method: instance_variable = {self.instance_variable}"

#     # Class Method
#     @classmethod
#     def class_method(cls):
#         return f"Class method: class_variable = {cls.class_variable}"

#     # Static Method
#     @staticmethod
#     def static_method():
#         return "Static method: No access to instance or class data"

# # Instance Method
# obj = MyClass(10)
# print(obj.instance_method())  # Output: Instance method: instance_variable = 10

# # Class Method
# print(MyClass.class_method())  # Output: Class method: class_variable = 100

# # Static Method
# print(MyClass.static_method())  # Output: Static method: No access to instance or class data








