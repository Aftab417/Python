
# Write a function named greet() that prints "Hello, World!" when called.

# def greet():
#     print("Hello")
#     return
# greet()

 
 
# Write a function named add_numbers(a, b) that returns the sum of two numbers passed as arguments.

# def add_num(a, b):
#     print(a + b)
#     return
# add_num(3, 5)


 


# Create a function is_even(number) that returns True if the given number is even, and False otherwise.

# def is_even(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#     return
# is_even(int(input("Enter a number: ")))

 



# Alternative:

# def is_even(number):
#     return number % 2 == 0

# num = int(input("Enter a number: "))

# if is_even(num):
#     print("Even")
# else:
#     print("Odd")


 
 


# Write a function square(num) that takes a number as input and returns its square.

# def square(num):
#     return num ** 2
# num = int(input("Enter a number: "))
# print(f"The square of {num} is {square(num)}")

 

# Alternative: 

# def square(num):
#     return num ** 2
# print(square(int(input("Enter a number: "))))

 

 

# Define a function multiply_list(numbers) that multiplies all the numbers in a list and returns the result.

# def multiply_list(numbers):
#     product = 1
#     for num in numbers:
#         product *= num
#     return product
# numbers = [3, 4, 2, 5, 7]
# print(multiply_list(numbers))


 

# Write a function count_vowels(text) that counts the number of vowels (a, e, i, o, u) in a given string.

# def count_vowels(text):
#     vol_count = 0
#     for char in text:
#         if char in "aeiouAEIOU":
#             vol_count += 1
#     return vol_count
# text = input("Enter a string: ")
# print(count_vowels(text))


# Alternative: 

# def count_vowels(text):
#     return sum(1 for char in text if char in "aeiouAEIOU")
# text = input("Enter a string: ")
# print(f"The vowels in your string are {count_vowels(text)}")



 

# Create a function reverse_string(s) that returns the reverse of a given string.

# def reverse_string(string):
#     return string[::-1]
# string = input("Enter a string: ").strip()
# print(reverse_string(string))



 


# Write a function factorial(n) to calculate the factorial of a given number.

# def factorial(num):
#     if num < 0:
#         return "Factorial is not defined for negitive number."
    
#     fact = 1
#     for i in range(2, num + 1):
#         fact *= i
#     return fact
# num = int(input("Enter a number: "))
# print(f"Factorial of {num} is {factorial(num)}")



 



# Write a function max_of_three(a, b, c) that returns the largest of three numbers.

# def max_of_three(a, b, c):
#     if a > b and a > c:
#         print(f"Largest number is {a}")
#     elif b > c:
#         print(f"Largest number is {b}")
#     else:
#         print(f"Largest number is {c}")
#     return
# max_of_three(3, 4, 2)



# Alternative:

# def max_of_three(a, b, c):
#     return max(a, b, c)
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# print(f"The largest number is {max_of_three(a, b, c)}")
 




# Create a function check_palindrome(word) that checks whether a given word is a palindrome.

# def check_palindrome(word):
#     reversed_word = word[::-1]
#     if word == reversed_word:
#         print("The given word is palindrome")
#     else:
#         print("The given word is not a palindrome.")
#     return
# word = ''.join(list(input("Enter a word: ").lower().split()))
# check_palindrome(word)



# Alternative:

# def check_palindrome(word):
#     if word == word[::-1]:
#         return True
#     return False
# word = input("Enter a word: ").replace(" ", "").lower()
# if check_palindrome(word):
#     print("The given word is palindrome.")
# else:
#     print("The given word is not a palindrome.")



 
 



# Write a function fibonacci(n) that returns the nth Fibonacci number using recursion.

# def fibonacci(n, memo = {}):
#     if n in memo:
#         return memo[n]
#     if n <= 1:
#         return n
#     memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
#     return memo[n]
# print(fibonacci(10))
# print(fibonacci(8))


 
 



# Define a function prime_numbers(limit) that returns a list of all prime numbers up to the given limit.

# def prime_number(limit):
#     if limit < 2:
#         return []
#     prime = []
#     for num in range(2, limit + 1):
#         is_prime = True
#         for divisor in range(2, int(num ** 0.5) + 1):
#             if num % divisor == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             prime.append(num)
#     return prime

# try:
#     limit = int(input("Enter a number: "))
#     if limit <= 0:
#         print("Please Enter a positive number: ")
#     else:
#         print(prime_number(limit))
# except ValueError:
#     print("Invalid syntax. Please enter an interger.")



 



# Write a function sort_words(sentence) that takes a sentence and returns the words sorted in alphabetical order.

# def sort_word(sentence):
#     words = sentence.split()
#     return sorted(words, key=str.lower)
# sentence = "The quick brown fox jumps over the lazy dog"
# print(sort_word(sentence))
 

 



# Create a function remove_duplicates(lst) that removes duplicate elements from a list.

# def remove_duplicate(lst):
#     return list(set(lst))
# lst = list(map(int, input("Enter a list of numbers: ").split()))
# print(remove_duplicate(lst))






# Write a function area_and_perimeter(length, width) that returns both the area and perimeter of a rectangle.

# def area_and_perimeter(length, width):
#     print(f"Area of rectangle is {length * width}\nPerimeter of rectangle is {2 * (length + width)}")
# length = int(input("Enter the length of rectangle: "))
# width = int(input("Enter the width of rectangle: "))
# area_and_perimeter(length, width)

# improved:

# def area_and_perimeter(length, width):
#     area = length * width
#     perimeter = 2 * (length + width)
#     return area, perimeter
# try:

#     length = float(input("Enter the length of Rectangle: "))
#     width = float(input("Enter the width of Rectangle: "))
#     area, perimeter = area_and_perimeter(length, width)
#     print(f"Area of Rectangle is : {area}")
#     print(f"Perimeter of Rectangle is: {perimeter}")
# except ValueError:
#     print("Invalid syntax. Please enter correct values.")


 
 


# Define a function find_gcd(a, b) to find the greatest common divisor (GCD) of two numbers.

# def find_gcd(a, b):
#     gcd = []
#     small_num = min(a, b)
#     for x in range(1, int(small_num // 2) + 1):
#         if a % x == 0 and b % x == 0:
#             gcd.append(x)
#     return max(gcd)
# try:
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     print(find_gcd(a, b))
# except ValueError:
#     print("Invalid syntax. Please enter integers")



# improved:

# def find_gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return abs(a)
# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     if a == 0 or b == 0:
#         print(f"The gcd for {a} and {b} is not defined.")
#     else:
#         print(f"The gcd for {a} and {b} is {find_gcd(a, b)}")
# except ValueError:
#     print(f"Invalid syntax. Please enter correct values.")





 

# Create a function is_anagram(str1, str2) that checks whether two strings are anagrams of each other.

# def is_anagram(str1, str2):
#     return sorted(str1) == sorted(str2)
# print(is_anagram("hello", "world"))
# print(is_anagram("triangle", "integral"))

 
# Alternative:

# def is_anagram(str1, str2):
#     return sorted(str1) == sorted(str2)
# try:
#     str1 = input("Enter first string: ")
#     str2 = input("Enter second string: ")
#     if is_anagram(str1, str2):
#         print(f"{str1} and {str2} are anagrams of eachother.")
#     else:
#         print(f"{str1} and {str2} are not anagrams of eachother.")
# except ValueError:
#     print("Invalid syntax. Please enter correct values.")


 


# Write a function map_lengths(words) that takes a list of words and returns a list of their lengths.

# def map_length(sentence):
#     words = sentence.split()
#     words_length = []
#     for x in words:
#         words_length.append(len(x))
#     return words_length
# sentence = input("Enter a string: ")
# print(map_length(sentence))



# Alternative:

# def map_length(sentence):
#     return [len(words) for words in sentence.split()]
# sentence = input("Enter a string: ")
# print(map_length(sentence))


 


# Define a function merge_dicts(dict1, dict2) that merges two dictionaries into one.

# def merge_dicts(dict1, dict2):
#     merged_dict = dict1.copy()
#     merged_dict.update(dict2)
#     return merged_dict
# dict1 = {
#     "name" : "Aftab",
#     "age" : 17
# }
# dict2 = {
#     "games" : "Football", 
#     "religion" : "islam"
# }
# print(merge_dicts(dict1, dict2))



# Alternative:

# def merge_dict(dict1, dict2):
#     return {**dict1, **dict2}

# dict1 = {
#     "name" : "Aftab",
#     "age" : 17
# }
# dict2 = {
#     "games" : "Football", 
#     "religion" : "islam"
# }

# print(merge_dict(dict1, dict2))








# Write a function validate_password(password) that checks if the given password is strong 
#     (contains at least 8 characters, including uppercase, lowercase, and a number).


# def validate_password(password):
#     if len(password) < 8:
#         print("password must contain 8 character")
#     elif not any(char.isdigit() for char in password):
#         print("Password must contain numaric character.")
#     elif not any(char.islower() for char in password):
#         print("Password must contain one lowercase letter.")
#     elif not any(char.isupper() for char in password):
#         print("Password must contain one uppercase letter.")
#     else:
#         print("Password is correct")
# password = input("Enter Your Password: ")
# validate_password(password)







# Alternative:

# import re
# def validate_password(password):
#     if (len(password) < 8):
#         return False
#     elif not re.search(r'[A-Z]', password):
#         return False
#     elif not re.search('[a-z]', password):
#         return False
#     elif not re.search(r'[0-9]', password):
#         return False
#     return True

# password = input("Enter Your Password: ")

# if validate_password(password):
#     print("Password is stronge")
# else:
#     print("Password is incorrect.")



 







# Write a function sum_of_digits(n) that takes an integer input and returns the sum of its digits using a loop.  

# def sum_of_digits(num):
#     return sum(int(digit) for digit in num)
# num = input("Enter a number: ")
# print(f"sum of digit is {sum_of_digits(num)}")
 







# Create a function filter_even(numbers) that takes a list of integers and return only the even numbers.

# def filter_even(numbers):
#     return filter(lambda x : x % 2 == 0, numbers)
# numbers = list(map(int, input("Enter a list of numbers: ").split()))
# print(list(filter_even(numbers)))


 






# Write a recursive function sum_range(start, end) that returns the sum of all integers between start and end, inclusive.

# def sum_range(start, end):
#     return sum(num for num in range(start, end + 1))
# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))
# print(sum_range(start, end))



# Alternative:

# def sum_range(start, end):
#     if start == end:
#         return start
#     return start + sum_range(start + 1, end)
# try:
#     start = int(input("Enter starting number: "))
#     end = int(input("Enter an ending number: "))
#     if start > end:
#         print("Starting number must be less or equal to end number.")
#     else:
#         print(f"The sum of digit between {start} to {end} is {sum_range(start, end)}")
# except ValueError:
#     print("invalid syntax. Please enter valid input.")


 






# Write a function is_palindrome(word) that checks if a given string is a palindrome  using slicing.

# def is_palindrome(word):
#     return word == word[::-1]
# word = input("Enter a string: ").replace(" ", "").lower()
# print(is_palindrome(word))








# Write a function is_palindrome(word) that checks if a given string is a palindrome  without  using slicing.

# def is_palindrome(word):
#     reversed_string = ""
#     for char in word:
#         reversed_string = char + reversed_string
#     if word == reversed_string:
#         return True
#     return False
   
# word = input("Enter a string: ").replace(" ", "").lower()

# if is_palindrome(word):
#     print("String is palindrome")
# else:
#     print("string is not palindrome")









# Create a function sort_by_length(words) that takes a list of words and uses a lambda function with sorted to sort them by length.

# def sort_by_length(words):
#     return sorted(words, key= lambda word : len(word))
# words = input("Enter a sentence").split()
# print(sort_by_length(words))

 








# Write a function factorial() that asks the user for a number and calculates its factorial using recursion.


# def factorial(num):
#     if num == 1:
#         return num
#     fact = num * factorial(num - 1)
#     return fact
# try:
#     num = int(input("Enter a number: "))
#     if num <= 0:
#         print("Please enter a positive number: ")
#     else:
#         print(f"The factoria of {num} is {factorial(num)}")
# except ValueError:
#     print("Invalid syntax. Please enter an interger value.")



 





# Write a function sum_even_numbers(n) that calculates the sum of all even numbers up to a given number n using a loop.

# def sum_even(num):
#     total = 0
#     for i in range(2, num + 1, 2):
#         total += i
#     return total
# try:
#     num = int(input("Enter a number: "))
#     if num < 0:
#         print("Please enter a positive number: ")
#     else:
#         print(f"sum of even digits till {num} is {sum_even(num)}")
# except ValueError:
#     print("Invalid syntax. Please enter valid input.")




# Alternative: 

# def sum_even(num):
#     return sum(x for x in range(1, num + 1) if x % 2 == 0)
# try:
#     num = int(input("Enter a number: "))
#     if num < 0:
#         print("Please enter a positive number: ")
#     else:
#         print(f"sum of even digits till {num} is {sum_even(num)}")
# except ValueError:
#     print("Invalid syntax. Please enter valid input.")
 


 








# Create a function char_frequency(text) that takes a string and returns a dictionary showing the frequency of each character using a loop.

# def char_frequency(word):
#     frequency = {}
#     for char in word:
#         if char in frequency:
#             frequency[char] += 1
#         else:
#             frequency[char] = 1
#     return frequency
# word = input("Enter a word: ")
# print(char_frequency(word))








# Write a function simple_calculator(a, b, operation) that uses a lambda function to perform addition, subtraction, multiplication, or division based on the operation parameter.

# def simple_calculator(a, b, operation):
#     operations = {
#         "add" : lambda x, y : x + y,
#         "subtract" : lambda x, y : x - y, 
#         "multiply" : lambda x, y : x * y,
#         "divide" : lambda x, y : x // y if y != 0 else "Division by zero is not allowed."
#     }

#     if operation in operations:
#         return operations[operation](a, b)
#     else:
#         print("Invalid operation. Please enter add, subtract, multiply, divide.")

# a = int(input("Enter first value: "))
# b = int(input("Enter second value: "))
# operation = input("Chose operation: ")

# print(simple_calculator(a, b, operation))

