n=int(input())
a=list(map(int,input().split()))
dp=[[0,0] for i in range(n)]
dp[0][0]=a[0]
dp[1][0]=dp[0][0]+a[1]
dp[1][1]=dp[0][0]-2*a[0]-a[1]
for i in range(2,n):
    dp[i][0]=max(dp[i-1])+a[i]
    dp[i][1]=max(dp[i-1][0]-2*a[i-1]-a[i],dp[i-1][1]+2*a[i-1]-a[i])
print(max(dp[n-1]))