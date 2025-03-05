
################-------------  Shutil (Shell Utilities) Module  ------------------################

#  Shutil module in python provide functions to perform high-level file operations. Such as copying, moving, renaming
#  and deleting files and directories. 






################-------------  Coping files and directories  ------------------################
   


# import shutil

# copying only file without metadata:

# shutil.copy("learning python.txt", "C:\\Users\\Ml\\OneDrive\\Desktop")



# copying files along with its metadata (permissions, timestamps)

# shutil.copy2("learning python.txt", "C:\\Users\\ML\\OneDrive\\Desktop")



# coping folder with sub_directories and files

# shutil.copytree("workspace", "C:\\Users\\ML\\OneDrive\\Desktop\\workspace")















################-------------  Moving files and directories  ------------------################


# import shutil


# shutil.move("learning python.txt", "C:\\Users\\ML\\OneDrive\\Desktop\\learning python.txt")

# shutil.move("C:\\Users\\ML\\OneDrive\\Desktop\\learning python.txt", ".")















################------------- Deleting files and directories  ------------------################


# import shutil

# shutil.rmtree("workspace")







