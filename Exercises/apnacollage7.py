
# Write a programme to print counting from 1 to 100.

# i = 1
# while i <= 100:
#     print(i)
#     i += 1






# Write a programme to print counting from 100 to 1.

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1







# Write a programme to print a multiplication table of number n.

# n = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(n * i)
#     i += 1







# Write a programme to print elements of list using loop.

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1






# Write a programme to search a spicific number x in the tuple.

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("Found at index", i)
        break
    else:
        print("Finding")
    i += 1






# Write a programme to print only odd numbers from 1 to 100.

# i = 0 
# while i < 100:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)






# write a programme to print only even numbers from 1 to 100.

# i = 0 
# while i < 100:
#     i += 1
#     if (i % 2 != 0):
#         continue
#     print(i)