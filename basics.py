import os

"""HANDLING THE CURRENT WORKING DIRECTORY"""
"""obtain the current working directory of a project"""

# cwd = os.getcwd()
# print(cwd)
url = "c:/users/ebizh/onedrive/desktop/documentations"
# to change directory use
# os.chdir('c:/users/ebizh/onedrive/desktop/documentations')
#
# cwd = os.getcwd()
# print(cwd)

"""change directory by one level"""
# print(os.getcwd())
# os.chdir(url)
# os.chdir("../")
# print(os.getcwd())

"""CREATING A DIRECTORY"""

# directory = "os full"
# sub_directory = "os main"
#
# parent_directory = "c:/users/ebizh/onedrive/desktop/os full/"
#
# path = os.path.join(parent_directory, directory)
# try:
#     os.mkdir(path)
# except FileExistsError:
#     print(f'Folder: "{directory}" already exists')
# else:
#     print(f'Folder: "{directory}" created successfully')
#
# # a second method for creating a directory using mode
#
# path1 = os.path.join(parent_directory, sub_directory)
# mode = 0o666
#
# try:
#     os.makedirs(path1, mode)
# except FileExistsError:
#     print(f'Folder {sub_directory} already exists')
# else:
#     print(f'Folder {sub_directory} created successfully')




