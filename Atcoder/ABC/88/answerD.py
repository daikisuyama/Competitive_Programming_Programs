import sys
#大きすぎるとダメ
h,w=map(int,input().split())
sys.setrecursionlimit(h*w+10)
s=[list(input()) for i in range(h)]
inf=1000000000000000
d=[[inf]*w for i in range(h)]


def dfs(i,j):
    global h,w,s
    nex=[(0,-1),(0,1),(-1,0),(1,0)]
    for k in range(4):
        l,m=i+nex[k][0],j+nex[k][1]
        if 0<=i+nex[k][0]<h and 0<=j+nex[k][1]<w:
            if s[l][m]=="." and d[l][m]>d[i][j]+1:
                d[l][m]=d[i][j]+1
                dfs(l,m)

d[0][0]=0
dfs(0,0)
ans=0
for i in range(h):
    for j in range(w):
        if s[i][j]==".":
            ans+=1
if d[h-1][w-1]==inf:
    print(-1)
else:
    print(ans-d[h-1][w-1]-1)