n=int(input())
a=list(map(int,input().split()))
dp=[0]*n
dp[0]=1000
for i in range(1,n):
    dp[i]=dp[i-1]
    for j in range(i):
        dp[i]=max(dp[i],(dp[j]//a[j])*a[i]+dp[j]%a[j])
print(dp[n-1])