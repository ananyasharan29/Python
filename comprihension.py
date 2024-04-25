m = [[i for i in range(5)] for _ in range(5)]
print(m)

l = [1, 2 ,3, 4, 5, 6, 7, 8, 9, 10]
mat =[l[i * 5: (i +1) * 5 ]for i in range(2)]
print(mat)


n = int(input("Enter the number of rows : "))
m = int(input("Enter the number of columns : "))

matrix = [l[i * m: (i + 1) * m] for i in range(n)]
print(matrix)

l = [123, 234, 456, 789, 890]
d = {int(d) for n in l for d in str(n)}
print(d)

sq = {i: i**2 for i in range(1,11)}
print(sq)

sqrt = {i: i**2 if i%2 == 0 else i**3 for i in range(1,11)}
print(sqrt)


