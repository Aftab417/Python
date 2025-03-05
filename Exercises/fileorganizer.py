
import os
import shutil


def organize_files():

    base_dir = "workspace"
    subdirs = {
        "images" : [".jpg", ".png", ".gif", ".jpeg"],
        "documents" : [".txt", ".pdf", ".docx"],
        "videos" : [".mp4"],
        "audioes" : [".mp3"],
        "coding_files" : [".py", ".html", ".js", ".php", ".css"],
        "others" : []
    }



    if not os.path.exists(base_dir):
        os.makedirs(base_dir)


    for subdir in subdirs.keys():
        subdir_path = os.path.join(base_dir, subdir) 

        if not os.path.exists(subdir_path):
            os.makedirs(subdir_path) 



    files = [f for f in os.listdir() if os.path.isfile(f)]    

    for file in  files:
        file_ext = os.path.splitext(file)[1].lower()
        moved = False   


        for subdir, extensions in subdirs.items():
            if file_ext in extensions:
                shutil.move(file, os.path.join(base_dir, subdir, file)) 
                moved = True
                break



        if not moved:
            shutil.move(file, os.path.join(base_dir, "others", file))    



    print("Organized files in workspace")  

    for subdir in subdirs.keys():
        print(f"{subdir}/: {os.listdir(os.path.join(base_dir, subdir))}")              



if __name__ == "__main__":
    organize_files() 

