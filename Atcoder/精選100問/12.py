#11/26 10:06~10:11
n,m=map(int,input().split())
rel=[[0]*n for i in range(n)]
for i in range(n):
    rel[i][i]=1
for i in range(m):
    x,y=map(int,input().split())
    rel[x-1][y-1]=1
    rel[y-1][x-1]=1
ans=1
for i in range(2**n):
    check=[j for j in range(n) if (i>>j)&1]
    f=True
    for j in check:
        for k in check:
            if not rel[j][k]:
                f=False
    if f:
        ans=max(ans,len(check))
print(ans)