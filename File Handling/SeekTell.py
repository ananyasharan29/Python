#Seek and Tell Function

#seek() - where is the current pointer pointing to.
#tell() - go to a given specific position in a file.

# with open('sample.txt', 'r') as f:
#     print(f.read(10), end='')
#     print(f.tell())
#     f.seek(0)
#     print(f.read(10), end='')
#     print(f.tell())

    #Seek during write
with open('sample.txt', 'w') as f:
    f.write('Hello')
    f.seek(0)
    f.write('xa')