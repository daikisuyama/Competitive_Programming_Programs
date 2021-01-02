n,m=map(int,input().split())
x=list(map(int,input().split()))
x.sort()
z=[[] for i in range(m)]
for i in range(n):
    z[x[i]%m].append(x[i])
ans=len(z[0])//2
if m%2==0:
    ans+=len(z[m//2])//2
from collections import Counter
for i in range(1,-(-m//2)):
    v,w=z[i],z[m-i]
    if len(w)==len(v):
        ans+=len(v)
        continue
    #v<wにする
    if len(w)<len(v):
        v,w=w,v
    ans+=len(v)
    #wで同じ整数の組の数
    c=0
    d=Counter(w)
    for i in d:
        c+=d[i]//2
    ans+=min(c,(len(w)-len(v))//2)
print(ans)