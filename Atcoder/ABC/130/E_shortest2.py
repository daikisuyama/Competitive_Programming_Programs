mod=10**9+7
n,m=map(int,input().split())
s=list(map(int,input().split()))
t=list(map(int,input().split()))
dp=[[0]*(m+1) for i in range(n+1)]
for i in range(n+1):
    dp[i][0]=1
for i in range(m+1):
    dp[0][i]=1
for i in range(n):
    for j in range(m):
        if s[i]==t[j]:
            dp[i+1][j+1]=(dp[i+1][j]+dp[i][j+1])%mod
        else:
            dp[i+1][j+1]=(dp[i+1][j]+dp[i][j+1]-dp[i][j])%mod
print(dp[n][m])