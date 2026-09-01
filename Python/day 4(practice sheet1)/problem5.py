# Label program written in problem 4 with comments
import os

# Select the directory you want to list
directory_path='/'

# Use os module to list all files and directories of the selected path
contents=os.listdir(directory_path)

# Print the contents of the directory
print (contents)