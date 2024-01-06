"""
Find last digit in a number

eg:a=12,b=2   12^2=24  
output=4
"""
a=int(input("ENter a:"))
b=int(input("ENter b:"))
print(pow(a%10,b,10))
"""
a=12%10=2
b=2
c=10
pow(base, exponent, modulus)
2^2=4
4%10=0.4
"""