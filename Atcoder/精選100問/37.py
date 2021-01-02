#11/28 12:29~
n,m=map(int,input().split())
c=list(map(int,input().split()))
dp=[10**15]*(n+1)
dp[0]=0
for i in range(m):
    for j in range(n):
        if j+c[i]>n:continue
        dp[j+c[i]]=min(dp[j+c[i]],dp[j]+1)
print(dp[n])
