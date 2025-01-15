
####################---------------- print() -----------------------#######################

# print output to console:

# name = "Aftab Ahmad"
# print(name)

# print("Taha Sultan")





####################---------------- input() -----------------------#######################

# Accept the user input in the form of strin:

# user_input = input("Your name: ")
# print(user_input)




####################---------------- len() -----------------------#######################

# Return the length(number of items in an object.)

# numbers = [1, 3, 5, 3, 6, 2]
# print(len(numbers))





####################---------------- type() -----------------------#######################

# Check the type of an object:
# name = "Aftab Ahmad"
# print(type(name))






####################---------------- int() -----------------------#######################

# Convert the value into an interger:
# num = 53.2
# print(int(num))






####################---------------- float() -----------------------#######################

# Convert the value into a float:
# num = 45
# print(float(num))




####################---------------- str() -----------------------#######################

# Convert the value into a string:
# num = 5
# print(type(str(num)))










####################---------------- sum() -----------------------#######################

# Calculate the sum of iterator in an iterable:

# lst = [1, 2, 3, 4, 5]
# total = sum(x for x in lst)
# print(total)



####################---------------- min() -----------------------#######################

# Find out the smallest number in given numbers:

# num = [33, 234, 2, 43, 5, 343]
# smallest = min(x for x in num)
# print(smallest)






####################---------------- max() -----------------------#######################

# Find out the largest number in given numbers:

# num = [33, 234, 2, 43, 5, 343]
# largest = max(x for x in num)
# print(largest)





####################---------------- zip() -----------------------#######################

# combine two or more iterable into a single iterable of tuple:

# num = [1, 3, 2, 5, 4]
# char = ["c", "d", "e", "b", "a"]
# combined = list(zip(num, char))
# print(combined)


# num = [1,2,3,4,5]
# char = ["a", "b", "c", "d", "e"]
# combined = dict(zip(num, char))
# print(combined)






####################---------------- sorted() -----------------------#######################

# Return a sorted list from an iterable:

# num = [1, 3, 2, 5, 4]
# char = ["c", "d", "e", "b", "a"]
# combined = list(zip(num, char))
# sorted_list = sorted(combined, key=lambda x : x[0])
# print(sorted_list)



# char = ["c", "d", "e", "b", "a"]
# combined = list(zip(num, char))
# sorted_list = sorted(combined, key=lambda x : x[1])
# print(sorted_list)



# fruites = ["mango", "banana", "apple", "Kiwi"]
# sorted_list  = sorted(fruites, key=str.lower)

# print(sorted_list)






####################---------------- map() -----------------------#######################

# Applies the function to each item in an iterable:

# numbers = [1, 2, 3, 4, 5]
# squared = map(lambda x : x ** 2, numbers)
# print(list(squared))



# num = [2, 4, 6, 8, 10, 12]
# final = map(lambda x : x // 2, num)
# print(list(final))





####################---------------- filter() -----------------------#######################

# Filter the elements from iterable according to given condition:

# lst = [1, 2, 3, 4, 5, 6, 7,8]
# even = filter(lambda x : x % 2 == 0, lst)
# print(list(even))



# nums = [1, 2, 3, 4, 5, 6]
# odd = filter(lambda x : x % 2 != 0, nums)
# print(list(odd))






####################---------------- enumerate() -----------------------#######################

# Adds an index with each iterator of an iterale:

# fruites = ["banana", "apple", "Orange", "mango"]
# for index, fruite in enumerate(fruites):
#     print(index, fruite)



# students = ["Taha", "Zakria", "Haider", "Aftab"]
# for index, name in enumerate(students):
#     print(index, name)





####################---------------- round() -----------------------#######################

# Round the numbers to nearest interger or specified decimal place:

# print(round(344.3434534))

# print(round(344.3434534, 3))


# num = 4353.865675
# print(round(num, 2))







####################---------------- any() -----------------------#######################

# Return true if any element in iterable evaluate true. If iterable is empty it return false:

# nums = [1, 2, 0, 3, 4]
# print(any(nums))

# nums = []
# print(any(nums))


# password = "hello124"
# if not any(char.isdigit() for char in password):
#     print("Passwor must contain at least one numaric character.")
# elif not any(char.islower() for char in password):
#     print("Password must contain at least one small letter.")
# else:
#     print("Password is correct.")






####################---------------- all() -----------------------#######################

# Return True if all the element in an iterable evaluate True. If the iterable is empty it return True:

# num = [0, 1, 0, 1]
# print(all(num))


# num = []
# print(all(num))


# password = "hello world"
# if not(all(char.isupper() for char in password)):
#     print("Password in incorrect")
# else:
#     print("password is correct.")







####################---------------- isinstance() -----------------------#######################

# Checks if an object is an instance of class or subclass:

# num = [1, 2, 3, 4]
# print(isinstance(num, list))


# print(isinstance(10, int))

# print(isinstance(34.344, float))






####################---------------- next() -----------------------#######################

# Return the next item from an iterator:

# num = iter([10, 20, 30, 40])
# print(next(num))

 


