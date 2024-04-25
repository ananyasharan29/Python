#import statements
from bs4 import BeautifulSoup as bs
from lxml import etree

#create a list of dictionaries
students=[
    {'name':'AAA',
     'sem':1,
     'sec':'A',
     'marks': 78
     },
     {'name':'BBB',
     'sem':1,
     'sec':'C',
     'marks': 95
     },
     {'name':'CCC',
     'sem':1,
     'sec':'B',
     'marks': 86
     }
]

#Create an xml structure
root = etree.Element('students')
print(type(root))
print(root)

#loop through each dictionary to create XML elements
for s in students:
    st=etree.SubElement(root, 'Student')

    n = etree.SubElement(st, 'name')
    n.text=str(s['name'])

    se = etree.SubElement(st, 'sem')
    se.text=str(s['sem'])

    sec = etree.SubElement(st, 'sec')
    sec.text=s['sec']

    m = etree.SubElement(st, 'marks')
    m.text=str(s['marks'])

print(type(m))
print(type(n))
print(type(se))
print(type(sec))

#create a string representation of the XML
x_s=etree.tostring(root, pretty_print=True, encoding='utf-8', xml_declaration=True)
print(type(x_s))

x_s1=etree.tostring(root, pretty_print=False, encoding='utf-8', xml_declaration=True)
print(x_s1)

x_s2=etree.tostring(root, pretty_print=True, encoding='utf-8', xml_declaration=False)
print(x_s2)

#Parse the string with BeautifulSoup for formatting
soup=bs(x_s, 'xml')
print(type(soup))
print(soup)

#write the xml data into a file
f=open('soup.xml','w')
f.write(str(soup))
f.close

#Read from a XML file
#Read the file
f=open('soup.xml')
content=f.read()
print(type(content))
print(content)

#Parse the content using BeautifulSoup
soup=bs(content,'xml')
print(type(soup))
print(soup)

#Get all students data 
st=soup.find_all('Student')
print(type(st), st)

#Extract information tag wise for each students
for s in st:
    name=s.find('name').get_text()
    sem=s.find('sem').get_text()
    sec=s.find('sec').get_text()
    marks=s.find('marks').get_text()

    print(f'Name: {name}, Semester: {sem}, Section: {sec}, Marks: {marks}')

#Modify a few elements
#Increment the semester by 1 and decrement marks by 10
#Read XML file
f=open('soup.xml')
content=f.read()

#parse the content with Beautyful Soup
soup = bs(content, 'xml')
#find All student details
st=soup.find_all('Student')

#Iterate over each student and modify the sem and marks
for s in st:
    sem=int(s.find('sem').get_text())
    m=int(s.find('marks').get_text())

    sem+=1
    m-=10

    s.find('sem').string=str(sem)
    s.find('marks').string=str(m)

#Write a modified data into a file
f=open('soup_m.xml', 'w')
f.write(str(soup))
f.close()
