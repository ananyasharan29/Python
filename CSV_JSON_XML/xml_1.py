# XML Files 
# ElementTree

import xml.etree.ElementTree as xml

#Create a list of data
Employee=[

    {
        'name':'Ananya',
        'age':22,
        'salary':60000
    },
    {
        'name':'Anamika',
        'age':26,
        'salary':80000
    }
]

#Create a root element
root=xml.Element('Employee')

#Iterate over the list
for e in Employee:
    child=xml.Element('Employee')
    root.append(child)
    n=xml.SubElement(child, 'name')
    n.text=e.get('name')
    a=xml.SubElement(child, 'age')
    ag=e['age']
    a.text=str(ag)
    s=xml.SubElement(child, 'salary')
    sal=e['salary']
    s.text=str(sal)

#Type of objects
print(type(root), type(child), type(n), type(n.text), type(a.text), type(s.text))

#Create the tree
tree= xml.ElementTree(root)

#Write the data in a file
f=open('first.xml','wb')
tree.write(f)
print(type(tree))

#Read an XML file
tree=xml.ElementTree(file='first.xml')
root=tree.getroot()
Employee=[]

#Type of objects
print(type(tree), type(root), type(Employee))

#Get each child's tag and text data
for e in root.findall('Employee'): #for each employee (child)
    e_data={}
    for v in e: #for each subelement in a child
        e_data[v.tag]=v.text
        print(type(e), type(v),type(v.tag), type(v.text))
    Employee.append(e_data)
print(type(e_data))
print(Employee)

#Modifiying an existing XML data in a file
tree=xml.ElementTree(file='first.xml')
root=tree.getroot()

#Iterate over the data to be modified
for x in root.iter('salary'):
    sal=int(x.text)
    sal=sal*1.05
    x.text=str(sal)

#Iterate over the data to be modified
f=open('first.xml','wb')
tree.write(f)

