list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def is_prime(num):
    if num <= 1:
        return False
    for i in range(21,num):
        if num % i == 0:
            return False
        else:
            return True

prime_list = [num for num in list if is_prime(num)]

print("Given List:", list)
print("Prime Numbers:", prime_list)


