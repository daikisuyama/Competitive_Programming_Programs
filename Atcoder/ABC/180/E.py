n=int(input())
tos=[list(map(int,input().split())) for i in range(n)]
#1からjでのコスト
def co(i,j):
    return abs(i[0]-j[0])+abs(i[1]-j[1])+max(0,j[2]-i[2])
inf=10**12
dp=[[inf for j in range(n)] for i in range(1<<n)]
dp[1][0]=0
for i in range(1,1<<n):
    for j in range(n):
        #自身には戻らぬ
        for k in range(n):
            if j==k:continue
            dp[i|(1<<k)][k]=min(dp[i|(1<<k)][k],dp[i][j]+co(tos[j],tos[k]))
ans=inf
for i in range(n):
    ans=min(ans,dp[(1<<n)-1][i]+co(tos[i],tos[0]))
print(ans)