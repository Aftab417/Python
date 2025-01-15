
 # There are following methods for dictionary.

student = {
    "name" : "Aftab",
    "age" : 18,
    "marks" : 1075,
    "subjects" : {
        "chem" : 95,
        "Eng" : 96,
        "Biology" : 85,
        "Physics" : 90,
    }
}
#################--------------- get() method --------------------#####################
# This method is use to acess any item in the dictionary.
# print(student.get)
# print(student.get("age"))

#################--------------- key() method --------------------#####################

# This method is use to access all the keys in dictionary.
# print(student.keys())
# print(student["subjects"].keys())


#################--------------- value() method --------------------#####################

# This method is use to access all the values in dictionary.

# print(student.values())
# print(student["subjects"].values())


#################--------------- items() method --------------------#####################

# This method is use to access all the items in dictionary.

# print(student.items())
# print(student["subjects"].items())



#################--------------- update() method --------------------#####################

# This method is use to add items in dictionary or to change the value of a specific key.

# student.update({"religion": "islam", "class": 12})
# print(student)
 
# student.update({"name": "Ali"})
# print(student)


#################--------------- pop() method --------------------#####################

# This method is use to delete the specified item from the dict.

# student.pop("name")
# print(student)


#################--------------- popitem() method --------------------#####################

# This method is use to delete the last inserted item in the list.

# student.popitem()
# print(student)



#################--------------- delete keyword --------------------#####################

# This is use to delete the item or whole list.
# del student["age"]
# print(student)