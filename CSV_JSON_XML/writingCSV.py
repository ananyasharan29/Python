import csv

with open('emp.csv', 'w') as f:
    w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    w.writerow(['Name', 'Department', 'Salary'])
    w.writerow(['ABC PQR', 'Accounting', 50000])
    w.writerow(['LMN XYZ', 'IT', 55000])
    w.writerow(['PQR GHI', 'Management', 60000])

# QUOTE_MINIMAL - default, quote fields only if they contain delimiter or quotechar
# QUOTE_ALL - quotes all fields
# QUOTE_NONE- escape delimiters
# QUOTE_NONNUMERIC - quote all fields that contain text data and converts numeric fields to float

# with open('emp_1.csv', 'w') as f:
#     w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     w.writerow(['Name', 'Department', 'Salary'])
#     w.writerow(['ABC PQR', 'Accounting', 50000])
#     w.writerow(['LMN XYZ', 'IT', 55000])
#     w.writerow(['PQR GHI', 'Management', 60000])

# with open('emp_2.csv', 'w') as f:
#     w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
#     w.writerow(['Name', 'Department', 'Salary'])
#     w.writerow(['ABC PQR', 'Accounting', 50000])
#     w.writerow(['LMN XYZ', 'IT', 55000])
#     w.writerow(['PQR GHI', 'Management', 60000])

# with open('emp_3.csv', 'w') as f:
#     w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
#     w.writerow(['Name', 'Department', 'Salary'])
#     w.writerow(['ABC PQR', 'Accounting', 50000])
#     w.writerow(['LMN XYZ', 'IT', 55000])
#     w.writerow(['PQR GHI', 'Management', 60000])

# with open('emp_4.csv', 'w') as f:
#     w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
#     w.writerow(['Name', 'Department', 'Salary'])
#     w.writerow(['ABC PQR', 'Accounting', 50000])
#     w.writerow(['LMN XYZ', 'IT', 55000])
#     w.writerow(['PQR GHI', 'Management', 60000])

#Write csv files with dictionary
# with open('emp_head.csv', 'w') as f:
#     fn=['Name', 'Age', 'Department']
#     w=csv.DictWriter(f, fieldnames=fn)
#     w.writeheader()
#     w.writerow({'Name':'Ananya', 'Age': 22, 'Department': 'IT'})
#     w.writerow({'Name':'Anamika', 'Age': 26, 'Department': 'Management'})

#Text File
# with open('emp_head.txt', 'w') as f:
#     fn=['Name', 'Age', 'Department']
#     w=csv.DictWriter(f, fieldnames=fn)
#     w.writeheader()
#     w.writerow({'Name':'Ananya', 'Age': 22, 'Department': 'IT'})
#     w.writerow({'Name':'Anamika', 'Age': 26, 'Department': 'Management'})

# works with csv files using the Pandas Packaage
# We can store the data in two different types
# Data Frames - a 2D data type
# Series - a 1D data type
import pandas as pd

# df=pd.read_csv('emp_head.csv')
# print(type(df))
# print(df)
# print(df['Name'])
# print(df['Age'])
# # print(df[0]) --error
# # print(df['Ananya']) --error
# df=pd.read_csv('emp_head.txt')
# print(type(df))
# print(df)
# df=pd.read_csv('emp_head.txt', delimiter=';')
# print(df)
# print(df.loc[0])
# print(df.loc[1])
# print(df.loc[2]) --value error
# print(df.loc[0][1])
# print(df['Name'][0])

#Create a Data Frame (two dimensional data type)
#First Method
v=[['ABC FGH', 23, 'Sales', 68569], ['PQR YOU', 30, 'IT', 27924], ['XYZ HGH', 35, 'Accounts', 64582]]
print(type(v))
df=pd.DataFrame(v, columns=['Name', 'Age', 'Department', 'Salary'])
print(df)
df1=pd.DataFrame(v)
print(df1)
# print(df[0]) --key Error
print(df1[0])

#Second Method
v={'Name': ['ABC', 'PQR', "XYZ"],
    'Age': [23,30,35],
    'Deaprtment': ['Sales', 'IT', 'Accounts']}
df2= pd.DataFrame(v)
print(df2)

#Third Method
v=[{'Name': 'ABC', 'Age': 23, 'Department': 'Sales'},
   {'Name': 'PQR', 'Age': 30, 'Department': 'IT'},
   {'Name': 'XYZ', 'Age': 35, 'Department': 'Accounts'}]
df3= pd.DataFrame(v)
print(df3)

#Fourth Method
v=[{'Name': 'Ananya', 'Age': 22},
   {'Name': 'Anukamal', 'Age': 21, 'Department': 'IT'},
   {'Name': 'Govind', 'Age': 23, 'Department': 'Accounts'}]
df4= pd.DataFrame(v, index=[1,2,3])
print(df4)

#Write the Dateframes into Files
df.to_csv('emp_5.csv')
df1.to_csv('emp_6.txt')
df.to_csv('emp_5.csv', index=True)
df.to_csv('emp_5.csv', index=False)

#Add a new column called as Birth Year and values are to be calculated based on age
v=[{'First Name': 'Ananya', 'Last Name': 'Sharan',  'Age': 22, 'Salary': 50000, 'Department': 'Sales'},
   {'First Name': 'Anukamal', 'Last Name': 'Sinha', 'Age': 21, 'Salary': 60000, 'Department': 'IT'},
   {'First Name': 'Govind', 'Last Name': 'Kumar','Age': 23, 'Salary': 70000, 'Department': 'Accounts'}]
df5= pd.DataFrame(v)
df5['Birth Year']=2024-df5['Age']
df5=df5[['First Name', 'Last Name', 'Birth Year', 'Age', 'Salary','Department']]

print(df5)
df['Birth Year']=2024-df['Age']


df5.to_csv('name_1.txt', index=False)
df5.to_csv('name_1.csv', index=False)
print(df5)

df.to_csv('name_2.txt', index=False)
df.to_csv('name_2.csv', index=False)
df['Birth Year']=2024-df['Age']
df[['First Name', 'Last Name']]=df['Name'].str.split(' ', n=1, expand=True)
df.drop(columns=['Name'], inplace=True)
df=df[['First Name', 'Last Name', 'Age', 'Birth Year', 'Salary','Department']]
print(df)

#Assume a csv file that contains data for name, age, department, designation, salary. 
# Find out which department has the least salary , which department has the highest age?

data = pd.read_csv('name_2.csv')
least_sal = data.groupby('Department')['Salary'].mean().idxmin()
highest_age = data.groupby('Department')['Age'].max().idxmax()
print('Department with least Salary :',least_sal)
print('Department with highest age :', highest_age)

#second Way CSV
# with open('name_2.csv','r') as file:
#     reader = csv.DictReader(file)
#     min_sal= 999999
#     max_age=0
#     salary_by_department = {}
#     age_by_department = {}
#     for row in reader:
#         department = row['Department']
#         salary = float(row['Salary'])
#         age = int(row['Age'])
#         if department in salary_by_department:
#             salary_by_department[department] += salary
#             if age > age_by_department[department]:
#                 age_by_department[department] = age
#             else:
#                salary_by_department[department] = salary
#                age_by_department[department] = age
# least_sal = min(salary_by_department, key=salary_by_department.get)
# highest_age = max(age_by_department, key=age_by_department.get)
# print('Department with least Salary :',least_sal)
# print('Department with highest age :', highest_age)

