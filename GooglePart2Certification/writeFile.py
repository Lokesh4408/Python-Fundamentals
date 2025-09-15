with open('novel.txt', 'w') as file:
    file.write("It was a dark and stormy night.")


'''The with open() statement creates a file object and assigns it to the variable file. 
The open() function takes two arguments: the name of the file and the mode. In this case, the mode is w, which means "write". 
This tells the open() function to create a new file if it doesn't exist, or to overwrite the existing file if it does exist.

The write() method of the file object takes a string as its argument and writes the string to the file. 
In this case, the string is "It was a dark and stormy night".

Mode:
The mode argument is optional, and it specifies the mode in which the file is opened. If omitted, it defaults to ”r” and that means opening for reading in text mode. The common modes include:

“r”  open for reading (default)

“w”  open for writing, truncating the file first

“x”  open for exclusive creation, failing if the file already exists

“a”  open for writing, appending to the end of the file if it exists

“+”  open for both reading and writing

Attempting to write to a file opened for read (“r”) will cause a runtime error.


***To open a file for reading or writing, use open(filename, mode). Two arguments that are needed include the file name and the mode. 
Python will encode the file as text (“t”) by default unless a specific encoding is specified.
'''