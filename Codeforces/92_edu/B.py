t=int(input())
inf=10000000000000000
for _ in range(t):
    n,k,z=map(int,input().split())
    a=list(map(int,input().split()))
    dp=[[[0,0] for i in range(z+1)] for i in range(n)]
    dp[0][0][0]=a[0]
    for i in range(1,n):
        dp[i][0][0]=dp[i-1][0][0]+a[i]
    for i in range(1,z+1):
        for j in range(1,n):
            dp[j-1][i][1]=max(dp[j-1][i][1],dp[j][i-1][0]+a[j-1])
        for j in range(1,n):
            dp[j][i][0]=max(dp[j-1][i][0]+a[j],dp[j-1][i][1]+a[j])
    ans=0
    for i in range(z+1):
        if k-2*i>=0:
            ans=max(ans,dp[k-2*i][i][0])
            ans=max(ans,dp[k-2*i][i][1])
    print(ans)