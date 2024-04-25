names = {'Alice':25, 'Bob':12, 'Catherine':90, 'Dore':34}

x = {names:('Adult' if age >18 else 'Child') for names, age in names.items()}
print(x)

c = {key: 'Adult' if value > 18 else 'Child' for key, value in names.items()}
print(c)

            
