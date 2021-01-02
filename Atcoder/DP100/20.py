n,t,s=map(int,input().split())
dp=[0]*(t+1)
for i in range(n):
    a,b=map(int,input().split())
    for j in range(t,s-1,-1):
        if j+b<=t:
            if j==s or dp[j]!=0:
                dp[j+b]=max(dp[j+b],dp[j]+a)
    for j in range(s,-1,-1):
        if j+b<=s:
            if j==0 or dp[j]!=0:
                dp[j+b]=max(dp[j+b],dp[j]+a)
        else:
            if s+b<=t:
                dp[s+b]=max(dp[s+b],dp[j]+a)
#print(dp)
print(max(dp))
