mod=998244353
n,s=map(int,input().split())
a=list(map(int,input().split()))
dp=[[0]*(s+1) for i in range(n+1)]
dp[0][0]=1
for i in range(n):
    for j in range(s+1):
        if j-a[i]>=0:
            dp[i+1][j]=dp[i][j]*2+dp[i][j-a[i]]
        else:
            dp[i+1][j]=dp[i][j]*2
        dp[i+1][j]%=mod
print(dp[n][s])