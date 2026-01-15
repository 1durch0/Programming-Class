import os
import shutil

print(f"current working directory: {os.getcwd()} has following files and directories: {os.listdir()}")

# creating folder and iles

def create_file(file_name, content=""):
    if not os.path.exists(file_name):
        with open(file_name, 'w') as f:
            f.write(content)
        print(f"Created file: {file_name}")

def create_directory(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print(f"Created directory: {dir_name}\n")

def delete_everything(dir_name):
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)

def list_files(dir_name):
    if os.path.exists(dir_name):
        return os.listdir(dir_name)
    return []
def rename_file(old_name, new_name):
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"Renamed file from {old_name} to {new_name}")

create_directory("lab_files")
create_file("lab_files/file1.txt", "This is the content of file 1.")
create_file("lab_files/file2.txt", "This is the content of file 2.")
create_file("lab_files/file3.txt", "This is the content of file 3.")
rename_file("lab_files/file3.txt", "lab_files/new_name")
print(f"\n{list_files("lab_files")} are present in lab_files directory.\n")
delete_everything("lab_files")