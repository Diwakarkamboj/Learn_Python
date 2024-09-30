import os

# Specify the directory you want to list
directory = '/python'

# List all files and directories in the specified path

contents = os.listdir(directory)
print("Contents of the directory:")
print(contents)

# for item in contents:
#     print(item)
