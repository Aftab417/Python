
# # Write a program that checks if a number is positive.
# num = float(input("Enter a number: "))
# if num > 0:
#     print("Yes number is positive")






# Write a program that checks if a number is even or odd

# num = float(input("Enter a number: "))
# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")







# Write a program that checks if a number is positive, negative, or zero.
# num = float(input("Enter a number: "))
# if num > 0:
#     print(f"{num} is positive")
# elif num < 0:
#     print(f"{num} is negative.")
# else:
#     print(f"{num} is Neutral.")








# #  Write a program to check the grade of a student (A for 90-100, B for 80-89, C for 70-79, D for 60-69, F for below 60).
# marks = float(input("Enter your marks to check the grade: "))

# if (marks >= 90 and marks <= 100):
#     print("Your grade is A")
# elif(marks >=80 and marks < 90):
#     print("Your grade is B")
# elif(marks >=70 and marks < 80):
#     print("Your grade is C")
# elif(marks >= 60 and marks < 70):
#     print("Your grade is D")
# elif(marks >= 0 and marks < 60):
#     print("Your grade is F")
# else:
#     print("Enter marks 0 to 100")









# # Write a program to check if a number is divisible by 5 and 10.

# num = int(input("Enter an integer: "))

# if (num % 5 == 0 and num % 10 == 0):
#     print(f"{num} is Divisible by 5 and 10")
# else:
#     print(f"{num} is not divisible by both 5 and 10")










# # # Write a program that checks if a person is eligible to vote (age >= 18).

# age = input("Enter Your Age: ")

# if age.isdigit():
#     age = int(age)
#     if age >= 18:
#         print("You are eligible to vote")
#     else:
#         print("You are not eligible to vote")
# else:
#     print("Pleae enter a valid age")









# #  Write a program to check if a year is a leap year.  A leap year is divisible by 4 and also by 400 and not by 100.

# year = input("Enter a Year: ")

# if year.isdigit():
#     year = int(year)
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(f"{year} is a leap year")
#     else:
#         print(f"{year} is not a leap year")
# else:
#     print("invalid syntax")










# Write a program to check if a number is prime.
 
# num = int(input("Enter a number: "))
# if num > 1:
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#     if is_prime:
#         print(f"{num} is a prime number.") 
#     else:
#         print(f"{num} is not a prime number")  
# else:
#     print(f"{num} is not a prime number.")              

 








# # Write a program that finds the largest of three numbers.
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))

# if num1 > num2 and num1 > num3:
#     print(f"{num1} is largest number.")
# elif num2 > num3:
#     print(f"{num2} is largest number.")
# else:
#     print(f"{num3} is largest number. ")


# Alternative:

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))

# largest = max(num1, num2, num3)
# print(f"largest number is {largest}")












# Write a program that checks if a number is a palindrome (reads the same backward).

# num = input("Enter a number.")

# if num == num[::-1]:
#     print(f"{num} is palindrome")
# else:
#     print(f"{num} is not a palindrome.")









#  Write a program that checks if a character is a vowel or consonant.
# letter = input("Enter an alphabet character: ").lower()

# if letter in "aeiou":
#     print(f"{letter} is a vowel.")
# elif letter.isalpha():
#     print(f"letter is a consonent.")
# else:
#     print(f"invalid syntax")
 











# For a number with  𝑛 digits, if the sum of each digit raised to the power n equals the number itself, then it is an Armstrong number.

# Write a program to check if a number is an Armstrong number

# num = int(input("Enter a number: "))
# num_str = str(num)
# num_digit = len(num_str)

# sum_powers = sum(int(digit) ** num_digit for digit in num_str)

# if sum_powers == num:
#     print(f"{num} is an Armstrong number.")
# else:
#     print(f"{num} is not an Armstrong number.")













# Write a programme to check if a number entered by the user is odd or even.

# num = int(input("Enter a Number: "))
# if num % 2 == 0:
#     print(num, "is Even.")
# else:
#     print(num, "is Odd.")











# Write a programme to find out the largest of 3 values.

# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))
# c = int(input("Enter Third Number: "))

# if (a > b and a > c):
#     print("First value is largest") 
# elif(b > a and b > c):
#     print("second value is largest")
# elif(c > a and c > b):
#     print("Third value is largest")
    

# Alternative Method:


# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))
# c = int(input("Enter Third Number: "))

# if (a > b and a > c):
#     print("First value is largest") 
# elif(b > c):
#     print("second value is largest")
# else:
#     print("Third value is largest")











# Write a programme to find out the largest of four values.

# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))
# c = int(input("Enter Third Number: "))
# d = int(input("Enter Fourth Number:"))

# if (a > b and a > c and a > d):
#     print("First value is largest") 
# elif(b > c and b > d):
#     print("second value is largest")
# elif(c > d):
#     print("Third value is largest")
# else:
#     print("Fourth value is largest")











# Write a programme to find out the number is multiple of 7 or not.

# num = int(input("Enter a number: "))
# if (num % 7== 0):
#     print(num, "is multiple of 7")
# else:
#     print(num , "is not a multiple of 7")













# Write a program that calculates the sum of digits in a number.

# num = input("Enter a number: ")
# sum_digit = 0

# for digit in num:
#     if digit.isdigit():
#         sum_digit += int(digit)
# print(sum_digit)


# Alternative

# sum_digit = sum(int(digit) for digit in num if num.isdigit())
# print(f"sum of digit of given number is: {sum_digit}")


 


# Write a program to print the Fibonacci series up to a specified number.

# num = int(input("Enter number to print Fibonacci series up to: "))
# a, b = 0, 1
# print(f"Fibonacci series up to {num}: ")

# while a <= num:
#     print(a, end=" ")
#     a, b = b, a + b


 



#  Write a program that checks if a string is a palindrome (reads the same backward).
# string = input("Enter to check palindrome or not: ") 

# cleaned_string = ''.join(string.lower().split())
# if cleaned_string == cleaned_string[::-1]:
#     print("String is Palindrome")
# else:
#     print("String is not a palindrome.")








# Write a program that takes a number and checks if it is between 10 and 50, between 51 and 100, or above 100.
# num = int(input("Enter a number: "))

# if num >= 0 and num <= 50:
#     print(f"{num} is between 0 and 50")
# elif num > 50 and num <= 100:
#     print(f"{num} is between 50 100.")
# else:
#     print(f"{num} is above 100.")







# Write a program that checks a student's grade and prints "Excellent" for A, "Good" for B, "Average" for C, and "Fail" for others.

# grade = input("Enter Your Grade: ").strip().lower()

# if grade == "a":
#     print("Excellent")
# elif grade == "b":
#     print("Good")
# elif grade == "c":
#     print("Average")
# else:
#     print("Fail")



# Alternative:

# grade = input("Enter Your Grade: ").strip().lower()

# grades = {
#     "a" : "Excellent",
#     "b" : "Good",
#     "c" : "Average",
# }

# print(grades.get(grade, "Fail" ))









# Write a programme input the color of light and tell the user what to do on trafic signal.

# light = input("Enter color of light: ")
# if (light == "red"):
#     print("Stop")
# elif(light == "yellow"):
#     print("Ready to Go.")
# elif(light == "green"):
#     print("You can Go.")
# else:
#     print("Signal light is not working.")












# Write a programme to check either a person can vote or not.

# age = int(input("Enter Your Age: "))
# if (age >= 18):
#     print("You can Vote.")
# else:
#     print("You can not Vote.")














# Write a programme to tell the student grade based on his marks.

# marks = float(input("Enter Your Marks: "))
# if (marks >= 90):
#     print("You grade is A")
# elif(90 > marks >= 80):
#     print("Your grade is B")
# elif(80 > marks >= 70):
#     print("Your grade is C")
# elif(70 > marks >= 60):
#     print("Your grade is D")
# else:
#     print("Your grade is E")


# Alternative Method.

# marks = float(input("Enter Your Marks: "))
# if (marks >= 90):
#     print("You grade is A")
# elif(marks >= 80 and marks < 90):
#     print("Your grade is B")
# elif(marks >=70 and marks < 80):
#     print("Your grade is C")
# elif(marks >= 60 and marks < 70):
#     print("Your grade is D")
# else:
#     print("Your grade is E")

















# Write a program to find the factorial of a number using conditional statements.

# num = int(input("Enter a number to find the factorial: "))

# fact = 1

# if num <= 0:
#     print("please enter a positive number.")
# else:
#     for i in range(1, num + 1):
#         fact *= i
# print(f"Factorial of {num} is {fact}")


 




# Write a program to check if a number is perfect (the sum of its divisors equals the number itself).

# num = int(input("Enter a number: "))

# sum_divisors = 0

# if num <= 0:
#     print("please enter a positive number.")
# else:
#     for i in range(1, num // 2 + 1):
#         if num % i == 0:
#             sum_divisors += i

# if sum_divisors == num:
#     print(f"{num} is a perfect number.")
# else:
#     print(f"{num} is not a perfect number.")



 








# Write a program to validate a password by checking if it contains at least one uppercase letter, one lowercase letter, one digit, and is at least 8 characters long.

# passwd = input("Enter Your Password: ")

# if not len(passwd) >= 8:
#     print("Password must contain at least 8 characters.")
# elif not any(char.isupper() for char in passwd):
#     print("Password must contain at least one capital letter.")
# elif not any(char.islower() for char in passwd):
#     print("Password must contain at least one small letter")
# elif not any(char.isdigit() for char in passwd):
#     print("Password must contain at least one numaric charcter.")
# else:
#     print("Password is Valid.")


 