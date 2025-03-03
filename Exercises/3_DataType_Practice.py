 
# Write a Python program to check whether a given variable is a list, tuple, set, or dictionary and print its type.

# a = [1, 3, 5, 6, 7, 2]
# print(isinstance(a,(tuple, list, int, float, set, dict, str, )))

 



# Write a Program to input user first name and print it's length.

# firstName = input("Enter Your First Name: ")
# print("Lenght of your name is",len(firstName))






# Write a program to  to find the occurance of $ symbol in string.

# dollar = "The price of this cycle is $100."
# print(dollar.find("$"))





# Write a programe to find how many time $ symbol repeates in string.

# dollar = "The price of football is $20. One $ is equal to 270pkr."
# print(dollar.count("$"))









# Question:
# Given the following nested data structure:

# data = {
#     "name": "John",
#     "age": 25,
#     "skills": ["Python", "Django", "Machine Learning"],
#     "projects": [
#         {"title": "E-commerce", "completed": True},
#         {"title": "AI Chatbot", "completed": False}
#     ]
# }



# Access the value "Django" from the skills list.
# print(data["skills"][1])


# Add a new skill, "React", to the skills list.
# data["skills"].append("React")
# print(data)



# Update the status of the "AI Chatbot" project to True.
# data["projects"][1]["completed"] = True
# print(data)

# Add a new project, "Portfolio Website", with a completion status of False.
# data["projects"].append({"title": "portfolio website", "completed": "False"})
# print(data)






# Question:
# Write a Python function that takes a variable as input and checks whether it is a list, tuple, set, or dictionary. Print the type along with an appropriate message.

# def check_type(variable):
#     if isinstance(variable, list):
#         print("vaiable is a List")
#     elif isinstance(variable, tuple):
#         print("variable is tuple")
#     elif isinstance(variable, dict):
#         print("variable is dict")
#     elif isinstance(variable, str):
#         print("variable is a string")
#     elif isinstance(variable, int):
#         print("variable is an integer")
#     elif isinstance(variable, set):
#         print("variable is a set")
#     elif isinstance(variable, complex):
#         print("variable is a complex number")
#     else:
#         print(f"variable is {type(variable)}")

# check_type({"name": "aftab", "age" : 17})
# check_type(["name", "aftab", "age", 17])
# check_type(("name", "aftab", "age", 17))
# check_type({"name", "aftab", "age", 17})
# check_type( "hello world")
# check_type( 5)
# check_type( 5.3)








# items = [10, "apple", 3.14, "banana", 5, "42"]

# # Separate the integers, floats, and strings into different lists. Sort each list individually and print the results.


# integer = [item for item in items if isinstance(item, int)]
# floats = [item for item in items if isinstance(item, float)]
# string = [item for item in items if isinstance(item, str)]

   
# integer.sort()
# floats.sort()
# string.sort()
# print(integer)
# print(floats)
# print(string)







 
# Question:
 
# students = {
#     "Alice": {"age": 20, "grade": 85},
#     "Bob": {"age": 22, "grade": 90},
#     "Charlie": {"age": 21, "grade": 78}
# }


# Tasks:
# Calculate the average age of all students.
# total_age = sum(student["age"] for student in students.values())
# avr_age = total_age / len(students)
# print(avr_age)


# Find the student with the highest grade.
# alice_grade = students["Alice"]["grade"]
# bob_grade = students["Bob"]["grade"]
# charlie_grade = students["Charlie"]["grade"]

# if (alice_grade > bob_grade and alice_grade > charlie_grade):
#     print("alice has highest grade")
# elif(bob_grade > alice_grade and bob_grade > charlie_grade):
#     print("bob has highest grade")
# else:
#     print("charlie has highest grade")


# Add a new student, "David", with age 23 and grade 88.
# students.update({"David": {"age": 23, "grade": 88}})
# print(students)





# Question:
# Write a Python function that swaps the values of two variables using tuple unpacking.
# a = 5
# b = 10

# a, b = b, a

# print("a", a)
# print("b", b)





# # Question:
# sentence = "Practice makes a person perfect"

# # Tasks:
# # Create a list of words from the string.
# words = sentence.split(" ")
# print(words)

# # Generate a list of word lengths.
# words_length = [len(word) for word in words]
# print(words_length)

# # Create a dictionary where keys are words and values are their lengths.
# word_dict = dict(zip(words, words_length))
# print(word_dict)




# Question:
 
# set1 = {2, 4, 6, 8, 10}
# set2 = {3, 6, 9, 12, 15}
# # Tasks:
# # Find elements that are in either set but not both.
# # symmatric_difference = set1 ^ set2
# # print(symmatric_difference)



# # Remove all elements divisible by 3 from set2.
# set2 = {x for x in set2 if x % 3 != 0}
# print(set2)



# # Check whether set1 is a subset of set2.
# # print(set1.issubset(set2))








#  Question:
 
# data = [
#     {"name": "Alice", "scores": [85, 92, 88]},
#     {"name": "Bob", "scores": [78, 81, 86]},
#     {"name": "Charlie", "scores": [89, 91, 84]}
# ]
# # Tasks:
# # Calculate and print the average score for each student.
# alice_aver_score = sum(score for score in data[0]["scores"]) / len(data[0]["scores"])
# bob_aver_score = sum(score for score in data[1]["scores"]) / len(data[1]["scores"])
# charlie_aver_score = sum(score for score in data[2]["scores"]) / len(data[2]["scores"])

# print(alice_aver_score)
# print(bob_aver_score)
# print(charlie_aver_score)


# # Identify the student with the highest average score.
# if (alice_aver_score > bob_aver_score and alice_aver_score > charlie_aver_score):
#     print("Alice has average scores.")
# elif (bob_aver_score > alice_aver_score and bob_aver_score > charlie_aver_score):
#     print("bob has highest average scores.")
# else:
#     print("charlie has highest average scores.")