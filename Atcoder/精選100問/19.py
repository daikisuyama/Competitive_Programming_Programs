#11/28 11:51~
d=int(input())
n=int(input())
m=int(input())
ds=[0,d]
for i in range(n-1):
    x=int(input())
    ds.append(x)
    ds.append(x+d)
ds.sort()
k=[int(input()) for i in range(m)]
from bisect import bisect_left
ans=0
for i in range(m):
    y=bisect_left(ds,k[i])
    ans+=min(abs(ds[y]-k[i]),abs(ds[y-1]-k[i]))
print(ans)
