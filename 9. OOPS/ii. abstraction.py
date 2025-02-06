

##################---------------- Abstraction -----------------#####################
  
# Abstraction is the process of hiding complex implementation details and showing only the essential features of an object. 
# It focuses on what an object does rather than how it does it.
# In Programming: Abstract classes and interfaces are used to define a blueprint for other classes
#  without providing implementation details.





# Example:

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

#     def perimeter(self):
#         return 2 * 3.14 * self.radius

# circle = Circle(5)
# print(circle.area())  # Output: 78.5