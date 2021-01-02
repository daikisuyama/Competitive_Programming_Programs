n,k=map(int,input().split())
r=list(map(int,input().split()))
check=[0]*n
for i in range(k):
    x,y=map(int,input().split())
    x-=1
    y-=1
    if r[x]>r[y]:
        check[x]+=1
    if r[y]>r[x]:
        check[y]+=1
from bisect import bisect_left
ans=[0]*n
p=sorted(r)
for i in range(n):
    b=bisect_left(p,r[i])
    ans[i]=str(b-check[i])
print(" ".join(ans))