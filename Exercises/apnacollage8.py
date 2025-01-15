
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