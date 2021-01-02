t=int(input())
from math import gcd
for _ in range(t):
    m,d,w=map(int,input().split())
    z=min(d,m)
    d-=1
    if d%w==0:
        print(z*(z-1)//2)
        continue
    w//=gcd(d,w)
    z-=1
    x=z//w
    y=z%w+1
    print(x*(x-1)//2*(w-y)+(x+1)*x//2*y)