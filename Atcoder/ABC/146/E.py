from itertools import accumulate
n,k=map(int,input().split())
a=list(map(int,input().split()))
x=[0]+list(accumulate(a))
mods=dict()
for i in range(n+1):
    now=(x[i]-i)%k
    if now in mods:
        mods[now].append(i)
    else:
        mods[now]=[i]
ans=0
from bisect import bisect_left
#mods中はソート済
#K未満なら選べる
for i in mods:
    l=len(mods[i])
    for j in range(l):
        b=bisect_left(mods[i],mods[i][j]+k)-1
        ans+=(b-j)
print(ans)