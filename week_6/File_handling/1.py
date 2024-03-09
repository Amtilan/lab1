import os

path = "C:\\Users\\РАЙЫМБЕК\\OneDrive\\Документы\\GitHub\\pp2-kbtu\\week_6\\File_handling"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
for i in dir_list:
    print(i, end="\n")
    