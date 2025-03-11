

#####################-------------------  Json Module  ------------------------#########################

#  JSON (Java Script Object Notation)  is syntax for storing and exchanging the data.
#  Python has built in Json module which can be used to work with json data.



  
##############---------------- Parse Json - Convert Json to python   -----------------###################



#  json.loads() :  This mathod is used to convert  'json string'  into a python object.
 

# import json

   
# data = '{"Name" : "Aftab", "City" : "Islamabad", "age" : 20}'

 
# python_obj = json.loads(data) 

 
# print(python_obj)

# print(python_obj["Name"])












# json.load() :  This method is used to convert  'json file'   into a python object


# import json

# json_string = '{"Name": "Aftab", "City": "Islamabad" }'

# with open("json_data", "r+") as file:
#     file.write(json_string)
#     file.seek(0)

#     print(json.load(file))
 















###############--------------  Coverting Python Object to JSON data   -----------------####################



#  json.dumps() :  This mathod is use to convert the python object to "JSON_string"




# import json


# data = {
#     "Name" : 'Aftab',
#     "Age" : 20,
#     "City" : "Islamabad"
# }


# json_string = json.dumps(data)

# print(json_string)

# print(json_string[0])










#  json.dump() :  This mathod is use to convert the python object to "JSON_file"




# import json


# data = {
#     "Name" : 'Aftab',
#     "Age" : 20,
#     "City" : "Islamabad"
# }


# with open("json_file", "w+") as file:
#     json.dump(data, file)
#     file.seek(0)
#     print(file.read())

 

 







#######   We can convert following data types of python into json.


# Python        ------------->               JSON

# dict          ------------->              Object

# list          ------------->              Array

# tuple         ------------->              Array

# str           ------------->              String

# int           ------------->              Number

# float         ------------->              Number

# True          ------------->              true

# False         ------------->              false

# None          ------------->              null
 




# Examples:



# import json


# print(json.dumps("Hello, world"))

# print(json.dumps({"Name": "Aftab", "City": "Islamabad"}))

# print(json.dumps(["mango", "orange", "banana", "Apple"]))

# print(json.dumps(("Ali", "Ahmad", "Taha", "Kashif" )))

# print(json.dumps(20))

# print(json.dumps(54.4))

# print(json.dumps(True))

# print(json.dumps(False))










# import json

# x = {
#     "Name": "john",
#     "Age": 30,
#     "Married": True,
#     "divorced": False,
#     "children": ("Anna", "bella"),
#     "pets": None,
#     "cars":[
#         {"model": "BMW 230", "mpg": 27.5},
#         {"model": "Ford", "mpg": 24.1}
#     ]
# }



# print(json.dumps(x))










#############################--------  json.dumps()  Parameters  --------------##########################

#  Json.dumps() method has parameter to make it easier to read the result


  
#############################--------  json.dumps()  'indent' parameter  --------------##########################


#  We use the indent parameter to define the numbers of indents 


# import json

# x = {
#     "Name": "john",
#     "Age": 30,
#     "Married": True,
#     "divorced": False,
#     "children": ("Anna", "bella"),
#     "pets": None,
#     "cars":[
#         {"model": "BMW 230", "mpg": 27.5},
#         {"model": "Ford", "mpg": 24.1}
#     ]
# }


# print(json.dumps(x, indent=1))

 









#############################--------  json.dumps()  'sort_key' parameter  --------------##########################

# We can use the sort_key  parameter to specify if the result should be sorted or not


# import json

# x = {
#     "Name": "john",
#     "Age": 30,
#     "Married": True,
#     "divorced": False,
#     "children": ("Anna", "bella"),
#     "pets": None,
#     "cars":[
#         {"model": "BMW 230", "mpg": 27.5},
#         {"model": "Ford", "mpg": 24.1}
#     ]
# }


# print(json.dumps(x, sort_keys=True))