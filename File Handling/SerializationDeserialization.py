# Serialization - process of converting python data types to JSON(JavaScript On Notation) format
# Deserialization - process of converting JSON to python data types
#  It is a kind of universal data format or text format understood by all the programming languages

#serialization using json module
#list
# json.dump - Python object(list/dict) to JSON,it takes which object is going to dump and file handler as a parameter
# json.dumps — Python object to JSON string
# json.load — .json FILE to Python object, it takes file handler as a parameter
# json.loads — JSON string to Python object

import json

# l = [1, 2, 3, 4]
# with open('demo.json', 'w') as f:
#     json.dump(l, f)

#dict
d = {
    'name':'Anamika',
    'age': 27,
    'gender':'Female'
    }
with open('demo.json', 'w') as f:
    json.dump(d, f, indent = 4)

# Deserialized
with open('demo.json', 'r') as f:
    d = json.load(f)
    print(d)
    print(type(d))

# Serialization and Deserialization on tuple
t = (1, 2, 3, 4, 5)
with open('demo1.json', 'w') as f:
    json.dump(t, f) #it will return list

d1 = {
    'student':'Ananya',
    'marks':[89, 90, 95, 93, 98]
}
with open('demo1.json', 'w') as f:
    json.dump(d1, f)

# Serialization and Deserialization on custom object
class Person():
    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

person = Person('Ananya', 'Sharan', 23, 'female')

# with open('demo2.json', 'w') as f:
#     json.dump(person, f)  #TypeError: Object of type Person is not JSON serializable
# We can only serialize python's in-built datatypes but can't serialize user defined class object
# Then we have to specify how to serialize 

# As a String
def show_object(person):
    if isinstance(person, Person):
        return "{} {} age {} and gender {}".format(person.fname,person.lname,person.age,person.gender)
    
with open('demo2.json', 'w') as f:
    json.dump(person, f, default=show_object)

# As a Dict
def show_object(person):
    if isinstance(person, Person):
        return {'name': person.fname +' '+ person.lname,'age':person.age,'gender':person.gender}
with open('demo2.json', 'w') as f:
    json.dump(person, f, default=show_object, indent=4)

# Deserialize
with open('demo2.json', 'r') as f:
    print(json.load(f))