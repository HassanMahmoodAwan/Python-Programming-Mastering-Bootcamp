"""
- OS -> interacting with operating system. 

"""

import os


# ==== Current Working Directory ===== #
print('Current working dir: ', os.getcwd())


# ==== Change Current Working Directory ===== #
print('Current working dir: ', os.getcwd())
os.chdir('../')                               # back on folder.
print('Current working dir: ', os.getcwd())


# ==== Creating New Directory ===== #
current_path = os.getcwd(); Working_dir = 'File Handling'
path = os.path.join(current_path,Working_dir)
new_folder = 'os_folder'
new_path = os.path.join(path, new_folder)
os.mkdir(new_path)
print('========= new folder created =======')


# ====== Remove FIlE using OS ======= #
try:
    file_path = os.path.join(path, 'removingfile.txt')
    os.remove(file_path)
except OSError:
    print('File not exist')


# ====== Remove Dir using OS ======= #
try:
    dir_path = os.path.join(path, 'os_folder')
    os.rmdir(dir_path)
except OSError:
    print('Folder not Exist')