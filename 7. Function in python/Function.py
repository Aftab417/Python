
# Function: It is a block of code that only run when it is called. We can pass some data in function which is called parameter. Function return some output which is called result.


# def print_hello():               # Function defination
#     print("Hello World")
# print_hello()                    # Function call





# Parameter: A parameter is a variable listed inside the parantheses in function defination.
# Arguments: An argument is the value that is sent to the function when it is called.

# def calc_sum(a, b):               # a, b  are parameters.
#     sum = a + b
#     print(sum)
#     return sum
# calc_sum(6, 3)
# calc_sum(5454, 3423)              # 5454, 3423 are arguments.


# def my_function(fname, lname):
#     print(fname+ " " +lname)
# my_function("Aftab", "Ahmad")
# my_function("Taha", "Sultan")
# my_function("Haider", "Ali")



# def calc_aver(a, b, c):
#     sum = a + b + c
#     avr = sum / 3
#     print(avr)
#     return avr
# calc_aver(65, 34, 43)







# Arbitrary Arguments: If you don't know how many arguments that will be passed into your function, add a "*" before your parameter name in the function defination.
# in this way function will receive the tuple of arguments, and then access the value accordingly

# def myfunction(*kids):
#     print("The youngest child is " + kids[2])
# myfunction("ali", "ahmad", "haider", "taha")




# Keyword Arguments: You can send arguments in key = value  syntax. In this way the order of arguments does not matter.

# def my_function(child1, child3, child2):
#     print("The youngest chiled is " + child3)
# my_function(child3= "ali", child2= "ahmad", child1= "haider")





# Arbitrary keyword Argument: if you don't know how many keyword argument that will be passed into your function you can add "**" before parameter name.

# def my_function(**kids):
#     print("The youngest child is " + kids["fname"])
# my_function(fname = "Taha", lname = "Sultan")




# Default parameter value: The following example show if we pass nothing in arguments how function use default value.

# def country_name(country = "Pakistan"):
#     print("I am from " + country)
# country_name("swedon")
# country_name("Japan")
# country_name()
# country_name("Austrlia")





# # List as Argument:

# def my_function(food):
#     for x in fruits:
#         print(x)

# fruits = ["banana", "orange", "mango", "apple"]
# my_function(fruits)






# Return Statement: To let a function return a value. Use return statement.

# def my_function(x):
#     return 5 * x
# print(my_function(3))


# def calc_square(num):
#     return num ** 2
# print(calc_square(4))


# def get_detail(name, age):
#     return name, age
# print(get_detail("ali", 15))


