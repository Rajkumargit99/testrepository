import os

print(os.getcwd())

print("-------------------------------------------------------------")

# os.mkdir()
# os.rmdir()

#os.makedirs("folder1")

#os.removedirs("folder1")

#os.makedirs(r"C:\Users\LENOVO\Desktop\Python Sessions\hope1")
#os.removedirs(r"C:\Users\LENOVO\Desktop\Python Sessions\hope5")

#for i in range(1,6):
    #os.makedirs(rf"C:\Users\LENOVO\Desktop\Python Sessions\hope1{i}")
    # os.makedirs(rf"C:\Users\LENOVO\Desktop\Python Sessions\hope{i}")
#
# print(os.getenv("path"))
#
# print(os.getenv("OS"))
#
# print(os.getenv("PyCharm"))

print("-------------------------------------------------------------")

# src = r"C:\Users\LENOVO\Desktop\Manual Testing"
# filename = "Module4"
#
# file_path = os.path.join(src, filename)
# print("path:", file_path)

import shutil

# path1 = r"C:\Users\LENOVO\Desktop\Manual Testing\Module4.txt"
# path2 = r"C:\Users\LENOVO\Desktop\Python Sessions\Module4.txt"
# path3 = r"C:\Users\LENOVO\Desktop\Python Sessions\Module4.new.txt"
#
# shutil.copy(path1, path2)
# shutil.copy(path1, path3)

list = os.listdir(r"C:\Users\LENOVO\Desktop\Manual Testing")

print(list)

