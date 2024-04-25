import os
#Get the current working directory
print(f'current working directory is : {os.getcwd()}')

#Change the current working directory
d='folder'
os.chdir(d)
print(f'The updated working directory is {os.getcwd()}')

print(f'The contents of the working directory is {os.listdir(os.getcwd())}')

d='C:/Users/91736/OneDrive/Documents/NamePython/folder'
os.chdir(d)
print(f'The current working directory is {os.getcwd()}')
print(f'The contents of the working directory is {os.listdir(os.getcwd())}')


# d='Standard Library'
# os.chdir(d)


#Create a new directory
# d='New folder'
# os.mkdir(d)
# if os.path.exists(d):
#     print(f'Directory called {d} has been successfully created')
# else:
#     print(f'Directory called {d} is already exists')

#Remove directory
d='New folder'
if os.path.exists(d):
    os.rmdir(d)
    print(f'Directory called {d} has been successfully removed')
else:
    print(f'Directory called {d} does not exists')

#Join path component intelligently
p1 = 'C:/Users/91736/OneDrive/'
p2 = 'Documents/NamePython/folder'
print(f'Joined path is {os.path.join(p1,p2)}')

#Check if the path exists
# if os.path.join(p1,p2):
#     print(f'Joined path {os.path.join(p1,p2)} exists')
# else:
#     print(f'Invalid path')

if os.path.join(p2,p1):
    print(f'Joined path {os.path.join(p2, p1)} exists')
else:
    print(f'Invalid path')

#Check if a path points to a directory or file
p='C:/Users/91736/OneDrive/Documents/NamePython'
if os.path.isdir(p):
    print(f'Path {p} points to a directory')
elif os.path.isfile(p):
    print(f'Path {p} points to a file')
else:
    print(f'Path {p} does not exists')

#Get the user's home directory from the environment variable
if 'USERPROFILE' in os.environ:
    print(f'Home directory is {os.environ['USERPROFILE']}')
else:
    print("Environment variable 'USERPROFILE' does not exist")

#Execute a shell command and check its exit code
r=os.system("ping -n 3 google.com")
print(r)
if r==0:
    print("Ping is successful")
else:
    print("Ping is unsuccessful")

r=os.system("dir")
print(r)

#Run a command and capture its output using a pipe
p=os.popen('dir')
print(f'The process output is {p.read()}')