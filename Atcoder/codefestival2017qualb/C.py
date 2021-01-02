n,m=map(int,input().split())
G=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
from collections import deque
check=[-1]*n
check[0]=0
d=deque([0])
while len(d):
    l=len(d)
    for _ in range(l):
        p=d.popleft()
        for i in G[p]:
            if check[i]==-1:
                check[i]=1-check[p]
                d.append(i)
            else:
                if check[i]!=check[p]:
                    pass
                else:
                    print(n*(n-1)//2-m)
                    exit()
print(check.count(0)*check.count(1)-m)