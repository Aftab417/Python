
###################----------------  OS MODULE -----------------########################


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









# Write a Python script that:

# Lists all files in the current working directory.
# Asks the user to enter a filename to delete.
# Checks if the file exists using os.path.exists().
# If the file exists, ask the user for confirmation before deleting it using os.remove().









# Write a Python script that:

# Lists all files in a folder.
# Renames all .txt files to have a _backup suffix before the extension.
# Example: notes.txt → notes_backup.txt
# Print the updated list of files.












# Write a program that:

# Creates a directory named recycle_bin/ if it does not exist.
# Moves deleted directories into recycle_bin/ instead of permanently deleting them.
# Allows the user to restore a deleted directory from recycle_bin/ by renaming it back to its original location.













# Write a script that:

# Captures a list of files and directories in a folder before and after making changes.
# After renaming, creating, or deleting files, compare the old and new lists.
# Print which files were added, removed, or renamed.















# Write a program that:

# Creates 100 folders named Folder_1 to Folder_100 using a loop and os.mkdir().
# After creation, lists all the folders to verify.
# Deletes all folders using shutil.rmtree() after confirmation.











# Write a script that:

# Searches for all empty subdirectories inside a given directory.
# Deletes only deeply nested empty directories using os.rmdir().
# If a directory is not empty, move its contents to the parent directory before deleting it.













# Write a script that:

# Finds all .log files in the current directory.
# Renames each .log file to have a .bak extension before deleting it.
# Example: server.log → server.bak → then delete it.
# If a .bak version already exists, append a number to the filename (server_1.bak, server_2.bak, etc.).

