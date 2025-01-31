

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




# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = person("Ali", 20)

# print(p1.name)
# print(p1.age)






# __str__() :  The __str__() function controls what should be returned when the class object is represented as a string.

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







