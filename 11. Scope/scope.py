
######################---------------  Scope --------------------#######################

# A variable is available from inside the region it is created. This is called scope in python.



######################---------------  Local Scope --------------------#######################

# A variable created inside a function belongs to the local scope of function. It can only be used by inside of this function.


# Example:


# def my_function():
#     x = 300                        # Local Scope
#     print(x)

# my_function()




# Note:    Local scope variable can be used by the function inside the main function.


# Example:

# def my_function():
#     x = 300

#     def my_inner_function():
#         print(x)

#     my_inner_function()    

# my_function()     











######################---------------  Global Scope --------------------#######################

# A variabl created in the main body of python code is called a global variable and belongs to global scope. Global scope can be used by anyone and can be accessed by anywhere.


# Example:


# x = 300                      # Global Scope

# def my_function():

#     print(x)

# my_function()


# print(x)














######################---------------  Naming Variable --------------------#######################

# If you operate with the same variable name inside and outside of a function.  Python will take both as seprate variable.



# Example:


# x = 300                           # Global Scope

# def my_function():

#     x = 200                       # Local Scope
#     print(x)

# my_function()


# print(x)










######################---------------  Global Keyword --------------------#######################


#  We can change the scope of local variable into global using global keyword.


# Example:


# def my_function():

#     global x
#     x = 300

#     print(x)

# my_function()    


# print(x)














