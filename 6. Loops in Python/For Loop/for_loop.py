
# For Loop : It is use to iterate over a squence that is either a list, tuple, dict, set or a string.

# list = [1, 3, 5, 6, 7,]
# for x in list:
#     print(x)



# tuple = ("banana", "mango", "orange", "apple")
# for fruites in tuple:
#     print(fruites)


# str = "Aftab Ahmad"
# for char in str:
#     print(char, end=" ") 



###################---------------- Break statement ---------------##########################

# nums = [1,2,3,4,5,6]
# for x in nums:
#     print(x, end=" ") 
#     if x == 5:
#         break



# letters = ["a", "b", "c", "d", "e"]
# for char in letters:
#     print(char, end=" ")
#     if char == "c":
#         break
 





###################---------------- Continue statement ---------------##########################

# nums = [1,2,3,4,5,6]
# for x in nums:
#     if x == 5:
#         continue
#     print(x)
 



# letters = ["a", "b", "c", "d", "e"]
# for x in letters:
#     if x == "c":
#         continue
#     print(x)
 








###################---------------- range() function ---------------##########################

# range function : it is use to print squence that start with 0 (by default), increase by 1, and ends at a specified value.

# for x in range(2, 10):
#     print(x)


# for x in range(2, 6):   # (start, stop)
#     print(x)




# for x in range(2, 100, 3):
#     print(x)




###################---------------- pass statement ---------------##########################

# Pass statement : it is null statement that does nothing. it act as a placeholder for future code.

# for x in range(2, 100):
#     pass

# print("This statement does nothing.")






###################---------------- Nested Loop ---------------##########################

# adj = ["red", "testy", "free"]
# fruits = ["apple", "orange", "mango"]

# for x in adj:
#     for y in fruits:
#         print(x, y)