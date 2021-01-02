import math
n=100000
l1=math.floor(math.log(n,6))
l2=math.floor(math.log(n,9))
dp=[i for i in range(n+1)]
for i in range(1,l1+1):
    for j in range(n):
        if j+6**i<n+1:
            dp[j+6**i]=min(dp[j]+1,dp[j+6**i])
for i in range(1,l1+1):
    for j in range(n):
        if j+9**i<n+1:
            dp[j+9**i]=min(dp[j]+1,dp[j+9**i])
print(dp[-1])