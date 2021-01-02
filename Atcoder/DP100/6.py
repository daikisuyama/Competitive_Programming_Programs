h,n=map(int,input().split())
inf=100000000000
dp=[inf]*(h+1)
dp[h]=0
for i in range(n):
    a,b=map(int,input().split())
    for j in range(h,-1,-1):
        dp[max(j-a,0)]=min(dp[max(j-a,0)],dp[j]+b)
print(dp[0])