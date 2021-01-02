n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
tod=[[] for i in range(k)]
for i in range(n):
    tod[i%k].append(a[i])
from itertools import accumulate
for i in range(k):
    tod[i]=list(accumulate(tod[i]))
ans=[]
now=0
for i in range(n):
    now+=tod[i%k][i//k]
    ans.append(now)
print(" ".join(map(str,ans)))