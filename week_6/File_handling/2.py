import os

print('Exist:', os.access('C:\\Users\\РАЙЫМБЕК\\OneDrive\\Документы\\GitHub\\pp2-kbtu\\week_6\\File_handling', os.F_OK))
print('Readable:', os.access('C:\\Users\\РАЙЫМБЕК\\OneDrive\\Документы\\GitHub\\pp2-kbtu\\week_6\\File_handling', os.R_OK))
print('Writable:', os.access('C:\\Users\\РАЙЫМБЕК\\OneDrive\\Документы\\GitHub\\pp2-kbtu\\week_6\\File_handling', os.W_OK))
print('Executable:', os.access('C:\\Users\\РАЙЫМБЕК\\OneDrive\\Документы\\GitHub\\pp2-kbtu\\week_6\\File_handling', os.X_OK))