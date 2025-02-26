

################--------------- Common Built-in Exceptions in Python ----------------#####################

# Here are some common built-in exceptions in python.


######################----------------- ZeroDivisionError  ----------------#############################

# Raised When dividing by zero.


# try:
#     num = int(input("Enter a number: ")) 
#     result = 10/num
#     print(f"Result: {result}")
# except ZeroDivisionError:
#     print(f"Division by zero is not allowed.")








######################----------------- ValueError  ----------------#############################

# Raised when a function gets an invalid argument (e.g: converting "abc" into integer.) 




# try:
#     num =  int(input("Enter a number: "))
#     print(f"You entered: {num}")

# except ValueError:
#     print("Invalid input! Please enter an integer value.")     











######################----------------- TypeError  ----------------#############################

# Raised when an operation is applied to an incompatible data type (e.g: adding a string and interger.)


# try:
#     word = "hello"
#     print(word + 23)

# except(TypeError) as e:
#     print(e)










######################----------------- FileNotFoundError  ----------------#############################

# Raised when trying to open a file that does not exist.


# try:
#     with open("file.txt", "r") as f:
#         print(f.read())

# except FileNotFoundError:
#     print("Error: File does not exist.")        











######################----------------- FileExistError  ----------------#############################

# Raised when trying to create a file that already exist.


# with open("hello.txt", "x") as f:
#     print("File is successfully created.")



# try:
#     with open("hello.txt", "x") as f:
#         print("File successfully created.")

# except FileExistsError:
#     print('File already exists.')











######################----------------- importError  ----------------#############################

# Raised when an imported module is not found.



# try:
#     from flask import Flask

# except (ImportError) as e:
#     print(e)    






# try:
#     from flask import Flask

# except ImportError:
#     print("Module is not found.")











######################----------------- NameError  ----------------#############################


# Raised when trying to use a variable that is not defined.

# try:
#     print(x)

# except (NameError) as e:
#     print(e)    





# try:
#     print(z)

# except NameError:
#     print("x is not defined.")    











######################----------------- IndexError  ----------------#############################


# Raised when trying to access index in list or tuple that does not exist.


# my_list  = ["hello", "Aftab", "Taha"]

# try:
#     print(my_list[5])

# except(IndexError) as e:
#     print(e)  





# try: 
#     print(my_list[5])

# except IndexError:
#     print("List index is out of range.")  











######################----------------- keyError  ----------------#############################

# Raised when trying to access a key in a dict that does not exist:

# my_dict = {
#     "Name" : "Aftab",
#     "class" : 12
# }


# try:
#     print(my_dict["city"])

# except KeyError:
#     print("Key not found!") 











######################----------------- indentationError  ----------------#############################

# Raised when indentation is not correct.


# try:
#     def my_function():
#     print("hello")    

# except(IndentationError) as e:
#     print(e)     













######################----------------- AttributeError  ----------------#############################


# Raised when an trying to access an attribute that is not defined in an object. 











######################----------------- RuntimeError  ----------------#############################


#  A general error that occure during a program execution.



# try:
#     def recursive_function():
#         return recursive_function()  

#     recursive_function() 


# except (RuntimeError) as e:
#     print(e)







# try:
#     def recursive_function():
#         return recursive_function()  

#     recursive_function() 


# except RuntimeError:
#     print("Maximum recursion depth exceed.")



