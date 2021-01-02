import sys
sys.setrecursionlimit(10**6)
from collections import deque
n,m=map(int,input().split())
path=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    path[a-1].append(b-1)
    path[b-1].append(a-1)
nan=deque([0])
check=[1 if i==0 else -1 for i in range(n)]
def bfs():
    global n,m,path,nan
    l=len(nan)
    if not l:
        return
    for _ in range(l):
        x=nan.popleft()
        for j in path[x]:
            if check[j]==-1:
                check[j]=x
                nan.append(j)
    bfs()
bfs()
if any([i==-1 for i in check]):
    print("No")
else:
    print("Yes")
    for i in range(1,n):
        print(check[i]+1)