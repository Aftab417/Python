
# Write a function to print the the lneght of list:

# def lenght_list(list):
#     return len(list)

# num = [2, 4, 3, 5, 34,]
# name = ["ali", "ahmad", "haider", "Kashif"]
# cities = ["lahore", "Karachi", "Multan", "Islamabad"]

# print(lenght_list(num))
# print(lenght_list(name))
# print(lenght_list(cities))









# Write a function to print the element of list in a single line.

# def list_ele(list):
#     for ele in list:
#         print(ele, end=" ")
# cities = ["Lahore", "Karachi", "Islamabad", "Multan"]

# list_ele(cities)
    









# Write a function to print the factorail of n :

# def fact(num):
#     fact = 1
#     for x in range(1, num + 1):
#         fact *= x
#     return fact

# print(fact(5))
# print(fact(10))
# print(fact(30))







# Write a function that convert USD doller into pkr.

# def convert_currency(doller):
#     return doller * 270

# print(convert_currency(30))








# Write a function that check the given number is even or odd.

# def check_num(num):
#     if num % 2 == 0:
#         print(f"{num} is Even")
#     else:
#         print(f"{num} is Odd")
#     return

# check_num(int(input('Enter a number: ')))









# Write a recursive function to calculate the sum of  first n natural number.
 
# def sum_of_num(n):
#     if n == 1:
#         return 1
#     return  n + sum_of_num(n - 1)
# number = int(input("Enter a number: "))
# if number > 0:
#     print(f"The sum of number till {number} is : {sum_of_num(number)}")
# else:
#     print("Please Enter a positive number.")







# Write a function to print the element of list recursively.


# def print_element(lst, index = 0):
#     if index == len(lst):
#         return
#     print(lst[index])
#     print_element(lst, index + 1)

# cities = ["Lahore", "Karachi", "Multan", "Islamabad", "Rawalpindi",]
# print_element(cities)