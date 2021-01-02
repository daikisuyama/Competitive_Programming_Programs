from math import sqrt
a,b=input().split()
k=int(a+b)
if int(sqrt(k))**2==k:
    print("Yes")
else:
    print("No")