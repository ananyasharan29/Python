"""
"Pickling" is the process whereby a Python object hierarchy is converted into a byt stream,
and "Unpickling" is the inverse operation, whereby a byte stream(from a binary file or bytes-like object)
is converted back into an object hierarchy.
"""
import pickle
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print('Hi my name is ',self.name,' and I am ', self.age,' years old.')

person = Person('Ananya Sharan', 23)

# pickle dump
with open('person.pkl', 'wb') as f:
    pickle.dump(person, f)

#pickle load
with open('person.pkl', 'rb') as f:
    person = pickle.load(f)

person.display_info()

# Pickle VS json
"""
Pickle lets the user to store data in binary format and
JSON lets the user to store data in human readable text format
"""