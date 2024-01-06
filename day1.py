"""Count digits in a number:
eg N=12
output 2
N=23
output 0
"""

N=int(input())
s=str(N)
count=0
for i in s:
	if i=='0':
		continue
	elif N%int(i)==0:
		count+=1
print(count)
"""
N=12
s="12"
for 1 in 12:
	12%1==0(true)
	count=1
for 2 in 12:
	12%2==0(true)
	count=2

N=23
s="23"
for 2 in 23:
	23%3==0(False)
	count=0
for 2 in 12:
	23%3==0(False)
	count=0

"""
