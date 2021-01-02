n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
#それぞれの要素の位置
ind=[0 for i in range(n)]
for i in range(n):
    ind[a[i]-1]+=i
for i in range(n):
    ind[b[i]-1]-=i
for i in range(n):
    if ind[i]<0:
        ind[i]+=n
from collections import Counter
c=Counter(ind)
ans=1
for i in c:
    ans=max(ans,c[i])
print(ans)
