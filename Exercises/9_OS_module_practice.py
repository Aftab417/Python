
###################---------------- Practice OS MODULE -----------------########################


# Write a Python program that:
# Creates a file named "test1.txt" in the current directory.
# Renames it to "renamed_test.txt" if it exists.
# Prints a message confirming the renaming.


# import os

# with open("test1.txt", "x") as file:
#     print("File has been created.")


# if os.path.exists("test1.txt"):
#     os.rename("test1.txt", "renamed_test.txt")
#     print("The File is successfully renamed. ")







# Alternative:



# import os

# try:
#     with open("test1.txt", "x") as file:
#         print("File is successfully created.")

# except FileExistsError:
#     print("File already exists.")



# if os.path.exists("test1.txt"):
#     os.rename("test1.txt", "renamed_test1.txt")
#     print("File is successfully renamed.")

# else:
#     print("File doesn't Found.")


















# Write a program that:
# Checks if "old_file.txt" exists in the current directory.
# If it exists, rename it to "new_file.txt".
# If it does not exist, print "File not found."
 


# import os

# if os.path.exists("old_file.txt"):
#     os.rename("old_file.txt", "new_file.txt")
#     print("File is successfully renamed")

# else:
#     print("File doesn't exist.")

















# Write a script that:
# Checks if "notes.txt" exists on your Desktop.
# If it exists, rename it to "backup_notes.txt".
# If not, print "File does not exist on Desktop."

 

# import os

# if os.path.exists("C:\\Users\\ML\\OneDrive\\Desktop\\notes.txt"):
#     os.rename("C:\\Users\\ML\\OneDrive\\Desktop\\notes.txt", "C:\\Users\\ML\\OneDrive\\Desktop\\backup_notes.txt")
#     print("File is successfully renamed.")

# else:
#     print("File doesn't exist.")







# Alternative:


# import os

# old_file = "C:\\Users\\ML\\OneDrive\\Desktop\\notes.txt" 

# new_file = "C:\\Users\\ML\\OneDrive\\Desktop\\backup_notes.txt"



# if os.path.exists(old_file):
#     os.rename(old_file, new_file)
#     print("File is successfully renamed.")

# else:
#     print("File doesn't exist.")



 















# Write a Python script that:

# Checks if a directory named workspace exists. If not, creates it using os.makedirs().
# Inside workspace, create three subdirectories: images, documents, and others.
# Move files from the current directory into these subdirectories based on their extensions:
# .jpg, .png, .gif → move to images/
# .txt, .pdf, .docx → move to documents/
# Other file types → move to others/
# List the contents of workspace after organizing the files.


 


# Solution:



# import os
# import shutil


# def organize_files():

#     base_dir = "workspace"
#     subdirs = {
#         "images" : [".jpg", ".png", ".gif", ".jpeg"],
#         "documents" : [".txt", ".pdf", ".docx"],
#         "videos" : [".mp4"],
#         "audioes" : [".mp3"],
#         "coding_files" : [".py", ".html", ".js", ".php", ".css"],
#         "others" : []
#     }



#     if not os.path.exists(base_dir):
#         os.makedirs(base_dir)


#     for subdir in subdirs.keys():
#         subdir_path = os.path.join(base_dir, subdir) 

#         if not os.path.exists(subdir_path):
#             os.makedirs(subdir_path) 



#     files = [f for f in os.listdir() if os.path.isfile(f)]    

#     for file in  files:
#         file_ext = os.path.splitext(file)[1].lower()
#         moved = False   


#         for subdir, extensions in subdirs.items():
#             if file_ext in extensions:
#                 shutil.move(file, os.path.join(base_dir, subdir, file)) 
#                 moved = True
#                 break



#         if not moved:
#             shutil.move(file, os.path.join(base_dir, "others", file))    



#     print("Organized files in workspace")  

#     for subdir in subdirs.keys():
#         print(f"{subdir}/: {os.listdir(os.path.join(base_dir, subdir))}")              



# if __name__ == "__main__":
#     organize_files() 




















# Write a Python script that:

# Lists all directories inside the current working directory using os.listdir().
# Checks if a directory is empty using os.listdir().
# If the directory is empty, delete it using os.rmdir().
# If the directory is not empty, ask the user if they want to delete it using shutil.rmtree().



# Solution:




# import os
# import shutil


# def list_dir():
#     return [d for d in os.listdir() if os.path.isdir(d)]


# def delete_dir(dir):
#     if not os.listdir(dir):
#         os.rmdir(dir)
#         print(f"Deleted Empty Directory: {dir}")

#     else:
#         confirm = input(f"{dir} is not empty. Do you want to Delete this folder? (yes/No): ")

#         if confirm.lower() == "yes":
#             shutil.rmtree(dir)
#             print(f"{dir} is Deleted.")
#         else:
#             print("Deletion canceled!")


# def main():
#     directories = list_dir()
    
#     if not directories:
#         print("No Directory Found")
#         return
    
#     for dir in directories:
#         delete_dir(dir)



# if __name__ == "__main__":

#     main()        





















# Create a script that:

# Takes a backup of an existing directory by:
# Checking if a directory named backup exists, if not, creating it.
# Renaming the target directory with a timestamp (e.g., my_project_20250303) using os.rename().
# Moving the renamed directory into backup/.
# Finally, list the contents of backup/.



# Solution:


# import os
# import shutil
# import datetime


# def backup_dir(target_dir):
#     if not os.path.exists(target_dir):
#         print(f"{target_dir} not exists.")
#         return
    

#     # Create backup directory if doesn't exist 
#     backup_dir = "backup"
#     if not os.path.exists(backup_dir):
#         os.mkdir(backup_dir)


#     # Generate timestamped in directory name
#     timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#     new_name = f"{target_dir}_{timestamp}"


#     # Rename directory
#     os.rename(target_dir, new_name)


#     # Move directory to backup folder
#     shutil.move(new_name, backup_dir)



#     # show backup directory content
#     print("Backup content")
#     print(os.listdir(backup_dir))



# backup_dir('hello')    
















# Write a Python script that:

# Lists all files in the current working directory.
# Asks the user to enter a filename to delete.
# Checks if the file exists using os.path.exists().
# If the file exists, ask the user for confirmation before deleting it using os.remove().


# Solution:



# import os
# import shutil


# def delete_file():
    
#     # List all files in the current directory
#     files = [f for f in os.listdir() if os.path.isfile(f)] 
#     print("Files in current Directory")
#     for file in files:
#         print(file)



#     # Ask user for filename to delete
#     filename = input("Enter the filename you want to delete: ")  


#     # checking file existence
#     if os.path.exists(filename):
#         confirm = input(f"Are you sure, you want to delete {filename}? (yes/no): ").strip().lower() 
#         if confirm == "yes":
#             os.remove(filename)
#             print(f"{filename} is deleted")
#         else:
#             print("Deletion canceled")



# delete_file()            

















# Write a program that:

# Creates a directory named recycle_bin/ if it does not exist.
# Moves deleted directories into recycle_bin/ instead of permanently deleting them.
# Allows the user to restore a deleted directory from recycle_bin/ by renaming it back to its original location.


# Solution:


# import os
# import shutil


# # Ensuring recycle_bin or not if not create it

# def ensure_recycle_bin():
#     if not os.path.exists("recycle_bin"):
#         os.makedirs("recycle_bin") 
  


# # Move deleted directories to recycle_bin instead of parmanently deleting

# def move_to_recycle_bin(dir):
#     if os.path.exists(dir) and os.path.isdir(dir):
#         ensure_recycle_bin()
#         shutil.move(dir, os.path.join("recycle_bin", os.path.basename(dir)))
#         print(f"{dir} is moved to recycle_bin")
#     else:
#         print(f"{dir} is not found")




# # Restoring Directory from recycle_bin

# def restore_from_recycle_bin(dir):
#     recycle_path = os.path.join("recycle_bin", dir)
#     if os.path.exists(recycle_path):
#         shutil.move(recycle_path, dir)
#         print(f"{dir} moved from recycle_bin")
#     else:
#         print(f"{dir} is not found")



# def main():
#     while True:
#         print("\nOptions:") 
#         print("1. Move Directory to recycle_bin")       
#         print("2. Move Directory from recycle_bin")       
#         print("3. Exit") 


#         choice = input("Enter your choice: ")

#         if choice == "1":
#             dir_name = input("Enter the directory name to delete: ")
#             move_to_recycle_bin(dir_name)

#         elif choice == "2":
#             dir_name = input("Enter the directory name to restore: ")
#             restore_from_recycle_bin(dir_name)
#         elif choice == "3":
#             break
#         else:
#             print("Invalid Input")


# if __name__ == "__main__":
#     main()            



           

          







 


# Write a program that:

# Creates 100 folders named Folder_1 to Folder_100 using a loop and os.mkdir().
# After creation, lists all the folders to verify.
# Deletes all folders using shutil.rmtree() after confirmation.


#Solution:


# import os
# import shutil


# # Creating Folders from 1 to 100:

# def create_folders():
#     parent_folder = "Folder"

#     if not os.path.exists(parent_folder):
#         os.makedirs(parent_folder)

#         for n in range(1, 101):
#             os.makedirs(os.path.join(parent_folder, f"Folder_{n}" ))
#         print(f"100 folders are created successfully inside 'Folder'")

#     else:
#         print(f"{parent_folder} already exists")


 

# # List all created folders inside "folder":

# def list_folders():
#     parent_folder = "Folder"
#     if os.path.exists(parent_folder):
#         folders = [f for f in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder,f))]
#         print(f"All folders inside 'Folder': {folders}")
#     else:
#         print("Folder doesn't exist. First create it.")
     



# # Deleting all folders inside folder with confirmation  
# def delete_folders():
#     parent_folder = "Folder"
#     confirm = input(f"Do you want to delete all folders inside 'Folder'? (yes/no): ").strip().lower()
#     if confirm == "yes":
#         shutil.rmtree(parent_folder, ignore_errors=True)
#         print("All folders inside 'Folder' are deleted.")
#     else:
#         print("Deletion canceled.")



# def main():
#     while True:
#         print("\nOptions")
#         print("1. Create 100 folders inside 'Folder' ")
#         print("2. List all 100 folders inside 'Folder' ")
#         print("3. Delete all 100 folders inside 'Folder' ")
#         print("4. Exit ")

#         choice = input("Enter you choice: ").strip()

#         if choice == "1":
#             create_folders()
#         elif choice == "2":
#             list_folders()
#         elif choice == "3":
#             delete_folders()
#         elif choice == "4":
#             break
#         else:
#             print("Invalid input.") 



# if __name__ == "__main__":
#     main()















# Write a script that:

# Searches for all empty subdirectories inside a given directory.
# Deletes only deeply nested empty directories using os.rmdir().
 



# import os
# import shutil



# # Searches and delete all empty dir inside 'Folder'

# def delete_empty_dir():

#     parent_dir = 'Folder'

#     if not os.path.exists(parent_dir):
#         return
    
#     confirm = input(f"Do you want to delete all empty directories inside {parent_dir}? (yes/no): ").strip().lower() 

#     if confirm != "yes":
#         print(f"Deletion canceled!")
#         return
    

#     empty_folders = [
#         f for f in os.listdir(parent_dir)
#         if os.path.isdir(os.path.join(parent_dir, f)) and not os.listdir(os.path.join(parent_dir, f))
#     ]


#     if not empty_folders:
#         print("No empty folder exists")
#         return
    
#     for folder in empty_folders:
#         os.rmdir(os.path.join(parent_dir, folder))
#         print(f"Deleted: {folder}")
#     print("All empty folders  are successfully deleted.")  



# if __name__ == "__main__":

#     delete_empty_dir()









 