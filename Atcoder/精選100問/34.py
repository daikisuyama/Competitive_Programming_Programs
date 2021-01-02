#11/28 12:20
n=int(input())
dp=[0]*(n+1)
dp[0],dp[1]=1,1
for i in range(n-1):
    dp[i+2]=dp[i+1]+dp[i]
print(dp[n])