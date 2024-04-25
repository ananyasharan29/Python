#loads is for console data
#load is for file data which is already in json
#dumps convert a python object to json string 
#dump convert python object(list/dict) to json

import json

#Use of Loads method

# p = '{"name": "AAA", "language": ["English", "Hindi", "Kannada"]}'
# print(type(p))

# p_1 = json.loads(p)
# print(p_1)

# # Use Load Method
# f=open('n.json')
# d=json.load(f)
# print(type(d))
# print(d)

f=open('employee.json')
e=json.load(f)
print(e)

#Highest salary
max_salary =0
for employee in e:
  if 'salary' in employee:
    max_salary = max(max_salary, employee['salary'])
print("Highest salary:", max_salary)

#lowest salary
min_salary =99999999
for employee in e:
  if 'salary' in employee:
    min_salary = min(min_salary, employee['salary'])
print("Lowest  salary:", min_salary)

#Average
total_salary=0



# f=open('address.json')
# data = json.load(f)
# for n in data:
#     print("name : ", n)
#     print("Age : ", data[n]['age'])
#     print("Phone no. : ", data[n]['Phone no.'])
#     print("Address : ", data[n]['Address'])

#Convert a dictionary to a JSON object
# d={'name':'AAA', 'age':35, 'married':False, 'children':None}
# d_j=json.dumps(d)
# print(type(d_j))
# print(d)
# print(d_j)

# f=open('n_1.json','w')
# json.dump(d,f)

# #pretty Print option
# f=open('n_2.json','w')
# json.dump(d, f, indent = 4)

# f=open('n_3.json','w')
# json.dump(d, f, indent = 8)

# #Sort the data while storing
# f=open('n_4.json','w')
# json.dump(d, f, sort_keys=True)

# ########################################
# d1=[
#     {'name':'AAA', 'age':35, 'married':False, 'children':None},
#     {'name':'BBB', 'age':40, 'married':True, 'children':2}
#    ]
# f=open('n_5.json','w')
# json.dump(d1,f)

# f=open('n_6.json','w')
# json.dump(d1,f, sort_keys=True)

# #Assume a json file that has data of name age salary and department,
# #write python script to display the lowest salary, the highest salary and the average age.

