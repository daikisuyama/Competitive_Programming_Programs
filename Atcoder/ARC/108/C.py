n,m=map(int,input().split())
check=[-1]*n
tree=[[] for i in range(n)]
for i in range(m):
    u,v,c=map(int,input().split())
    tree[u-1].append([v-1,c-1])
    tree[v-1].append([u-1,c-1])
from collections import deque
check[0]=0
d=deque([0])
while len(d):
    l=len(d)
    for i in range(l):
        p=d.popleft()
        for j in tree[p]:
            if check[j[0]]==-1:
                if check[p]==j[1]:
                    if j[1]==0:
                        check[j[0]]=1
                    else:
                        check[j[0]]=j[1]-1
                else:
                    check[j[0]]=j[1]
                d.append(j[0])
for i in range(n):
    print(check[i]+1)