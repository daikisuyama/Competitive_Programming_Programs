from itertools import groupby
h,w,n,m=map(int,input().split())
#初めの状態
check=[[-1]*w for _ in range(h)]
for i in range(n):
    a,b=map(int,input().split())
    check[a-1][b-1]=1
for i in range(m):
    c,d=map(int,input().split())
    check[c-1][d-1]=0
#最終的な状態
ans=[[0]*w for _ in range(h)]
#まずは行方向で最終的な状態を考える
for i in range(h):
    x=[(key,list(group)) for key,group in groupby(check[i],key=lambda x:x==0)]
    now=0
    for k,g in x:
        if not k and 1 in g:
            for _ in g:
                ans[i][now]=1
                now+=1
        else:
            now+=len(g)
#列方向で最終的な状態を考える
for j in range(w):
    x=[(key,list(group)) for key,group in groupby([check[i][j] for i in range(h)],key=lambda x:x==0)]
    now=0
    for k,g in x:
        if not k and 1 in g:
            for _ in g:
                ans[now][j]=1
                now+=1
        else:
            now+=len(g)
#照らされた数
print(sum(ans[i][j] for j in range(w) for i in range(h)))