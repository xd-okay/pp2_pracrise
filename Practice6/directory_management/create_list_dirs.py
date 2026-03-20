import os
import shutil
# os.makedirs("dir1")
# os.removedirs("dir1")
# os.makedirs("dir1/subdir1")
# os.makedirs("dir1/subdir2")
# os.makedirs("dir1/subdir1/sub_sub_dir1")
# os.makedirs("dir1/subdir2/sub_sub_dir1")
list_dir=os.listdir("dir1")
print(list_dir)

for f in list_dir:
    if(f[-4:]==".txt"):
        print(f)
        c="dir1/"+f
        
        shutil.move(c, "dir1/subdir1")