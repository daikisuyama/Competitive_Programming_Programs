from math import *
n=int(input())
l=floor(sqrt(n))+1
ans=[0]*n
def f(a,b,c):
    return a*a+b*b+c*c+a*b+b*c+c*a
for x in range(1,l+1):
    for y in range(1,l+1):
        for z in range(1,l+1):
            g=f(x,y,z)
            if g<=n:
                ans[g-1]+=1
for i in range(n):
    print(ans[i])