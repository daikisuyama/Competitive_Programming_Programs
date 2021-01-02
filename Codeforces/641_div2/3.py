#×、複数回あるので
from itertools import groupby
t=int(input())
ans=[False]*t
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    g=[(key,len(list(group))) for key,group in groupby(a)]
    if len(g)==1:
        ans[i]=(g[0][0]==k)
    elif g[0][0]==k and g[-1][0]==k:
        y=g[0][1]
        z=g[-1][1]
        x=n-y-z
        ans[i]=(any([a[i]==k for i in range((x+y)//2,y+(x+z)//2+1)]))
    elif g[0][0]==k:
        y=g[0][1]
        z=0
        x=n-y-z
        ans[i]=(any([a[i]==k for i in range((x+y)//2,y+(x+z)//2+1)]))
    elif g[-1][0]==k:
        y=0
        z=g[-1][1]
        x=n-y-z
        ans[i]=(any([a[i]==k for i in range((x+y)//2,y+(x+z)//2+1)]))
    else:
        y=0
        z=0
        x=n-y-z
        ans[i]=(any([a[i]==k for i in range((x+y)//2,y+(x+z)//2+1)]))
for i in range(t):
    print("yes" if ans[i] else "no")

