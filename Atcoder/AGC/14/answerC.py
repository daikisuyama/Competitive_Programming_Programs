h,w,k=map(int,input().split())
s=[-1,-1]
a=[]
for i in range(h):
    x=list(input())
    for j in range(w):
        if x[j]=="S":
            x[j]="."
            s=[i,j]
    a.append(x)
inf=10**15
#移動回数,最小の開く回数
check=[[inf for i in range(w)] for i in range(h)]
from collections import deque
d=deque([s])
check[s[0]][s[1]]=0
for j in range(k):
    l=len(d)
    for i in range(l):
        nowx,nowy=d.popleft()
        for nexx,nexy, in [[nowx-1,nowy],[nowx+1,nowy],[nowx,nowy-1],[nowx,nowy+1]]:
            if 0<=nexx<h and 0<=nexy<w:
                if a[nexx][nexy]==".":
                    if check[nexx][nexy]>check[nowx][nowy]+1:
                        check[nexx][nexy]=check[nowx][nowy]+1
                        d.append([nexx,nexy])
ans=inf
for i in range(h):
    for j in range(w):
        if check[i][j]!=inf:
            ans_sub=-(-min(i,h-1-i,j,w-1-j)//k)+1
            ans=min(ans,ans_sub)
print(ans)