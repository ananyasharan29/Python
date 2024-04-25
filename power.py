def power(n):
    return n, n**2, n**3, n**4, n**5, n**6, n**7, n**8, n**9, n**10
_,_,_,pow4, pow5, *_=power(3)
print("Fourth Power:  ", pow4)
print("Fifth Power:  ", pow5)
*_,pow9,pow10=power(2)
print("Nineth Power:  ", pow9)
print("tenth Power:  ", pow10)
