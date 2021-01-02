def alp(z):
    return ord(z)-97
h,w=map(int,input().split())
inf=10**15
a=[list(input()) for i in range(h)]
dp=[[inf]*w for i in range(h)]
check=[False]*26
al=[[] for i in range(26)]
for i in range(h):
    for j in range(w):
        if a[i][j] not in ["S","G","#","."]:
            al[alp(a[i][j])].append([i,j])
from collections import deque
d=deque()
for i in range(h):
    for j in range(w):
        if a[i][j]=="S":
            dp[i][j]=0
            d.append([i,j])
while len(d):
    l=len(d)
    for _ in range(l):
        p=d.popleft()
        for i,j in [[p[0],p[1]-1],[p[0],p[1]+1],[p[0]-1,p[1]],[p[0]+1,p[1]]]:
            if 0<=i<h and 0<=j<w:
                if a[i][j]!="#":
                    if dp[i][j]==inf:
                        dp[i][j]=dp[p[0]][p[1]]+1
                        d.append([i,j])
        if a[p[0]][p[1]] not in ["S","G","#","."]:
            if check[alp(a[p[0]][p[1]])]:
                continue
            check[alp(a[p[0]][p[1]])]=True
            for i,j in al[alp(a[p[0]][p[1]])]:
                if dp[i][j]==inf:
                    dp[i][j]=dp[p[0]][p[1]]+1
                    d.append([i,j])
for i in range(h):
    for j in range(w):
        if a[i][j]=="G":
            if dp[i][j]==inf:
                print(-1)
            else:
                print(dp[i][j])