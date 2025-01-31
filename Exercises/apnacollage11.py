
# Write a programe to creat a file and write  the following content in it and in exact given format.
# Hi, everyone
# I am learning File I/O 
# using Python.
# I like programmming in Python.


# with open("practice.txt", "w") as f:
#     f.write("Hi, everyone\nI am learning File I/O ")
#     f.write("using Python\nI like programming in Python.")
 






# Write a programe to replace the word "Python" with "Java" in above file.

# with open("practice.txt", "r") as f:
#     data = f.read()
# new_data = data.replace("Python", "Java")
# print(new_data)

# with open("Practice.txt", "w") as f:
#     f.write(new_data)






# Write a programme that searches is the word "learning" exist in the file.

# with open("practice.txt", "r") as f:
#     data = f.read()
#     if data.find("learing"):
#         print("Yes, the word 'learning' exist in the file.")
#     else:
#         print("No, the word 'learning' does not exist in the file.")



# Alternative:

# def check_for_word():
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if data.find("learning"):
#             print("Found")
#         else:
#             print("Not Found")
# check_for_word()







# Write a Function in which line does the word "learning" occure first and return -1 if the word does not exist.

  
# def check_for_line(word):
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if word in data:
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1
# print(check_for_line("learning"))








# From a file containing numbers seprated by comma, print the count of even numbers.

# with open("numbers.txt", "x") as f:
#     f.write("1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14")


# def count_even():
#     with open("numbers.txt", "r") as f:
#         data = f.read()
#         new_data = list(map(int, (digit for digit in data.split(","))))
#         print(new_data)
#         return sum(1 for num in new_data if num % 2 == 0)
# print(count_even())
    