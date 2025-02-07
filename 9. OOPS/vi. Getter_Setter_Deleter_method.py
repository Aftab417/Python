

####################---------------- Getter Method ---------------####################

# The Getter method is used to retreive the value of private attribute. It allows controlled access to an attribute without directly exposing it.

# Decorator :  @property ,  This decorator make the geeter method to be accessed as simple variable.


# Example : 


# class Person:
#     def __init__(self, name):
#         self._name = name                  # Private Attribute.

#     @property
#     def name(self):
#         return self._name
    
# p1 = Person("Aftab")

# print(p1.name)                           # Accessing private attribute as simple variable due to getter method.















####################---------------- Setter Method ---------------####################


# Definaion:  It is used to securely modify the  private attribute  While applying logic and validation before assignment.

# Decorator:  @<property-name>.setter     


# Example:


# class Person:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, new_name):
#         if len(new_name) < 2:
#             raise ValueError("The name must contain at least two letters.")
#         else:
#             self._name = new_name


# p1 = Person("Aftab")

# print(p1.name)

# p1.name = "Taha"

# print(p1.name)

# p1.name = "h"

# print(p1.name)















####################---------------- deleter Method ---------------####################


# A deleter mathod is used to delete an attribute safely when nedded. But is delete attribute after confirmation.

# Decorator:   @<property-name>.deleter



# class Person:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, new_name):
#         if len(new_name) < 2:
#             raise ValueError("The name must contain at leaset two letters.")
#         self._name = new_name

#     @name.deleter
#     def name(self):
#         confirm = input("Do you want to delete the name? yes/no: ")
#         if confirm.lower() == "yes":
#             print("Name is deleted")
#             del self._name
#         else:
#             print("Delete canceled.")

# p1 = Person("Aftab")

# print(p1.name)
# p1.name = "Ali"
# print(p1.name)
# del p1.name














####################---------------- Examples with all three Methods ---------------####################


 

 









# class Example:
#     def __init__(self, value):
#         self._value = value

#     @property
#     def value(self):
#         return self._value
    
#     @value.setter
#     def value(self, new_value):
#         if new_value < 0:
#             raise ValueError("The value must be Positive.")
#         else:
#             self._value = new_value

#     @value.deleter
#     def value(self):
#         confirm = input("Are you sure you want to delete the value? (yes/no): ")
#         if confirm.lower() == "yes":
#             print("Value is Deleted")
#             del self._value
#         else:
#             print("Deletion canceled.")


# v1 = Example(20)

# print(v1.value)

# v1.value = 30

# print(v1.value)

# del v1.value













# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self._balance = balance

#     @property
#     def balance(self):
#         return self._balance
    
#     @balance.setter
#     def balance(self, amount):
#         if amount < 0:
#             raise ValueError("The must be positive.")
#         self._balance = amount

#     @balance.deleter
#     def balance(self):
#         confirm = input(f"Are you sure you want ot delete the balance record or {self.account_holder}? (yes/no): ")
#         if confirm.lower() == "yes":
#             print(f"{self.account_holder}'s balance is deleted.")
#             del self._balance

# account = BankAccount("Aftab", 10000)

# print(account.balance)

# account.balance = 20000

# print(account.balance)

# del account.balance













# class Employee:
#     MIn_Salary = 15000
#     def  __init__(self, name, salary):
#         self.name = name
#         self._salary = max(salary, self.MIn_Salary)

#     @property
#     def salary(self):
#         return self._salary
    
#     @salary.setter
#     def salary(self, new_salary):
#         if new_salary < self.MIn_Salary:
#             print(f"Salary must be greater than {self.MIn_Salary}")
#         else:
#             self.salary == new_salary

#     @salary.deleter
#     def salary(self):
#         confirm = input(f"Are you sure you want ot delete {self.name}'s salary record? (yes/no): ")
#         if confirm.lower() == "yes":
#             print(f"{self.name}'s salary records are deleted.")
#             del self._salary
#         else:
#             print("Deletion Canceled.")
        

# emp = Employee("Aftab", 700000)

# print(emp.salary)

# emp.salary = 1000000

# print(emp.salary)

# del emp.salary
        












# class student:
#     def __init__(self, name, grade):
#         self.name = name 
#         self._grade = self.validate_grade(grade)

#     def validate_grade(self, grade):
#         if 0 <= grade <= 100:
#             return grade
#         else:
#             raise ValueError("The grade must be between 0 and 100")
        
#     @property
#     def grade(self):
#         return self._grade
    
#     @grade.setter
#     def grade(self, new_grade):
#         self._grade = self.validate_grade(new_grade)

#     @grade.deleter
#     def grade(self):
#         confirm = input(f"Are you sure you want to delete {self.name}'s grade records? (yes/no): ")
#         if confirm.lower() == "yes":
#             print(f"{self.name}'s grade records are deleted.")
#             del self._grade
#         else:
#             print("Deletion canceled.")

# s1 = student("Aftab", 100)

# print(s1.grade)

# s1.grade = 99

# print(s1.grade)

# del s1.grade












































# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"Point({self.x}, {self.y})"

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

# p1 = Point(1, 2)
# p2 = Point(3, 4)
# p3 = p1 + p2
# print(p3)  # Output: Point(4, 6)