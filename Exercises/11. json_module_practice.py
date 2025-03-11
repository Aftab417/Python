

# 1️⃣ Read & Write JSON File with Nested Data


# Problem:
# You have the following Python dictionary:


# data = {
#     "user": {
#         "name": "Aftab",
#         "age": 21,
#         "skills": ["Python", "Docker", "JavaScript"]
#     },
#     "location": {
#         "city": "Lahore",
#         "country": "Pakistan"
#     }
# }





# Task:

# Write this dictionary into a JSON file named user_data.json.
# Read the JSON file and print only the user’s skills.




# Solution:


# Write this dictionary into a JSON file named user_data.json.

# import json

# with open("user_data.json", "w+") as file:
#     json.dump(data, file)
#     file.seek(0)
#     print(file.read())
 







# Read the JSON file and print only the user’s skills.

# import json

# with open("user_data.json", "r") as file:
#     data = json.load(file)
#     print(data["user"]["skills"])
 
















# # 2️⃣ Convert JSON String to Python & Modify It


# # Problem:
# # You receive the following JSON string from an API:

 
# json_string = '{"product": "Laptop", "price": 1200, "in_stock": true}'


# # Task:

# # Convert this JSON string into a Python dictionary.
# # Increase the price by 10%.
# # Convert it back to a JSON string and print the new JSON data.





# # Solution:


# # Convert this JSON string into a Python dictionary.

# import json

# python_dic = json.loads(json_string)

 



# # Increase the price by 10%.

# python_dic["price"] = 1200 * 10

# print(python_dic)





# # Convert it back to a JSON string and print the new JSON data.

# updated_json_string = json.dumps(python_dic)

# print(updated_json_string)


















# # 3️⃣ Merge Two JSON Files and Save the Result


# # Problem:
# # You have two JSON files:


# # file1.json
 
# # {
# #     "name": "Aftab",
# #     "age": 21,
# #     "city": "Lahore"
# # }




# # file2.json
 

# # {
# #     "skills": ["Python", "JavaScript", "Docker"],
# #     "experience": "2 years"
# # }




# # Task:

# # Read both files and merge their content into one dictionary.
# # Save the merged dictionary into a new JSON file called merged_data.json.




# # Solution:


# # First of all creat both files and store their relevent data


# # # Creating file1.json

# # data1 = {
# #     "name": "Aftab",
# #     "age": 21,
# #     "city": "Lahore"
# # }


# # import json

# # with open("file1.json", "w") as file1:
# #     json.dump(data1, file1)








# # # creating file2.json

# # data2 = {
# #     "skills": ["Python", "JavaScript", "Docker"],
# #     "experience": "2 years"
# # }


# # import json

# # with open("file2.json", "w") as file2:
# #     json.dump(data2, file2)








# # Read both files and merge their content into one dictionary.

# import json

# with open("file1.json", "r") as file1, open("file2.json", "r") as file2:
#     data1 = json.load(file1)
#     data2 = json.load(file2)


#     merged_dic = {**data1, **data2}

#     print(merged_dic)
 




# # Save the merged dictionary into a new JSON file called merged_data.json.


# with open("merged_data.json", "w+") as file3:
#     json.dump(merged_dic, file3)
#     file3.seek(0)
#     print(file3.read())