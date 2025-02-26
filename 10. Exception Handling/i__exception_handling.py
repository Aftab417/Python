

################## -----------  Exception Handling ---------------###################

# Exception Handling in python is a mechnism that allows a program to handle runtime errors gracefully without crashing
# It helps in detecting and responding to unexpected errors in code, such as zero divison error,  invalid input  or file not found error
# python uses try-except block to handle the error. The code that may cause an xception is placed in try block and potential errors
# are handled in except block.






# Key components:

#  try  Block:   Contains the code that might cause and exception
#  except Block:  Handle the exception if it occure
#  finally Block: Execute whether exception occure or not     ------>   (optional)  
#  else  Block:   Execute if no exception occure              ------>   (optional)






# Example:


# try:
#     num = int(input("Enter a number: "))
#     result = 10 /num                      # can cause zero division error  or invalid input
#     print(f"Result: {result}")

# except ZeroDivisionError:
#     print(f"Nunber must be greater than zero")
# except ValueError:
#     print(f"Invalid syntax! Please enter an interger. ")
# finally:
#     print("Execution completed")








# try:
#     num = int(input("Enter a number: "))
#     print(f"You Entered: {num}")

# except ValueError:
#     print("Please Enter an integer.")
# else:
#     print("No error occured.")   









# try:
#     with open("file.txt", "r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("Error:  File not found.")
# else:
#     print("No error occured.")    















#########################--------------  Types of Exception Handling --------------##############################

# Python provides different ways to handle exceptions.



#########################--------------  Handling a specific exception --------------##############################

# We can catch specific exception using multiple except block.



# try:
#     num = int(input("Enter a number:"))
#     result = 10 / num
#     print(f"Result: {result}")

# except ValueError:
#     print("Invalid syntax! Please enter an integer value.")
# except ZeroDivisionError:
#     print("Number must be greater than zero.")
# else:
#     print("No error occured.")
# finally:
#     print("Execution completed.")








#########################--------------  Handling Multiple exceptions in one except block --------------##############################

# We use a tuple to handle multiple exception types in a single except block.



# try:
#     num = int(input("Enter a number: ")) 
#     result = 10/num
#     print(f"Result: {result}") 

# except(ZeroDivisionError, ValueError) as e:
#     print(f"Error: {e}")

# else:
#     print("No Error occured.")










#########################-------------- Raising Custom Exception "raise" Keyword  --------------##############################

# We can manyally triger an exception using "raise" keyword without using tyr-except blocks.




# age = int(input("Enter you age: "))

# if age < 18:
#     raise ValueError("Your age must be greater than 18.")
# else:
#     print("No error occured.")









#########################-------------- Custom Exception class  --------------##############################

# We can create  custom exceptions by inheriting from exception class.



# class NegativeNumberError(Exception):
#     pass


# try:
#     num = int(input("Enter a number: "))

#     if num < 0:
#         raise NegativeNumberError("Negative numbers are not allowed.")
    
# except (NegativeNumberError) as e:
#     print(e)  




