First_name = input("Enter the First name: ")
try:
    if First_name[0].islower():
        raise Exception("First letter should be capital")
    else:
        print(First_name)
except Exception as e:
    print(f'Exception Error: {e}')

try:
    if '.'  in First_name:
        raise Exception("Full stop is not allowed.")
    else:
        print(First_name)
        
except Exception as e:
    print(f'Exception Error: {e}')


gender=input("Enter your Gender :")
try:
    if gender == M or m or f or F or O or O:
        print(gender)

    else:
        raise Exception("Gender should be M,F,O")
except Exception as e:
    print(f'Exception Error: {e}')
    
    
