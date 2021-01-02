#わかんねー辛いーー

from math import log2
from math import ceil
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=30
xa=[0]*l
xb=[0]*l
for i in range(n):
    k=a[i]
    for j in range(l):
        if (k>>j)&1:
            xa[j]+=1
for i in range(n):
    k=b[i]
    for j in range(l):
        if (k>>j)&1:
            xb[j]+=1
ans=[[0,0] for i in range(l+1)]
for i in range(l):
    ans[i][0]+=((n-xa[i])*xb[i]+(n-xb[i])*xa[i])
    ans[i+1][1]+=(xa[i]*xb[i])
for i in range(l):
    ans[i][0]+=ans[i][1]
    ans[i+1][1]+=ans
print(ans)
_ans=0
for i in range(l):
    _ans+=(ans[i]%2)*(2**i)
print(_ans)


