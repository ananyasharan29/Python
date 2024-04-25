import xml.dom.minidom as minidom

#Input data
emp=[
    {'name':'AAA',
     'age':22,
     'dept':'IT',
     'salary': 78000
    },
    {'name':'BBB',
     'age':35,
     'dept':'Management',
     'salary':80000
    },
    {'name':'CCC',
     'age':43,
     'dept':'HR',
     'salary': 170000
    }
]

#Create the XML structure
doc=minidom.Document()

print(type(doc), doc)

#Create the root elements
e=doc.createElement('Employees')
doc.appendChild(e)
print(type(e), e)

#Loop through each employee and create the element
for e_d in emp:
    e_ele=doc.createElement('Employee')

    n=doc.createElement('name')
    n_t=doc.createTextNode(e_d['name'])
    n.appendChild(n_t)

    a=doc.createElement('age')
    a_t=doc.createTextNode(str(e_d['age']))
    a.appendChild(a_t)

    d=doc.createElement('dept')
    d_t=doc.createTextNode(e_d['dept'])
    d.appendChild(d_t)

    s=doc.createElement('salary')
    s_t=doc.createTextNode(str(e_d['salary']))
    s.appendChild(s_t)

    e_ele.appendChild(n)
    e_ele.appendChild(a)
    e_ele.appendChild(d)
    e_ele.appendChild(s)

    e.appendChild(e_ele)

print(type(e_d), e_d, type(e_ele), type(n), type(n_t))

#Write the XML data into a file
f=open('dom.xml','w')
f.write(doc.toprettyxml(indent="   "))
f.close()


#This method does not store XML data
f=open('dom1.xml','w')
f.write(str(doc))
f.close()

#Read from a XML file
f='dom.xml'
print(type(f), f)

dom_tree=minidom.parse(f)
print(type(dom_tree), dom_tree)

#Get the root elements
root=dom_tree.documentElement
print(type(root), root)

#get all the employee details
e=root.getElementsByTagName('Employee')
print(type(e), e)

#iterate through evevry employrr
for e1 in e:
    n=e1.getElementsByTagName('name')[0].childNodes[0].data
    a=e1.getElementsByTagName('age')[0].childNodes[0].data
    d=e1.getElementsByTagName('dept')[0].childNodes[0].data
    s=e1.getElementsByTagName('salary')[0].childNodes[0].data
    print(f'Name: {n}, Age: {a}, Department: {d}, Salary: Rs.{s}')

#modify the data - increease the age by 1 and increase the salary by 10%
f=open('dom.xml')
dom_tree=minidom.parse(f)

#Get the root elements
root =dom_tree.documentElement

#Get all employees details
emp=root.getElementsByTagName('Employee')

#Modify the value
for e in emp:
    a=e.getElementsByTagName('age')[0]
    a_v=int(a.childNodes[0].data)
    a_v=a_v+1

    s=e.getElementsByTagName('salary')[0]
    s_v=float(s.childNodes[0].data)
    s_v=s_v*1.1

    a.childNodes[0].data=str(a_v)
    s.childNodes[0].data=str(s_v)

#Write a data in a file
f=open('dom_m.xml','w')
f.write(dom_tree.toxml())
f.close()

print(dom_tree)
