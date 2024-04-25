class Course:
    def __init__(self, name):
        self.name = name

class Professors:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def Add_course(self, course):
        self.courses.append(course)

class Department:
    def __init__(self, name):
        self.name = name
        self.professors = []

    def Add_professor(self, professor):
        self.professors.append(professor)

class University:
    def __init__(self, name):
        self.name = name
        self.department = []

    def Add_department(self, department):
        self.department.append(department)

c1 = Course("PP")
c2 = Course("DSA")
c3 = Course("Computer Networks")
c4 = Course("Operating System")
c5 = Course("DBMS")
c6 = Course("ML & AI")

p1 = Professors("Ananya")
p2 = Professors("Govind")
p3 = Professors("Anukamal")
p4 = Professors("Vidit")
p5 = Professors("Shubha")
p6 = Professors("Suhas")
        
d1 = Department("MCA")
d2 = Department("CSE")
d3 = Department("IT")
d4 = Department("ME")

u = University("PESU")

print(p1.Add_course(c1))
p1.Add_course(c2)
p2.Add_course(c3)
p2.Add_course(c2)
p3.Add_course(c5)
p3.Add_course(c4)
p4.Add_course(c6)
p4.Add_course(c3)
p5.Add_course(c4)
p6.Add_course(c5)


d1.Add_professor(p5)
d2.Add_professor(p3)
d3.Add_professor(p1)
d4.Add_professor(p2)
d1.Add_professor(p4)

u.Add_department(d1)
u.Add_department(d2)
u.Add_department(d3)
u.Add_department(d4)

print(u.name)

#name of all professors in each deoartment

for d in u.department:
    print(f"Professor in {d.name}")
    for p in d.professors:
        print(p.name)

print("\n")        
#all courses taught by each professors

for d in u.department:
    for p in d.professors:
        print(f"Course taught by {p.name}")
        for c in p.courses:
            print(c.name)















    
