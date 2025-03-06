
##################-----------------  OS MODULE  ----------------######################

#  Python has built in os module with methods to interact with operating system, like creating and removing files and directoreries.




##################--------------  Get Current Directory  ----------------######################

# Return path of current working directory.


# import os

# print(os.getcwd())
 


 




##################--------------  Make Directory  ----------------######################

#  The function creates a new directory at specified location.


# import os

# os.mkdir("hello")



# Alternative:


# os.mkdir("C:\\Users\\ML\\OneDrive\\Desktop\\hello")









##################--------------  Creating Multiple Nested Directories  (Parent + Child)  ----------------######################


# import os

# os.makedirs("grandparent/parent/child")




# Alternative:


# os.makedirs("C:\\Users\\ML\\OneDrive\\Desktop\\grandparent\\parent\\child")








##################--------------  Remove Empty Directory  ----------------######################


# import os

# os.rmdir("hello")




# Alternative:


# os.rmdir("C:\\Users\\ML\\OneDrive\\Desktop\\hello")










##################--------------  Remove Directory with content ----------------######################

#  To remove directory with content we have to import a module named "shutil" 


# import shutil

# shutil.rmtree("grandparent")



# Alternative:

# shutil.rmtree("C:\\Users\\ML\\OneDrive\\Desktop\\grandparent")







##################-------------- Creating File ----------------######################

# We can create file with the help of python open() function.


# with open("hello.txt", "x") as f:
#     print("File is created.")




# Aternative:

# with open("C:\\Users\\ML\\OneDrive\\Desktop\\hello.txt", "x") as file:
#     print("File is created.")










##################--------------  Remove File  ----------------######################


# import os 

# os.remove("hello.txt")




# Alternative:


# os.remove("C:\\Users\\ML\\OneDrive\\Desktop\\hello.txt")











##################--------------  Change Current Directory  ----------------######################



# import os

# print(os.getcwd())


# os.chdir("C:\\Users\\ML\\OneDrive\\Desktop\\Hello")


# print(os.getcwd())


 








##################--------------  List Files and Directory  ----------------######################

#  This method list all the files and folder in the given directory. if the path is not given it will list the files and folder in the current working directory.



# import os

# print(os.listdir())




# Alternative:

# x = os.listdir()

# for folder in x:
#     print(folder)






# Alternative:

# print(os.listdir("C:\\Users\\ML\\OneDrive\\Desktop\\Deployment"))














##################--------------  Rename File or Directory  ----------------######################


# import os



# with open("hello.txt", "x") as file1: 
#     print("File is created.")



# os.rename("hello.txt", "random.txt")    







# Alternative:


# os.mkdir("hello")

# os.rename("hello", "well")



 






#################--------------  Check File Existance   -----------------#######################


# This method checks the file exist or not on the specified location.

# import os

# print(os.path.exists("hello.txt"))


# Alternative:

# if os.path.exists("hello.txt"):
#     print("File exists.")
# else:
#     print("File doesn't exist")






# Alternatvie:


# if os.path.exists("C:\\Users\\ML\\OneDrive\\Desktop\\hello.txt"):
#     print("File exists")
# else:
#     print("File doesn't exist.")
 















#################--------------  os.path.join()   -----------------#######################


# This function join base directory with subdirectory.    ------->     base_dir\\sub_dir



# import os

# base_dir = "workspace"
# sub_dir = "images"


# sub_dir_path = os.path.join(base_dir, sub_dir)

# if not os.path.exists(sub_dir_path):
#     os.makedirs(sub_dir_path)
# else:
#     print("Path already exists")


















#################--------------  os.path.isfile(f)   -----------------#######################

# This function checks that the given object is a file or folder.



# import os

# with open("hello.txt", "x") as f:
#     print("file is successfully created")

#     if os.path.isfile("hello.txt"):
#         print(f"'hello.txt' is a file")
#     else:
#         print(f"'hello.txt' is a folder")













#################--------------  os.path.isdir(d)   -----------------#######################


# import os

# os.mkdir("hello")


# if os.path.isdir("hello"):
#     print("Yes 'hello' is a directory")
# else:
#     print("No 'hello' is not a directory")











#################--------------  os.path.splitext()   -----------------#######################


# This function split the file name into two in a tuple. First_name(file name without dot(.))
# second_name(it is the file extension with dot(.))



# import os

# file_name = "photo.jpg"

# file_ext = os.path.splitext(file_name)[1].lower()

# print(file_ext)














#################--------------  os.path.basename()   -----------------#######################

# This function extract the basename out of give path.





# import os

# path = "home/Users/ML/OneDrive/Desktop/hello"

# print(os.path.basename(path))


















#################--------------  Summary  -----------------#######################


# os.getcwd()
# os.mkdir()
# os.makedires()
# os.rmdir()
# os.remove()
# os.chdir()
# os.listdir()
# os.rename()
# os.path.exist()
# os.path.isfile()
# os.path.isdir()
# os.path.splitext()
# os.path.join()
# os.path.basename() 