#File Handling

# Types of data used for I/O - text, binary

# There are two files type to deal with 
#   Text Files - all programs files are text files
#   Binary Files - Images, music, videos, exe files

# Functions done in file handling
#   -Open a file
#   -Read/Write data
#   -Close the file
 
# # Writing to a file
# #Case 1: if the file is not present
# f= open('sample.txt','w')
# f.write('Hello Ananya!')
# f.close() 
# # f.write('Hello') --since file is closed hence this will not work

# #Write multiline strings
# f = open('sample1.txt','w')
# f.write('Hello world')
# f.write('\nHow are you?')
# f.close()

# #Case 2: if the file is already present
# f = open('sample.txt', 'w')
# f.write('Hello Parul!')
# f.close() #if you try to write in existing file, that replaced whole old content with the new one

# #Buffer memory - reads all data line by line

# # Problem with w mode - it'll replace the old contents with the new one
# # Then , introducing append 'a' mode
# f = open('sample1.txt','a')
# f.write('\nI am fine.')
# f.close()

# # write lines
# l =['Hello\n', 'Hii\n', 'How are you?\n', 'I am fine.']
# f = open('sample.txt', 'w')
# f.writelines(l) 
# f.close()

# # why f.close()? --memory free, safety purpose 

# #Reading from file
# # There is two way of reading a file - 1. read() - it reads the whole content
# #                                      2. readline() - it reads a line at a time

# #1. read() - it reads the whole content
# f = open('sample.txt', 'r')
# s = f.read()
# print(s)
# f.close() 

# f = open('sample.txt', 'r')
# s = f.read(8) #--if we want to read 10 characters only ,we can read like this 
# print(s)
# f.close() 

# # 2. readline() - it reads a line at a time
# f = open('sample.txt', 'r')
# print(f.readline(), end='')
# print(f.readline(), end='')
# f.close() 

# #reading entire lines using this
# f = open('sample.txt', 'r')
# while True:
#     data = f.readline()

#     if data == '':
#         break
#     else:
#         print(data, end='')
# f.close()

#Problems with working in text mode
#  --can't work bbinary files like images
#  --not good for other data types like int/float/list/tuples

#Working with binary file
# For the solution of first problem we will work on rb, wb mode for read and write a binary file
with open('Screenshot.png', 'rb') as f:
    with open('Screenshot1.png', 'wb') as wf:
        wf.write(f.read())

