a,b,c=map(int,input().split())
dp=[[[0]*101 for i in range(101)] for j in range(101)]
dp[a][b][c]=1
for i in range(101):
    for j in range(101):
        for k in range(101):
            if i==100 or j==100 or k==100:
                continue
            if i+j+k==0:
                continue
            dp[i+1][j][k]+=(i/(i+j+k))*dp[i][j][k]
            dp[i][j+1][k]+=(j/(i+j+k))*dp[i][j][k]
            dp[i][j][k+1]+=(k/(i+j+k))*dp[i][j][k]
ans=0
for i in range(101):
    for j in range(101):
        for k in range(101):
            if i==100 or j==100 or k==100:
                ans+=dp[i][j][k]*(i-a+j-b+k-c)
print(ans)