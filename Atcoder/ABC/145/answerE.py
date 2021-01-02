#典型dp
n,t=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]
ab.sort(key=lambda x:x[0])
m=ab[-1][0]
dp=[0]*(t+m)

for i in range(n):
    dp_sub=[0]*(t+m)
    for j in range(t):
        if j==0:
            dp_sub[ab[i][0]]=ab[i][1]
        else:
            if dp[j]!=0:
                dp_sub[j+ab[i][0]]=dp[j]+ab[i][1]
    for j in range(t+m):
        dp[j]=max(dp[j],dp_sub[j])
print(max(dp))
