
##################--------------- Encapsulation -------------------##################

# It restricts direct access to some of an object's  secret or private components,
#  which is a way of preventing unintended interference and misuse.



# Public attributes & methods :  These are normal attributes and can be accessible by outside of class.

# Private attributes & methods :  These are created to be used within the class and not accessible by outside of the class.

# Python uses naming conventions to indicate private or protected attributes/methods:
# _single_underscore: Protected (not enforced, just a convention).
# __double_underscore: Private (name mangling is applied to make it harder to access outside the class).






# Example:


# class person:
#     __name = "anonymous"        # Private attribute

#     def __init__(self, age):
#         self.age = age
    
# p1 = person(20)

# print(p1.age)
# print(p1.__name)                # Can't be accessed outside of class because the name is a private attribute.







# class person:
#     def __init__(self, name, age):
#         self.__name = name           # Private Attribute
#         self.age = age

#     def get_name(self):
#         return self.__name
    
# p1 = person("Ali", 20)

# print(p1.get_name())                 # Now by defining a method we can access the name but can't directly access outside of class.










# class person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age
    
#     def __hello(self):              # Private method.
#         return self.__name

# p1 = person("Ali", 20)

# print(p1.__hello())                 # Can't be accessed by outside of class as it is private method.













# class person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age

#     def __hello(self):                         # Private method.
#         return self.__name                     # Here a private attribute can be access because it is inside the class.
    
#     def welcome(self):
#         return f"Welcome {self.__hello()}"     # Here a private method can be accessed because it is inside the class.
    
# p1 = person("Ali", 20)

# print(p1.welcome())
    












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