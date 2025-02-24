
# We can remove items from a dictionary by following method.

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

# student.pop("name")
# print(student)

# student.popitem()          # this will remove last inserted item.
# print(student)





# This also can be done by del keyword

# del student["name"]
# print(student)

# del student     # This will delete the whole dictionary.





# we can remove all the items of dictionary by clear() method.

# student.clear()
# print(student)         # This wil return empty {} because all the items in dictionary are cleared.