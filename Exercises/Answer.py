
# Write a program to swap the values of two variables without using a third variable.

# a = 5
# b = 10

# a = b + a
# b = a - b
# a = a - b

# print(a, b)




# Assign values to three variables and calculate their average.

# a = 5
# b = 4
# c = 2

# aver = (a + b + c) / 3
# print(aver)




# Write a program to store the radius of a circle in a variable and calculate its area (πr²) and circumference (2πr). Use 3.14 for π.
# radius = float(input("Etner radius of circle: "))
# area = 3.14 * (radius ** 2)
# circum = 2 * 3.14 * radius
# print(f"Area = {area}, Circumference = {circum}")





# Create a program to store your first and last name in two variables and print your fullname.
# first_name = input("Enter your first name: ")
# last_name = input("Etner your last name: ")

# full_name = first_name+ " " +last_name
# print(full_name)










# Create a program to check whether a number is even or odd using the modulus operator (%).

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")



# Write a Python program to calculate the square and cube of a number using the exponent operator (**).

# num = int(input("Enter a number: "))
# print(f"Square of {num} is {num ** 2} and Cube of {num} is {num ** 3}")




# Take two numbers as input and compare them using relational operators (>, <, ==, !=, >=, <=). Print the results.

# a = int(input("Enter first number: "))
# b = int(input("Etner second number: "))

# if a > b:
#     print(f"{a} > {b}")
# elif a < b:
#     print(f"{a} < {b}")
# else:
#     print(f"{a} = {b}")







# Write a Python program to swap two numbers using arithmetic operations (addition and subtraction).
# a = 5
# b = 10

# a = a + b
# b = a - b
# a = a - b
# print(a , b)



# Write a program to calculate the area of a triangle using the formula:
# base = int(input("Enter the base of triangle: "))
# height = int(input("Enter the height of triangle: "))

# area = 1/2 * (base * height)
# print(area)



# Develop a program to find whether a given number is divisible by both 3 and 5 using logical operators (and, or, not).
# num = int(input("Enter a number: "))
# if num % 3 == 0 and num % 5 == 0:
#     print(f"{num} is divisible by both 3 and 5")
# elif num % 3 == 0:
#     print(f"{num} is divisible by 3")
# elif num % 5 == 0:
#     print(f"{num} is divisible by 5")
# else:
#     print(f"{num} is not divisible by both 3 and 5")




# Create a program that checks if a number is positive and even, negiitive and odd using logical operators.

# num = int(input("Enter a number: "))
# if num > 0:
#     if num % 2 == 0:
#         print(f"{num} is Positive and even.")
#     else:
#         print(f"{num} is Positive and Odd")
# else:
#     if num % 2 == 0:
#         print(f"{num} is Negative and even")
#     else:
#         print(f"{num} is Negative and odd")





# Write a Python program to calculate the total marks, percentage, and average of 5 subjects entered by the user.
# subjects = ["English", "Math", "Biology", "Chemistery", "Physics"]
# sub_marks = []
# for sub in subjects:
#     marks = float(input(f"Enter Marks for {sub}: "))
#     sub_marks.append(marks)
# print(f"Your Total marks are: {sum(sub_marks)}")
# print(f"Your average marks are: {sum(sub_marks) / len(sub_marks)}")
# print(f"Your Percentage Marks are: {sum(sub_marks) / 500 * 100}")






# Develop a program that takes the price of an item and applies a discount percentage to calculate the final price.
# price = float(input("Enter price for item: "))
# disc_per = float(input("Enter Percentage discount: "))
# discount_amout = disc_per / 100 * price
# final_price = price - discount_amout
# print(f"Final price after discount is {final_price}")





# Store the length and width of a rectangle in two variables and calculate its area and perimeter.

# len = float(input("Enter the length of rectangle: "))
# width = float(input("Enter the width of ractangle: "))

# area = len * width 
# perimeter = 2 * (len + width)
# print(f"Area of rectangle is {area}")
# print(f"Perimeter of rectangle is {perimeter}")



# Write a program to store the price of an item and the sales tax percentage in variables. Calculate and print the total price after tax.

# price = float(input("Enter the price for item: "))
# tax_per = float(input("Enter the tax percentage: "))
# tax_amount = tax_per / 100 * price
# final_price = price + tax_amount
# print(f"Final price after tax is {final_price}")









# Convert the following data type into other:
# a. Integer 5 into a string.
# a = 5
# b = str(a)
# print(type(b))


# b. String "123" into an integer.
# a = "1234"
# b = int(a)
# print(type(b))


# c. Float 3.14 into an integer.
# a = 3.14
# b = int(a)
# print(type(b))



# d. List [1, 2, 3] into a tuple.
# num = [1, 2, 3, 4]
# number = tuple(num)
# print(number)
# print(type(number))




# Write a Python program to check whether a given variable is a list, tuple, set, or dictionary and print its type.
# var1 = "string"
# var2 = [1,2,3,4]
# var3 = (1,2,3,4)
# var4 = {1, 3, 23, 3}
# var5 = {"name": "Aftab", "age": 17}

# def check_type(variable):
#     if isinstance(variable, list):
#         print("Variable is a list.")
#     elif isinstance(variable, tuple):
#         print("Variable is a tuple.")
#     elif isinstance(variable, dict):
#         print("Variable is a dictionary.")
#     elif isinstance(variable, set):
#         print("Variable is Set.")
#     else:
#         print("Variable is string.")
# check_type(var1)
# check_type(var2)
# check_type(var3)
# check_type(var4)
# check_type(var5)






# Write a Python program to create a dictionary with three key-value pairs. Retrieve the value of a specific key and add a new key-value pair.
# data = {
#     "Name": "Aftab",
#     "Age": 17,
#     "Religion": "Islam"
# }

# print(data["Name"])
# print(data["Age"])
 









# Question:
# data = {
#     "name": "John",
#     "age": 25,
#     "skills": ["Python", "Django", "Machine Learning"],
#     "projects": [
#         {"title": "E-commerce", "completed": True},
#         {"title": "AI Chatbot", "completed": False}
#     ]
# }

# Tasks:
# Access the value "Django" from the skills list.
# print(data["skills"][1])


# Add a new skill, "React", to the skills list.
# data["skills"].append("React")
# print(data)

# Update the status of the "AI Chatbot" project to True.
# data["projects"][1]["completed"] = True
# print(data)

# Add a new project, "Portfolio Website", with a completion status of False.

# data["projects"].append({"titlle": "Portfolio", "completed": "False"})
# print(data)








 

# # Question:
# items = [10, "apple", 3.14, "banana", 5, "42"]

# # Tasks:
# # Separate the integers, floats, and strings into different lists.
# # Sort each list individually and print the results.
# integers = []
# strings = []
# floats = []
# for item in items:
#     if isinstance(item, int):
#         integers.append(item)
#     elif isinstance(item, float):
#         floats.append(item)
#     else:
#         strings.append(item)

# integers.sort()
# floats.sort()
# strings.sort()

# print(integers)
# print(floats)
# print(strings)







# Question:
# students = {
#     "Alice": {"age": 20, "grade": 85},
#     "Bob": {"age": 22, "grade": 90},
#     "Charlie": {"age": 21, "grade": 78}
# }

# Tasks:
# Calculate the average age of all students.
# total_age = sum(student["age"] for student in students.values())
# students_num = len(students)
# average_age = total_age / students_num
# print(average_age)



# Find the student with the highest grade.
# highest_grade = max(student["grade"] for student in students.values())
# print(highest_grade)


# Add a new student, "David", with age 23 and grade 88.
# students.update({"David": {"age": 23, "grade": 88}})
# print(students)



# Question:
# Write a Python function that swaps the values of two variables using tuple unpacking.
# a = 5
# b = 4
# a, b = b, a
# print(a, b)






# # Question:
# sentence = "Practice makes a person perfect"

# # Tasks:
# # Create a list of words from the string.
# word_list = sentence.split(" ")
# print(word_list)


# # Generate a list of word lengths.
# word_len = [len(words) for words in word_list]
# print(word_len)


# # Create a dictionary where keys are words and values are their lengths.
# data =  dict(zip(word_list, word_len))
# print(data)




# # Question:
# set1 = {2, 4, 6, 8, 10}
# set2 = {3, 6, 9, 12, 15}

# # Tasks:
# # Find elements that are in either set but not both.
# # symmetrical_diff = set1 ^ set2
# # print(symmetrical_diff)


# # Remove all elements divisible by 3 from set2.
# # set2 = {x for x in set2 if x % 3 != 0}
# # print(set2)


# # Check whether set1 is a subset of set2.
# # print(set1.issubset(set2))



# # Question:
# data = [
#     {"name": "Alice", "scores": [85, 92, 88]},
#     {"name": "Bob", "scores": [78, 81, 86]},
#     {"name": "Charlie", "scores": [89, 91, 84]}
# ]

# # Tasks:
# # Calculate and print the average score for each student.
# # alice_average = sum(score for score in data[0]["scores"]) / len(data[1]["scores"])
# # print(alice_average)
# # bob_average = sum(score for score in data[1]["scores"]) / len(data[1]["scores"])
# # print(bob_average)
# # charlie_average = sum(score for score in data[2]["scores"]) / len(data[1]["scores"])
# # print(charlie_average)



# # Identify the student with the highest average score.
# # highest_average = max(alice_average, bob_average, charlie_average)
# # print(f"Higest average scores is {highest_average}")







# Write a program that checks if a number is positive.
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(f"{num} is positive.")



# Write a program that checks if a number is even or odd.
# num = int(input("Enter a number: "))
# if num % 2 == 2:
#     print(f"{num} is Even.")
# else:
#     print(f'{num} is Odd.')




# Write a program that checks if a number is positive, negative, or zero.
# num = int(input("Enter a number: "))
# if num == 0:
#     print("Number is zero.")
# elif num > 0:
#     print("number is Positive.")
# else:
#     print("number is Negative.")


# Write a program to check the grade of a student (A for 90-100, B for 80-89, C for 70-79, D for 60-69, F for below 60).
# marks = float(input("Enter Your Marks:"))
# if marks >= 90 and marks <= 100:
#     print("Your grade is A")
# elif marks >= 80 and marks < 90:
#     print("Your grade is B")
# elif marks >= 70 and marks < 80:
#     print("Your grade is C")
# elif marks >= 60 and marks < 70:
#     print("Your grade is D")
# else:
#     print("Your grade is F")



# Write a program to check if a number is divisible by 5 and 10.
# num = int(input("Enter a number."))
# if num % 10:
#     print("Number is divisible by both 5 and 10")
# else:
#     print("Number is not divisible by both 5 and 10.")



# Write a program that checks if a person is eligible to vote (age >= 18).
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to Vote.")
# else:
#     print("You are not eligible to Vote")







# Write a program to check if a year is a leap year.
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a learp year.")




# Write a program to check if a number is prime.
# num = int(input("Enter a number: "))

# if num > 1:
#     is_prime = True
#     for x in range(2, int(num ** 0.5) + 1):
#         if num % x == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(f"{num} is a prime number.")
#     else:
#         print(f"{num} is not a prime number.")
# else:
#     print(f'{num} is not a prime number.')







# # Write a program that finds the largest of three numbers
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# # if num1 > num2 and num1 > num3:
# #     print(f"{num1} is greater number.")
# # elif num2 > num3:
# #     print(f"{num2} is greater number")
# # else:
# #     print(f"{num3} is greater number.")



# # Alternative:
# largest_number = max(num1, num2, num3)
# print(f"Your largest number is {largest_number}")






# Write a program that checks if a number is a palindrome (reads the same backward).
# num = input("Ente a number:")
# reversed_number= num[::-1]
# if num == reversed_number:
#     print(f"{num} is palindrome.")
# else:
#     print(f"{num} is not a palindrome.")




# Write a program that checks if a character is a vowel or consonant.
# char = input("Enter an alphabet character: ").lower()
# if char in "aeiou":
#     print(f'{char} is vowel')
# else:
#     print(f"{char} is consonent")



# Write a program to check if a number is an Armstrong number (e.g., 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153).

# num = int(input("Enter a number: "))
# sum_digit = sum(int(digit) ** len(str(num)) for digit in str(num))
# if sum_digit == num:
#     print(f"{num} is an armstronge number.")
# else:
#     print(f"{num} is not an armstronge number.")









# Write a program that calculates the sum of digits in a number.
# num = input("Enter a number: ")
# sum_digit = sum(int(digit) for digit in num)
# print(sum_digit)





# Write a program to print the Fibonacci series up to a specified number.
# num = int(input("Enter a number: "))
# a, b = 0, 1
# print(f"Fibonnaci series up to {num}")

# while a <= num:
#     print(a, end=" ")
#     a, b = b, a + b





# Write a program that checks if a string is a palindrome (reads the same backward).
# string = input("Enter a string: ")
# cleaned_string = ''.join(string.lower().split())
# reversed_string = cleaned_string[::-1]
# if reversed_string == cleaned_string:
#     print(f"String is palindrome.")
# else:
#     print(f"String is not a palindrome.")






# Write a program to find the factorial of a number  with conditional statements.
# num = int(input("Enter a number: "))
# fact = 1
# for x in range(1, num + 1):
#     fact *= x
# print(fact) 




# Write a program to check if a number is perfect (the sum of its divisors equals the number itself).
# num = int(input("Enter a number: "))
# sum_divisors = sum(int(digit) for digit in range(1, int(num // 2) + 1) if num % digit == 0)
# if sum_divisors == num:
#     print(f"{num} is a perfect number.")
# else:
#     print(f"{num} is not a perfect number.")



# Write a program to validate a password by checking if it contains at least one uppercase letter, one lowercase letter, one digit, and is at least 8 characters long.

# passwd = input("Enter Your Password: ")

# if len(passwd) < 8:
#     print("Password must contain at least 8 character.")
# elif not any(char.isdigit()for char in passwd):
#     print("Password must contain at least one numaric charcter.")
# elif not any(char.isupper()for char in passwd):
#     print("Password must contain at least one Upper case letter.")
# elif not any(char.islower()for char in passwd):
#     print("Password must contain at least one lower case letter.")
# else:
#     print("Password is correct")










# Print all even numbers between 1 and 20.
# for x in range(0, 20, 2):
#     print(x)

# x = 1
# while x < 20:
#     x += 1
#     if x % 2 != 0:
#         continue
#     print(x)





# Print all odd numbers between 1 and 20.
# for x in range(1, 20, 2):
#     print(x)

# x = 1
# while x < 20:
#     x += 1
#     if x % 2 == 0:
#         continue
#     print(x)



# Calculate the sum of numbers from 1 to 100.
# sum = 0
# for x in range(1, 101):
#     sum += x
#     print(sum)
    


    



# Print each character in the string "Python" using a loop.
# string = "Python"
# for x in string:
#     print(x)




# Print numbers from 10 to 1 in reverse order using a while loop.
# for x in range(10, 0, -1):
#     print(x)

# i = 10
# while i > 0:
#     print(i)
#     i -= 1


# Print the multiplication table of 5 using a while loop.
# for x in range(1, 11):
#     print(x * 5)


# i = 1
# while i <= 10:
#     print(i * 5)
#     i += 1




# Keep asking the user for input until they type "exit".

# while True:
#     user_input = input("Enter something: ").lower()
#     if user_input == "exit":
#         break
#     print(user_input)
    




# Print all numbers between 1 and 50 that are divisible by both 3 and 5.
# for x in range(1, 51):
#     if x % 5 == 0 and x % 3 == 0:
#         print(x)




# Count the number of vowels in a given string.
# string = input("Enter a String: ").lower()
# vol_count = 0
# for x in string:
#     if x in "aeiou":
#         vol_count += 1
# print(vol_count)







# Create a multiplication table (from 1 to 10) for numbers 1 to 5.
# for x in range(1, 6):
#     for y in range(1, 11):
#         print(x * y)







# Print the factorial of a number entered by the user.
# num = int(input("Enter a number: "))
# fact = 1
# for x in range(1, num + 1):
#     fact *= x
# print(fact)





# Generate the Fibonacci series up to 10 terms.
# a,b = 0,1
# while a <= 10:
#     print(a, end=" ")
#     a, b = b, a + b




# Find the largest number in a list using a loop.
# user_input = list(map(int, input("Enter a list of number sprated by space: ").split()))
# largest = user_input[0]
# for x in user_input:
#     if x > largest:
#         largest = x
# print(largest)




# Reverse a string without using slicing.
# string = input("Enter a string: ")
# reversed_string = ''
# for x in string:
#     reversed_string  = x + reversed_string
# print(reversed_string)




# Print all prime numbers between 1 and 50.
# for num in range(1, 51):
#     is_prime = True
#     for x in range(2, int(num // 2) + 1):
#         if num % x == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)








# Print the sum of digits of a given number.
# num = input("Enter a number: ")
# digit_sum = sum(int(digit) for digit in num)
# print(digit_sum)





# Count how many times each character appears in a given string.
# string = input("Enter a string: ")
# cleaned_string = ''.join(string.lower().split())
# data = {}

# for char in cleaned_string:
#     if char in data:
#         data[char] += 1
#     else:
#         data[char] = 1
# print(data)





# Create a nested loop to print a 5x5 grid of numbers.
# for x in range(1, 6):
#     for y in range(1, 6):
#         print(y,end=" ")
#     print()





# Print numbers from 1 to 100, replacing multiples of 3 with "Fizz," multiples of 5 with "Buzz," and multiples of both with "FizzBuzz."
# for x in range(1, 101):
#     if x % 5 == 0 and x % 3 == 0:
#         print("Fizzbuzz")
#     elif x % 3 == 0:
#         print("Fizz")
#     elif x % 5 == 0:
#         print("Buzz")
#     else:
#         print(x)




 




# Find and print all Armstrong numbers between 1 and 1000.
# for num in range(1, 1001):
#     digit_sum = sum(int(digit) ** len(str(num)) for digit in str(num))
#     if digit_sum == num:
#         print(num)




# Find the GCD (Greatest Common Divisor) of two numbers using loops.
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# smaller_num = min(num1, num2)
# gcd = 1
# for x in range(1, smaller_num + 1):
#     if num1 % x == 0 and num2 % x == 0:
#         gcd = x
# print(gcd)




# Simulate a number guessing game where the user has 5 attempts to guess a random number.
# import random
# random_number = random.randint(1, 100)

# attempts = 5

# for attempt in range(1, attempts + 1):
#     guess = int(input(f"Attempt {attempt} Enter Your Guess Number: "))
#     if guess == random_number:
#         print(f"Congratulation! You have guessed the correct number.")
#         break
#     elif guess < random_number:
#         print("Too small. Try a larger one.")
#     elif guess > random_number:
#         print("Too large. Try a smaller one")
#     if attempt == attempts:
#         print(f"Sorry You are Failed. The correct number is {random_number}")




# Calculate the product of all elements in a list using a loop.
# user_input =  list(map(int, input("Enter a list of number seprated by space: ").split()))
# product = 1
# for num in user_input:
#     product *= num
# print(product)




# Create a list of squares of numbers from 1 to 10 using a loop.
# square_list = [num ** 2 for num in range(1, 11)]
# print(square_list)
 



# Print the following patteren:
# *
# **
# ***
# ****
# *****

# n = 5
# for x in range(1, n + 1):
#     print("*" * x)


# print the following patteren
# 1  
# 12  
# 123  
# 1234  
# 12345 

# n = 5
# for x in range(1, n + 1):
#     for y in range(1, x + 1):
#         print(y, end="")
#     print()





# Print the following pattern:
#     *  
#    ***  
#   *****  
#  *******  
# *********  

# n = 5
# for x in range(1, n + 1):
#     print(" " * (n - x) + "*" * (2 * x - 1))




# Generate a diamond pattern like this:
#    *  
#   ***  
#  *****  
# *******  
#  *****  
#   ***  
#    *  

# n = int(input("Enter a number: "))

# for x in range(1, n + 1):
#     print(" " * (n - x) + "*" * ( 2 * x - 1))
# for x in range(n-1, 0, -1):
#     print(" " * (n - x) + "*" * (2 * x - 1))