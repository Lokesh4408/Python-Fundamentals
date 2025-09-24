import os

#os.rename('first_draft.txt','finished_masterpiece.txt')
x = os.path.exists('novel.txt')
print(x)

y = os.path.getsize('novel.txt') # this code will provide the size of the file in bytes.
print(y, 'bytes')

z = os.path.getmtime('novel.txt') # this code will provide the last modification time of the file in seconds since epoch.
print(z)

import datetime
timestamp = os.path.getmtime('novel.txt')
print(datetime.datetime.fromtimestamp(timestamp)) # this code will convert the timestamp into a readable format.

print('Absolute path: ',os.path.abspath('novel.txt')) # this code will provide the absolute path of the file.

print('Current Working Directory: ', os.getcwd()) # this code will provide the current working directory.

os.rmdir('new_dir') if os.path.exists('new_dir') else None
# os.mkdir('new_dir')
# os.chdir('new_dir')
# os.rmdir('new_dir') # this will remove the directory only if it is empty.
# print(os.getcwd())
os.mkdir('newer_dir')
os.rmdir('newer_dir')
print(os.getcwd())

print(os.listdir('C:/Users/ivanr/OneDrive/Desktop/github/Python-Fundamentals/GooglePart2Certification')) # this code will list all files and directories in the current working directory as a list.

dir = 'C:/Users/ivanr/OneDrive/Desktop/github/Python-Fundamentals/GooglePart2Certification'
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print('{} is a directory'.format(name))
    else:
        print('{} is a file'.format(name))