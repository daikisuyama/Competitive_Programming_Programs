n=int(input())
tree=[[] for i in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
#は？違うことをしていた
d=dict()
for i in range(n):
    if len(tree[i])==1:
        x=tree[i][0]
        if x in d:
            d[x]+=1
        else:
            d[x]=1
        st=i
ma=n-1
for i in d:
    ma-=(d[i]-1)

#最小の方
inf=10000000000000000
dep=[inf for i in range(n)]
dep[st]=0
from collections import deque
d=deque()
d.append(st)
dep_sub=0
while len(d):
    dep_sub+=1
    l=len(d)
    for _ in range(l):
        p=d.popleft()
        for i in tree[p]:
            if dep[i]==inf:
                dep[i]=dep_sub
                d.append(i)
if any(dep[i]%2 and len(tree[i])==1 for i in range(n)):
    mi=3
else:
    mi=1
print(mi,ma)