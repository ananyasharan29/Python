#Custom Exception
class InvalidValueException(Exception):
    '''raise when vale is less than 100'''
    pass

try:
    n= int(input("Enter the value : "))
    if n > 100:
        raise InvalidValueException
    else:
        print(n)
except InvalidValueException as e:
    print(f"InvalidValueException: {e}")


#Custom Exception with error description
class SalarynotinRange(Exception):
    '''rasised when salary is not in between 30000 and 50000 attributes:
    salery - input for raising exception
    msg - description of the exception'''

    def __init__(self,salary,msg='Salary not in range between (30000,5000)'):
                 self.salary=salary
                 self.msg=msg
                 super().__init__(self.msg)


amt=int(input("Enter the salary : "))
if not 30000 < amt < 50000:
                 raise SalarynotinRange(amt)

else:
    print(f'salary is Rs.{amt}')


class SalarynotinRange(Exception):
    '''rasised when salary is not in between 30000 and 50000 attributes:
    salery - input for raising exception
    msg - description of the exception'''

    def __init__(self,salary,msg='Salary not in range between (30000,5000)'):
                 self.salary=salary
                 self.msg=msg
                 super().__init__(self.msg)

try:
    amt=int(input("Enter the salary : "))
    if not 30000 < amt < 50000:
        raise SalarynotinRange(amt)

    else:
        print(f'salary is Rs.{amt}')
except:
    print(f'SalarynotinRange:{e}')

#raise bulid-in Exception explicitly


x=int(input("Enter the 1st number: "))
y=int(input("Enter 2nd number: "))

try:
    z=x/y
    if z>10:
        raise valueError(z)
    else:
        print(z)
except valueError:
    print(f'valueError:invalid Range')
    
