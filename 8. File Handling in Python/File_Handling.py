 
######################-----------  Reading a File --------------####################

# Open file :  In python there is built_in function to open a file.

# f = open("sample.txt", "r")     
# print(f.read())  
# f.close()


# Best syntax:

# with open("sample.txt", "r") as f:
#     print(f.read())


# with open("sample.txt", "r") as f:
#     for x in f:
#         print(x)

# with open("demo.txt", "r") as f:
    # print(f.read(5))



# with open("demo.txt", "r") as f:
#     print(f.readline())
#     print(f.readline())


######################-----------  Writing in File --------------####################

# append mode: By this mode The already written text in the file will not remove. If the specified file does not exist already the append mode will creat a new file.

# with open("sample.txt", "a") as f:
#     f.write("I want to Play football\nI want to become an AI Engineer.")


# with open("hello.txt", "a") as f:
#     f.write("Hello world!")




# Write mode : By this mode The already written content in the file will be removed, means this mode overwrite the content.

# with open("demo.txt", "w") as f:
#     f.write("Hi, I am Ali.\nI want to become a Doctor.")





######################-----------  Creating a new File --------------####################

# "x" mode : This mode creat a new file. If the file already exist it will throw an error.

# with open("hello.txt", "x") as f:
#     f.write("Hi, i am Aftab Ahmad\nI want to become AI Engineer.")






######################----------- Deleting a File --------------####################

# Deleting File : To delete a file we have to import an OS Module.

# import os


# This will remove a file:

# os.remove("demo.txt")




# This will check if a file exit:

# f = os.path.exists("hello.txt")
# print(f)



# if os.path.exists("hello.txt"):
#     os.remove("hello.txt")
# else:
#     print("The file does not exist.")






# This will remove the whole folder:

# os.rmdir("hello")

# if os.path.exists("hello"):
#     os.rmdir("hello")
# else:
#     print("Folder does not exist.")










#############---------------   reading and writting  "r+" ------------###############

# This mode will open the file in both read and write mode.

# with open("json_data", "r+") as file:
#     file.write("hello world")









#############---------------   reading and writting  "w+" ------------###############

# This mode will open the file in both read and write mode.

 
# with open("json_data", "w+") as file:
#     print(file.read())
  









#############---------------   reading and appending  "a+" ------------###############

# This method will open file in both read and appened mode.
 

# with open("json_dat", "a+") as file:
#     file.write("world") 
#     print(file.read())









#############---------------   seek() method  ------------###############

# This method is used to move the cursor in the begining of content in the file.

# with open("json_data", "r") as file:
#     file.seek(0)
#     print(file.read())