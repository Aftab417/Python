
 
# Print all even numbers between 1 and 20.
 
# for x in range(0, 20, 2):
#     print(x)

# Alternative:
# for x in range(1, 20):
#     if x % 2 != 0:
#         continue
#     print(x)






# Print all odd numbers between 1 and 20.
# for x in range(1, 20, 2):
#     print(x)
 

# Alternative:
# for x in range(1, 20):
#     if x % 2 == 0:
#         continue
#     print(x)







# Calculate the sum of numbers from 1 to 100.

# sum = 0
# for x in range(1, 100):
#     sum += x
#     print(sum)


# Alternative:
# Total_sum = sum(x for x in range(1, 101)) 
# print(Total_sum)






# Print each character in the string "Python" using a loop.

# str = "Python"
# for x in str:
#     print(x)






# Print numbers from 10 to 1 in reverse order using a loop.

# i = 10
# while i >= 1:
#     print(i)
#     i -= 1

# for x in range(11, 1, -1):
#     print(x)





# Print the multiplication table of 5 using a loop.

# i = 1
# n = 5
# while i <= 10:
#     print(n * i)
#     i += 1


# Alternative:
# for x in range(1, 11):
#     print(x * 5)







# Keep asking the user for input until they type "exit".
 
# while True:
#     user_input = input("Enter something: ").lower().strip()
#     if user_input == "exit":
#         break
#     print(f"You Entered: {user_input} ")







 
# Print all numbers between 1 and 50 that are divisible by both 3 and 5.

# for x in range(1, 50):
#     if (x % 3 == 0 and x % 5 == 0):
#         print(x)

 





# Count the number of vowels in a given string.

# user_input = input("Enter something: ")
# cleaned_input = ''.join(user_input.lower().split())
# vol_count = 0
# for char in cleaned_input:
#     if char  in "aeiou":
#         vol_count += 1
# print(f"Vowel in your sting are {vol_count}.")        

 
# Alternative:

# user_input = input("Enter something: ").lower()
# vol_count = sum(1 for char in user_input if char in "aeiou")
# print(f"vowel in your string are {vol_count}")

 






 

# Create a multiplication table (from 1 to 10) for numbers 1 to 5.

# for x in range(1, 6):
#     for y in range(1, 11):
#         print(x * y)











# Write a programme to print the nums of following list.

# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for nums in list:
#     print(nums)


# Alternative:

# i = 0
# while i < len(list):
#     print(list[i])
#     i += 1







# Write a programme to find out the number x in the following tuple.

# tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = 49

# idx = 0

# for num in tuple:
#     if (num == x):
#         print("Found at index", idx)
#     idx += 1





# Alternative : 

# x = 49

# idx = 0
# while idx < len(list):
#     if(tuple[idx] == x):
#         print("found at index", idx)
#     idx += 1






# Print number from 1 to 100.

# for x in range(1, 100):
#     print(x)




# Print numbers from 100 to 1.

# for x in range(100, 0, -1):
#     print(x)






# Write a programme to print the table of number x.

# num = int(input("Enter a number: "))

# for x in range(1, 11):
#     print(x*num)





# Write a programme to print the sum of first 7 natural numbers.

# n = 7 
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print("Total sum is of number is :", sum)



# Alternative:

# n = 7

# sum = 0

# i = 0

# while i <= n:
#     sum += i
#     i += 1
# print("Total sum is ", sum)





# Write a programme to find out the factorial of first 5 natural numbers.

# n = 5

# fact = 1

# for x in range(1, n+1):
#     fact *= x
#     print("Factorial of numbers is ", fact)





# Alternaive : 

# n = 5

# fact = 1

# i = 1

# while i <= n:
#     fact *= i
#     i += 1
# print("Factorial of number is ", fact)










# write a programme to print all even number from 1 to 100.

# for x in range(1, 100, 2):
#     print(x)

# i = 1

# while i <= 100:
#     i += 1 
#     if (i % 2 == 0):
#         continue
# print(i)




# Print the factorial of a number entered by the user.
# num = int(input("Enter a number: "))
# fact = 1
# if num <= 0:
#     print("Enter a positive number.")
# else:
#     for x in range(1, num + 1):
#         fact *= x
# print(f"Factorial of {num} is {fact}")
    
 




# Generate the Fibonacci series up to 10 terms.
# num = int(input("Enter a number: "))
# a, b = 0, 1
# print(f"Fibonacce series for {num} is: ")
# while a <= num:
#     print(a, end=" ")
#     a, b = b, a + b


 




# Find the largest number in a list using a loop.
# user_input = input("Enter list of numbers sperated by space: ")
# numbers = [int(num) for num in user_input.split()]
# largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
# print(f"largest number in your list is {largest} ")

       
# Alternative:

# user_input = input("Enter a list of numbers:  ")
# numbers = [int(num) for num in user_input.split()]
# largest = max(numbers)
# print(largest)



# Reverse a string:

# string = input("Enter a string: ")
# reversed_string = string[::-1]
# for x in reversed_string:
#     print(x, end="")

# Alternative:
  
# string = input("Enter a string: ")  
# reversed_string = string[::-1]
# print(reversed_string)




# Reverse a string without using slicing.

# string = input("Enter a string: ")
# reversed_string = ''
# for x in string:
#     reversed_string = x + reversed_string
# print(reversed_string)     
   
 





# Print all prime numbers between 1 and 50.
# prime_num = []

# for num in range(2, 51):
#     is_prime = True
#     for x in range(2, int(num ** 0.5) + 1):
#         if num % x == 0:
#             is_prime = False
#             break
#     if is_prime:
#         prime_num.append(num)            
# print(prime_num)        


 




# Print the sum of digits of a given number.
# num = input("Enter a number: ")
# sum_digits = 0
# for x in num:
#     sum_digits += int(x)
# print(sum_digits)    

 

# Alternative:
# num = input("Enter a number: ")
# sum_digit = sum(int(digit) for digit in num)
# print(sum_digit)








# Count how many times each character appears in a given string.

# string = input("Enter a string: ")
# char_count = {}

# for char in string:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
# print(char_count)  


 











# Create a nested loop to print a 5x5 grid of numbers.

# for x in range(1, 6):
#     for y in range(1, 6):
#         print(y, end=" ")
#     print()

 




# Print numbers from 1 to 100, replacing multiples of 3 with "Fizz," multiples of 5 with "Buzz," and multiples of both with "FizzBuzz."

# for x in range(1, 100):
#     if x % 3 == 0 and x % 5 == 0:
#         print("FizzBuzz")
#     elif x % 3 == 0:
#         print("Fizz")
#     elif x % 5 == 0:
#         print("Buzz")
#     else:
#         print(x)

 




# # Check whether a given number is a palindrome.
# num = input("Enter a number: ")
# reverse_num = num[::-1]
# if num == reverse_num:
#     print(f"{num} is a palindrome")
# else:
#     print(f"number is not a palindrome")


 





# # Find and print all Armstrong numbers between 1 and 1000.
# for num in range(1, 1000):
#     num_string = str(num)
#     digit_num = len(num_string)    
#     digit_sum = sum(int(digit) ** digit_num for digit in num_string)
#     if digit_sum == num:
#         print(num)

 




# Alternative:

# for num in range(1, 1001):
#     digit_sum = sum(int(digit) ** len(str(num)) for digit in str(num))
#     if digit_sum == num:
#         print(num)
 







 


# Find the GCD (Greatest Common Divisor) of two numbers using loops.
# num1 = int(input('Enter a number: '))
# num2 = int(input('Enter second number: '))

# smaller = min(num1, num2)
# gcd = 1

# for x in range(1, smaller + 1):
#     if num1 % x == 0 and num2 % x == 0:
#         gcd = x
# print(gcd)


 



# Calculate the product of all elements in a list using a loop.
# user_input = input("Enter a list of number seprated by space:")
# num_list = [int(num) for num in user_input.split()]
# prod_list = 1
# for x in num_list:
#     prod_list *= x
# print(prod_list)


 


# Alternative:
# number_list = list(map(int, input("Enter a list of number seprated by space: ").split()))
# product = 1
# for num in number_list:
#     product *= num
# print(product)

 





# # Create a list of squares of numbers from 1 to 10 using a loop.
# square_list = []
# for num in range(1, 11):
#    square_list.append(num ** 2)
# print(square_list)
    
 

# square_list = [num ** 2 for num in range(1, 11)]
# print(square_list)


 








# Simulate a number guessing game where the user has 5 attempts to guess a random number.

# import random

# random_num = random.randint(1, 100)
# attempts = 5

# print(f"Welcome to the game.\nYou have {attempts} attempts to guess a random number betwwen 1 and 100.")

# for attempt in range(1, attempts + 1):
#     guess = int(input(f"Attempt {attempt}, Enter Your Guess Number: "))

#     if guess == random_num:
#         print(f"Congratulation! You have Guessed the right number.")
#         break
#     elif guess > random_num:
#         print(f"Too high. Try a lower number.")
#     elif guess < random_num:
#         print(f"Too Low. Try a greater number.")
#     if attempt == attempts:
#         print(f"Sorry You are Failed. The correct number is {random_num}")









# Create a program to determine whether a given number is a perfect number (sum of its divisors equals the number).

# num = int(input("Enter a Number: "))

# sum_divisor = 0

# for x in range(1, num // 2 + 1):
#     if num % x == 0:
#         sum_divisor += x
# if sum_divisor == num:
#     print(f"{num} is a perfect number.")
# else:
#     print(f"{num} is not a perfect number.")



# Print the following patteren:
# *
# **
# ***
# ****
# *****

# for x in range(1, 6):
#     print('*' * x)


# Print the following pattern:
# 1  
# 12  
# 123  
# 1234  
# 12345  

# rows = 5

# for x in range(1, rows + 1):
#     for y in range(1, x + 1):
#         print(y, end="")
#     print()
 


# Print the following pattern:
#     *  
#    ***  
#   *****  
#  *******  
# *********  

# rows = 5

# for i in range(1, rows + 1):
#     print(" " * (rows - i), end="")  
#     print("*" * (2 * i - 1))




# Generate a diamond pattern like this:
#    *  
#   ***  
#  *****  
# *******  
#  *****  
#   ***  
#    *  



# Input: Number of rows for the upper half of the diamond
# n = int(input("Enter the number of rows for the upper half: "))

# # Upper half of the diamond
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

# # Lower half of the diamond
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

 