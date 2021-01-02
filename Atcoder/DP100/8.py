s=input()
n=len(s)
dp=[[0,0] for i in range(n)]
dp[0][0]=1
for i in range(1,n):
    dp[i][0]=dp[i-1][1]+1
    if s[i-1]!=s[i]:
        dp[i][0]=max(dp[i][0],dp[i-1][0]+1)
    if i>1:
        dp[i][1]=dp[i-2][0]+1
        if i>2:
            if s[i-3:i-1]!=s[i-1:i+1]:
                dp[i][1]=max(dp[i][1],dp[i-2][1]+1)
print(max(dp[n-1]))