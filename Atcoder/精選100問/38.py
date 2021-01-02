#11/28 13:05~
q=int(input())
for _ in range(q):
    x,y=input(),input()
    n,m=len(x),len(y)
    dp=[[0]*(m+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            #i,j同じ時は+する
            if x[i-1]==y[j-1]:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]+1)
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    print(dp[n][m])