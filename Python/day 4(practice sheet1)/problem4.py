# Write a program in python to print the contents of directory using os module . Search online for function which does that.

import os

directory_path='/'

contents=os.listdir(directory_path)

for item in contents:
    print (item)

