import xml.etree.ElementTree as xml

courses = [
    {'course_name': 'Python', 'course_instructor': 'Lekha', 'Department': 'MCA', 'Student_no': 50},
    {'course_name': 'Python', 'course_instructor': 'Lekha_1', 'Department': 'Btech', 'Student_no': 40},
    {'course_name': 'Python', 'course_instructor': 'Lekha_2', 'Department': 'BCA', 'Student_no': 60},
    {'course_name': 'Python', 'course_instructor': 'Lekha_3', 'Department': 'Mtech', 'Student_no': 30},
    {'course_name': 'DSA', 'course_instructor': 'Veena s', 'Department': 'MCA', 'Student_no': 50},
    {'course_name': 'DSA', 'course_instructor': 'Veena_1', 'Department': 'Mtech', 'Student_no': 30},
    {'course_name': 'Operating system', 'course_instructor': 'Lekha', 'Department': 'MCA', 'Student_no': 50}
]


root = xml.Element("Courses")
for course in courses:
    course_elem = xml.SubElement(root, "Course")
    for key, value in course.items():
       xml.SubElement(course_elem, key).text = str(value)

tree = xml.ElementTree(root)
tree.write("courses.xml")

tree = xml.parse("courses.xml")
root = tree.getroot()

departments = {}
courses = []
course_students = []

for c in root.findall("Course"):
    d = c.find("Department").text
    c_n = c.find("course_name").text
    s_c = int(c.find("Student_no").text)
    
    if d not in departments:
        departments[d] = 1
    else:
        departments[d] += 1
    
    if c_n not in courses:
        courses.append(c_n)
        course_students.append(s_c)
    else:
        index = courses.index(c_n)
        if s_c < course_students[index]:
            course_students[index] = s_c

max_dept = max(departments, key=departments.get)
print("Department with maximum courses:", max_dept)

min_students = course_students.index(min(course_students))
print("Course with least number of students:", courses[min_students])

min_department = courses.index(min(courses, key=lambda x: departments[x]))
print("Course with least number of departments:", courses[min_department])

