"""
- File handling in Python is a powerful. 
- File handling allows users to handle files i.e., to read and write files
- Along with many other file handling options, to operate on files.


Modes:
    r:  READ file.
    w:  WRITE in file.
    a:  APPEND in file.
    === Advance Modes ===
        - r+: 
        - w+: 
        - a+: 


Note: File handling in Python is slower than other programming languages, especially when dealing with large files. 
"""

# ==== Open file and Read ===== #
try:
    file = open('./data.txt', 'r')
except IOError:                 
    print('File not Exsist')

for line in file:                       # It read each line.
    print(line)


# ==== READ each line in file ===== #
file = open('./data.txt', 'r')
print(file.read())


# ==== Another: READ each line in file ===== #
with open('./data.txt', 'r') as file:
    data = file.read()
print(data)


# ===== READLINES: list of each line in file ===== #
with open('./data.txt', 'r') as file:
    data = file.readlines()
print(data)


# ===== READLINES: list of words each line ===== #
with open('./data.txt', 'r') as file:
    data = file.readlines()
    for line in data:
        print(line.split())



# ==== READ Char from txt file ==== #
with open('./data.txt', 'r') as file:
    print(file.read(10))
    