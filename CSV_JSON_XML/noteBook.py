 # Read CSV files with the method reader()
import csv
with open('data.csv','r') as f:
    reader= csv.reader(f)
    for r in reader:
        print(r)

print(r[0][2])
print(type(reader))
print(r[0])

#Remove Space after delimiter
        
with open('data.csv','r') as f:
    reader= csv.reader(f, skipinitialspace=True)
    for r in reader:
        print(r)

#Read Text File as CSV File
        
with open('data.txt') as f:
    reader=csv.reader(f, skipinitialspace=True)
    for r in reader:
        print(r)

with open('data1.txt') as f:
    reader=csv.reader(f, skipinitialspace=True)
    for r in reader:
        print(r)
        
with open('data.txt') as f:
    reader=csv.reader(f, skipinitialspace=True)
    for r in reader:
        print(r)

with open('data.txt') as f:
    reader=csv.reader(f, delimiter=';',skipinitialspace=True)
    for r in reader:
        print(r)

#Split into column header and values
#first way
with open('data.txt') as f:
    reader=csv.reader(f, delimiter=';', skipinitialspace=True)
    lc= 0
    for r in reader:
        if lc==0:
            print(f'column names are {", ".join(r)}')
            lc+=1
        else:
            print(r)
            lc+=1
    print(f'The total number of lines read is {lc}')


#second Way
with open('data.txt') as f:
    reader=csv.reader(f, delimiter=';',skipinitialspace=True)
    lc= 0
    for r in reader:
        if lc==0:
            print(f'column names are {", ".join(r)}')
            lc+=1
        else:
            print(f'{r[0]} aged {r[1]} years works in {r[2]} with a salary of {r[3]} Rs.')
            lc+=1
    print(f'The total number of lines read is {lc}')

#For CSV File
with open('data.csv') as f:
    reader=csv.reader(f,delimiter='|', skipinitialspace=True)
    lc= 0
    for r in reader:
        if lc==0:
            print(f'column names are {", ".join(r)}')
            lc+=1
        else:
            print(f'{r[0]} aged {r[1]} years works as {r[2]}')
            lc+=1
    print(f'The total number of lines read is {lc}')


#Read CSV files with DictReader
#First way
with open('data.csv') as f:
    reader=csv.DictReader(f, delimiter='|', skipinitialspace=True)
    lc=0
    for r in reader:
        if lc==0:
            print(f'column names are {", ".join(r)}')
            lc+=1
        else:
            print(f'{r['Name']} aged {r['Age']} years works as {r['Designation']}')
            lc+=1
    print(f'The total number of lines processed {lc}')

#second way
with open('data.csv') as f:
    reader=csv.DictReader(f, delimiter='|', skipinitialspace=True)
    lc=0
    for r in reader:
        if lc==0:
            print(f'column names are {", ".join(r)}')
            lc+=1
        else:
            print(f'{r.get('Name')} aged {r.get('Age')} years works as {r.get('Designation')}')
            lc+=1
    print(f'The total number of lines processed {lc}')

#For data.txt File
with open('data.txt') as f:
    reader=csv.DictReader(f, delimiter=';', skipinitialspace=True)
    lc=0
    for r in reader:
        if lc==0:
            print(f'column names are {", ".join(r)}')
            lc+=1
        else:
            print(f'{r['Name']} aged {r['Age']} years works in {r['Department']} with a salary of {r['Salary']}')
            lc+=1
    print(f'The total number of lines processed {lc}')
'''
#Read a file name.txt and calculate the average age. Print the names that are close to the average age
with open('name.txt') as f:
    reader=csv.DictReader(f)

def calculate_average_age(data):
    total_age = sum(int(row['Age']) for row in data)
    return total_age/ len(data)
'''
