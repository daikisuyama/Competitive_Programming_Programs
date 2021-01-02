import math
n=int(input())
r=sorted([int(input()) for i in range(n)],reverse=True)

d=0
for i in range(n):
    if i%2==0:
        d+=r[i]*r[i]
    else:
        d-=r[i]*r[i]
print(d*math.pi)
