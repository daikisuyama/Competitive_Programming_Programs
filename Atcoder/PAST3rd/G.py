from sys import exit,setrecursionlimit
from collections import deque
setrecursionlimit(10**6)
n,x,y=map(int,input().split())
check=[[False]*2001 for i in range(2001)]
check[0+1000][0+1000]=True
for i in range(n):
    x_,y_=map(int,input().split())
    check[x_+1000][y_+1000]=True
cand=deque()
cand.append((1000,1000))
def bfs(d):
    global check,x,y,cand
    if d>10**4:
        print(-1)
        exit()
    l=len(cand)
    ij_=[[1,1],[0,1],[-1,1],[1,0],[-1,0],[0,-1]]
    for _ in range(l):
        i,j=cand.popleft()
        #print(i,j)
        for k in range(6):
            ij=ij_[k]
            if 0<=i+ij[0]<=2000 and 0<=j+ij[1]<=2000:
                if check[i+ij[0]][j+ij[1]]==False:
                    check[i+ij[0]][j+ij[1]]=True
                    if i+ij[0]==x+1000 and j+ij[1]==y+1000:
                        print(d+1)
                        exit()
                    else:
                        cand.append((i+ij[0],j+ij[1]))
    bfs(d+1)
bfs(0)