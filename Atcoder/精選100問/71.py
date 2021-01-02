#11/29 11:36~
#道路をmodに直す
mod=10**9+7
n,q=map(int,input().split())
a=list(map(int,input().split()))
c=[0]+[i-1 for i in list(map(int,input().split()))]+[0]
b=[]
for i in range(n-1):
    b.append(pow(a[i],a[i+1],mod))
from itertools import accumulate
d=[i for i in list(accumulate(b))]
ans=0
for i in range(q+1):
    x,y=sorted([c[i],c[i+1]])
    #absの操作で余りズレた
    ans+=(0 if y==0 else d[y-1])-(0 if x==0 else d[x-1])
    ans%=mod
print(ans)