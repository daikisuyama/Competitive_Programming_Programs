mod=10**9+7
n,m=map(int,input().split())
#n,m=min(n,m),max(n,m)
dp=[[[0,0] for j in range(2)] for i in range(m)]
dp[0]=[[1,0],[1,0]]
for i in range(m-1):
    for j in range(2):
        for k in range(2):
            if j==0 and k==0:
                dp[i+1][j][1]+=dp[i][j][k]
                dp[i+1][j+1][0]+=dp[i][j][k]
            elif j==1 and k==0:
                dp[i+1][j][1]+=dp[i][j][k]
                dp[i+1][j-1][0]+=dp[i][j][k]
            elif j==0 and k==1:
                dp[i+1][j+1][0]+=dp[i][j][k]
            else:
                dp[i+1][j-1][0]+=dp[i][j][k]
    for j in range(2):
        for k in range(2):
            dp[i+1][j][k]%=mod
ans=-2
for j in range(2):
    for k in range(2):
        ans+=dp[m-1][j][k]
        ans%=mod
dp2=[[[0,0] for j in range(2)] for i in range(n)]
dp2[0]=[[1,0],[1,0]]
for i in range(n-1):
    for j in range(2):
        for k in range(2):
            if j==0 and k==0:
                dp2[i+1][j][1]+=dp2[i][j][k]
                dp2[i+1][j+1][0]+=dp2[i][j][k]
            elif j==1 and k==0:
                dp2[i+1][j][1]+=dp2[i][j][k]
                dp2[i+1][j-1][0]+=dp2[i][j][k]
            elif j==0 and k==1:
                dp2[i+1][j+1][0]+=dp2[i][j][k]
            else:
                dp2[i+1][j-1][0]+=dp2[i][j][k]
    for j in range(2):
        for k in range(2):
            dp2[i+1][j][k]%=mod
for j in range(2):
    for k in range(2):
        ans+=dp2[n-1][j][k]
        ans%=mod
print(ans)