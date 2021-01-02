from math import gcd
from itertools import accumulate
def lcm(x,y):
    return x*y//gcd(x,y)
n=int(input())
a=list(map(int,input().split()))
l=list(accumulate(a,gcd))[:-1]
r=list(accumulate(a[::-1],gcd))[:-1]
#print(l)
#print(r)
g=[]
for i in range(n):
    if i==0:
        g.append(r[-1])
    elif i==n-1:
        g.append(l[-1])
    else:
        g.append(gcd(l[i-1],r[n-2-i]))
#print(g)
ans=g[0]
for i in range(1,n):
    ans=lcm(ans,g[i])
print(ans)
