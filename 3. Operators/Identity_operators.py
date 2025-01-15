# Identity operators are used to compare the objects, not if they are equal,
#  but if they are actually the same object, with the same memory location.

#################------------- is ------------#######################
# "is" operator : It return True if two object are same. Return False if two object are not same

# a = 5
# b = a
# print(a is b)   # True
# print(b is a)   # True

# a =  5
# b =  5
# print(a is b)    # True


# a = 5
# b = "5"
# print(a is b)     # False

# a = ["banana", "orange", "mango"]
# b = ["banana", "orange", "mango"]
# print(a is b)     # False

# a = ("banana", "orange", "mango")
# b = ("banana", "orange", "mango")
# print(a is b)
  

# a = {"name": "Aftab", "age": 17}
# b = {"name": "Aftab", "age": 17}
# print(a is b)    # False

# a = {"orange", "banana", "mango"}
# b = {"orange", "banana", "mango"}
# print(a is b)    # False



#################------------- is not------------#######################

# is not : It return True if two object are not same. Return False if two object are same.

# a =  5
# b =  "5"
# print(a is not b) # True

# a = 5
# b = 5
# print( a is not b ) # False