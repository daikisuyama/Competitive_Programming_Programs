import math
n=int(input())
if n%2==1 or n<10:
    print(0)
else:
    n=n//2
    k=math.floor(math.log(n,5))
    c=0
    for i in range(1,k+1):
        c+=n//(5**i)
    print(c)
