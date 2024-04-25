# Using Context Manager(With) - it is a kind of replacement of f.close()
# --it's a good idea to close a file after usage as it will free up the resources
# --if we don't close it, garbage collector would close it
# --with keyword closes the file as soon as the usage is over

with open('sample1.txt', 'w') as f:
    f.write('Ananya Sharan')

# f.write('Parul') --it won't work and it'll show error because with keyword automatically closes the file when work is done

with open('sample.txt', 'r') as f:
    print(f.read())

#Moving with the file -> f.read(10) prints 10 char then next f.read(10) prints next 10 char
with open('sample.txt', 'r') as f:
    print(f.read(10), end='')
    print(f.read(10))

#benefit? -> to load a big file in memory
"""big_l = ['Hello World!' for i in range(1000)]
with open('big.txt', 'w') as f:
    f.writelines(big_l)

with open('big.txt', 'r') as f:
    chunk_size = 100

    while len(f.read(chunk_size)) > 0:
        print(f.read(chunk_size), end='')
        f.read(chunk_size) 
"""




