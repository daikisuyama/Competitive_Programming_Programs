inf=1000000000000000000000000
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    #絶対値
    dp=[[[-inf,inf] for j in range(5)] for i in range(n)]
    dp[0][0]=[a[0],a[0]]
    for i in range(n-1):
        dp[i+1][0]=[a[i+1],a[i+1]]
        for j in range(5):
            dp[i+1][j][0]=max(dp[i][j][0],dp[i+1][j][0])
            dp[i+1][j][1]=min(dp[i][j][1],dp[i+1][j][1])
        for j in range(4):
            if dp[i][j][0]!=-inf:
                dp[i+1][j+1][0]=max(dp[i+1][j+1][0],dp[i][j][0]*a[i+1])
                dp[i+1][j+1][1]=min(dp[i+1][j+1][1],dp[i][j][0]*a[i+1])
            if dp[i][j][1]!=inf:
                dp[i+1][j+1][0]=max(dp[i+1][j+1][0],dp[i][j][1]*a[i+1])
                dp[i+1][j+1][1]=min(dp[i+1][j+1][1],dp[i][j][1]*a[i+1])
    print(dp[n-1][4][0])