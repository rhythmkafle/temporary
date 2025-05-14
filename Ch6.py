'''
Ch6 - File Handling

Introduction
    - process to create, read, write and delete files
    - helps interact with files 

Basic Syntax:
    - file = open('filename.txt', 'mode')

    - mode is the way you want to interact with files


File Opening Modes
    - r mode i.e. read
    - w mode i.e. write
    - a mode i.e. append
    - r+ mode i.e. read and write
    - w+ mode i.e. write and read (same)
    - a+ mode i.e. read and append
    - x mode i.e. create
    - b mode i.e. binary mode (rb, wb, ab)
    - t mode i.e. text mode(default)

    - we normally interact with only r, w, a and binary modes

    - the difference between w and a mode is that w mode overwrites a file's content, whereas a mode appends on previous content
'''


'''
Reading and Writing files
    - use r for reading, w or a for writing
'''
# Writing to a file 'data.txt'
file = open('data.txt', 'w')
file.write("Hello World!")
file.close()    # always close the file

# Reading from the file 'data.txt'
file = open('data.txt', 'r')
content = file.read()
print(content)  # Output: Hello World!
file.close()

# Now, if you use 'w' mode again, we will overwrite the file i.e. Hello World! will be deleted and new content will be added
# If we dont want to delete the existing content, we use the 'a' mode
file = open('data.txt', 'a')
file.write("\nThis is a new line, new content.")
file.close()

# We can read only one line of a file using the .readline() method
file = open('data.txt', 'r')
print(file.readline()) # Output: Hello World! (the other lines of a file are not read. To read all the lines, we use a loop)

for lines in file.readline():
    print(lines)    
# Output: Hello World!
#         This is a new line, new content. 



'''
The os module and common functions
    - it is used for file/directory management
'''

import os
print(os.getcwd()) # prints the current directory
os.mkdir("new_folder") # makes a new folder called new_folder
os.rmdir("new_folder") # removes the folder
# os.rename("data.txt", "new_data.txt") # renames the file data.txt into new_data.txt
print(os.listdir()) # lists files and folders in the current directory in form of a list    



'''
The with statement
    - used as a context manager to handle file operations 
    - automatically closes the file after the block finishes i.e. no need to manually close the file
'''

# Reading a file using with
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)
# You can use it the same way to read, write or append files

'''
Binary Modes - not specifically mentioned in the syllabus, But no trust in TU
    - used to read or write non-text files, such as images or videos
    - they handle raw bytes(0s and 1s), not strings 
'''
# Reading an image file
with open('image.png', 'rb') as image_file:
    data = image_file.read()
    print(data)

# Snippet of the output: e2\xc0G\x90\x86\x91}}#\x1e\x198\x19\xc3\x89\xa1\xcd\t\xd7\xb2\xc0\xcbmkk>\x16\xb

'''
Finished!!!
'''