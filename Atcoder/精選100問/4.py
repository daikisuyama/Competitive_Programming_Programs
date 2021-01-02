#11/25 8:22~8:27
n,m=map(int,input().split())
a=[list(map(int,input().split())) for i in range(n)]
#選び方全探索(前計算すればO(n^2)になるかも)
ans=0
for i in range(m):
    for j in range(i+1,m):
        s=0
        for k in range(n):
            s+=max(a[k][i],a[k][j])
        ans=max(ans,s)
print(ans)