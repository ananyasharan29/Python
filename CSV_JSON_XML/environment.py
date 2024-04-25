import os

#Create a dictionary to get the current environment variables
e_v = os.environ
print("Environment Variables")
for k, v in e_v.items():
    print(f'{k}: {v}')

#Get the value of specific environmnet variables
s='PATH'
v=os.getenv(s)
print(f'Value of {s} is {v}')

#Use pipe to execute commands
c='dir*.csv'
p=os.popen(c)
o=p.read()
p.close()
print(f'Output of {c} is {o}')

