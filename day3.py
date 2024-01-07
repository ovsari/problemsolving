"""
	Reverse a number
n = int(input())  # Input example: 1234
rev = 0 

while n >= 0:
    rev = rev * 10 + (n % 10)
    n = n // 10
print(rev)
"""
n = int(input())  # Input example: 1234
rev = str(n)
print(int(rev[::-1]))
