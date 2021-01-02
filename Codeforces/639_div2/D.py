from sys import setrecursionlimit
setrecursionlimit(10**7)
n,m=map(int,input().split())
s=[input() for i in range(n)]
bfs_chk=[[s[i][j]=="." for j in range(m)] for i in range(n)]

from collections import deque
d=deque()
def bfs():
    global d,bfs_chk
    while len(d):
        l=len(d)
        for i in range(l):
            c=d.popleft()
            nex=[[c[0]-1,c[1]],[c[0]+1,c[1]],[c[0],c[1]+1],[c[0],c[1]-1]]
            for j in nex:
                if j[0]<n and j[1]<m:
                    if not bfs_chk[j[0]][j[1]]:
                        bfs_chk[j[0]][j[1]]=True
                        d.append(j)

ans=0
for i in range(n):
    for j in range(m):
        if bfs_chk[i][j]==False:
            bfs_chk[i][j]=True
            d.append([i,j])
            bfs()
            ans+=1

#黒くなってしまう場合(それぞれの行と列に存在する場合)
#連続してない場合(全体覆ってないのもだめ)
#全体覆ってなくてもいいかんじに配置すればいけるか
from itertools import groupby
r=[False]*n
c=[False]*m
for i in range(n):
    g=list(groupby(s[i]))
    if len(g)>3:
        print(-1)
        exit()
    if len(g)==3 and g[0][0]=="#":
        print(-1)
        exit()
    for j in range(m):
        if s[i][j]=="#":
            c[j]=True
t=[list(x) for x in zip(*s)]
for i in range(m):
    g=list(groupby(t[i]))
    if len(g)>3:
        print(-1)
        exit()
    if len(g)==3 and g[0][0]=="#":
        print(-1)
        exit()
    for j in range(n):
        if t[i][j]=="#":
            r[j]=True

if (all(r) and all(c)) or ((not any(r)) and (not any(c))):
    print(ans)
else:
    print(-1)
