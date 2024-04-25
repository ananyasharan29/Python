list = ["Ananya", "anu", "govind", "shubha", "vidit"]

new_list = [x for x in list if 'a' in x[0] or 'A' in x[0]]
print(new_list)

new_list2 = [i for i in list if len(i)%2 == 0]
print(new_list2)

new_list3 = [x[len(x) // 2] for x in list]
print(new_list3)
