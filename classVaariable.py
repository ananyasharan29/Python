class Student:
    college_name = 'PESU'
    def __init__(self, name, age, sem):
        self.name = name
        self.age = age
        self.sem = sem

s1 = Student('ABC', 22, 1)
print(s1)
