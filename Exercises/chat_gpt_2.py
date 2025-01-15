
######################--------------- Operator ------------------####################

# Write a program to add, subtract, multiply, divide, and find the remainder of two numbers entered by the user.

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# print("Sum of two numbers is : ", a + b)
# print("Difference of two numbers is : ", a - b)
# print("Product of two numbers is : ", a * b)
# print("Division of two numbers is : ", a / b)
# print("Reminder of two numbers is : ", a % b)
 




# Create a program to check whether a number is even or odd using the modulus operator (%).

# num = int(input("Enter an integer: "))
# if(num % 2 == 0):
#     print("Number is even")
# else:
#     print("Nember is odd")\






# Write a Python program to calculate the square and cube of a number using the exponent operator (**).

# num = float(input("Enter a number: "))
# squre = num ** 2
# cube = num ** 3

# print(f"Square of {num} is {squre}")
# print(f"Cube of {num} is {cube}")






# Take two numbers as input and compare them using relational operators (>, <, ==, !=, >=, <=). Print the results.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if(a < b):
#     print(f"{a} is less then {b}")
# elif(a > b):
#     print(f"{a} is greater than {b}")
# else:
#     print(f"{a} is equal to {b}")





# Write a program to calculate the area of a triangle using the formula:

# base = float(input("Enter the base of triangle: "))
# height = float(input("Enter the height of triangle: "))

# area = 1/2 * (base * height)

# print(f"Area of triangle is {area}")







# Develop a program to find whether a given number is divisible by both 3 and 5 using logical operators (and, or, not).

# num = int(input("Enter a number: "))

# if(num % 3 == 0 and num % 5 == 0):
#     print(f"{num} is divisible by both 3 and 5")
# else:
#     print(f"{num} is not divisible by both 3 and 5")





# Write a Python program to swap two numbers using arithmetic operations (addition and subtraction).

# a = int(input("Enter the value of a : "))
# b = int(input("Enter the value of b : "))

# a = a + b
# b = a - b
# a = a - b

# print("After swaping the values are:")
# print("a :", a)
# print("b :", b)






# Create a program that checks if a number is positive and even, negiitive and odd using logical operators.

# num = float(input('Enter a number: '))

# if num > 0:
#     if num % 2 == 0:
#         print(f"{num} is positive and even")
#     else:
#         print(f"{num} is positive and odd")
# elif num < 0:
#     if num % 2 == 0:
#         print(f"{num} is negitive and even")
#     else:
#         print(f"{num} is negitive and odd")
# else:
#     print(f"{num} is zero, which is neither positive nor negitive. It is a neutral number.")







# Write a Python program to calculate the total marks, percentage, and average of 5 subjects entered by the user.

# phy = float(input("Enter Physics marks out of 100: "))
# bio = float(input("Enter Biology marks out of 100: "))
# che = float(input("Enter Chemistry marks out of 100: "))
# math = float(input("Enter Math marks out of 100: "))
# eng = float(input("Enter English marks out of 100: "))


# total_marks = phy + che + bio + eng + math 
# average_marks = (phy + che + bio + eng + math ) / 5
# percentage = (total_marks / 500) * 100


# print(f"Your Total_marks are : {total_marks}")
# print(f"Your percentage is {percentage}%")
# print(f"Average of marks is {average_marks}")








# # Develop a program that takes the price of an item and applies a discount percentage to calculate the final price.


# price = float(input("Enter the price of item: "))
# discount = float(input("Enter discount percentage: "))

# discount_amount = (discount / 100) * price
# total_price = (price - discount_amount)

# print(f"\nOriginal price of item is: {price:.2f}$")
# print(f"percentage discount applied is: {discount:.2f}%")
# print(f"Discout amount is: {discount_amount:.2f}$")
# print(f"Total price after discount is: {total_price}")