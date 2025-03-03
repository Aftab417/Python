
##################--------------  Module  -----------------########################

# Consider a module to be the same as code library.  It is basically a file containing the set of functions you want to include in your file.


##################-------------- Creating a Module  -----------------########################

# To create a module just save the code you want in a file with file extension  .py




##################-------------- Use a Module  -----------------########################

# We can use the module that we just have created or also built in module by "import" keyword.

# import mymodule

# mymodule.greetings("Aftab")





##################-------------- Variable in a Module  -----------------########################


#  Variable of any data type can be stored in a module.


# import mymodule

# print(mymodule.person1["name"])
  






##################-------------- Importing module as alias  -----------------########################

# We can create an alias when importing a module using  "as"  keyword.


# import mymodule as mx

# print(mx.person1["age"])








##################-------------- Built-in Module  -----------------########################

# There are several built-in module in python. we can use them when needed.


# import platform

# print(platform.system())


# print(platform.__name__)


# print(platform.__spec__)








##################-------------- Using dir() function for a Module  -----------------########################

#  Using dir() function we can list all the function names and variable in a module.



# import platform

# x = dir(platform)

# print(x)





# import mymodule

# print(dir(mymodule)) 












##################-------------- Import from Module  -----------------########################

# We can also import some specific parts of module using  "from"  keyword.




# from mymodule import person1

# print(person1["age"])














##################-------------- if __name__ == "__main__"     in a Module  -----------------########################


#  if module file containe such a function that are also excuting in the file they must be execute using  if __name__ == "__main__" statement 
# otherwise  the code of that file will execute in other file by only importing that file.





# import mymodule

# mymodule.hello()