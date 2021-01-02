x,y=map(int,input().split())
n=int(input())
dp=[[0 for i in range(x+1)] for j in range(x+y+1)]
for i in range(n):
    #チケットの枚数、嬉しさ
    t,h=map(int,input().split())
    for j in range(x+y,-1,-1):
        for k in range(x):
            if j+t<=x+y:
                dp[j+t][k+1]=max(dp[j+t][k+1],dp[j][k]+h)
ans=0
for i in range(x+y+1):
    for j in range(x+1):
        ans=max(ans,dp[i][j])
print(ans)