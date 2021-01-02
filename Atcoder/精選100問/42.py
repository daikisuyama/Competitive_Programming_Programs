#14:55~
n,m=map(int,input().split())
d=[int(input()) for i in range(n)]
c=[int(input()) for i in range(m)]
inf=10**20
dp=[inf]*(n+1)
dp[0]=0
for i in range(m):
    for j in range(n-1,-1,-1):
        dp[j+1]=min(dp[j+1],dp[j]+d[j]*c[i])
print(dp[n])