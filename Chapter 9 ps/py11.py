#Write a python program to rename a file to “renamed_by_ python.txt.
import os
import shutil

# with open("old.txt") as f:
#     content = f.read()

# with open("renamed_by_ python.txt", "w") as f2:
#     f2.write(content)

# os.rename("old.txt","renamed_by_ python.txt")  

shutil.move("old.txt", "renamed_by_python.txt")

print("Name changed successfully.")

