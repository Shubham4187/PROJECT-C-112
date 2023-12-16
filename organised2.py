import os
import shutil

from_dir="C:/Users/shubh/Downloads"
to_dir="D:/demo files"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name , extension= os.path.splitext(file_name)
    #print(name)
    #print(extension)
    if extension=="":
        continue
    if extension in ['.pdf', '.doc','.ppt', '.xls','.heic', '.txt']:
        path1=from_dir + "/" + file_name
        path2=to_dir + "/" + "DocFiles"
        path3=to_dir + "/" + "DocFiles" + "/" + file_name

        if os.path.exists(path2):
            shutil.move(path1 , path3)
        else:
            os.makedirs(path2)
            shutil.move(path1 , path3)