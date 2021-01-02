import math
def combinations_count(n, r):
    if n-r<0:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
mod=998244353
n,s=map(int,input().split())
a=list(map(int,input().split()))
dp=[dict() for i in range(s+1)]
for i in range(n):
    if a[i]<=s:
        if 1 in dp[a[i]]:
            dp[a[i]][1]+=1
        else:
            dp[a[i]][1]=1
for i in range(1,s+1):
    for k in range(i,s+1):
        if k+i<=s:
            if k!=i:
                for j in dp[i]:
                    if j+1 in dp[k+i]:
                        dp[k+i][j+1]+=dp[i][j]
                        dp[k+i][j+1]%=mod
                    else:
                        dp[k+i][j+1]=dp[i][j]
                        dp[k+i][j+1]%=mod
            else:
                for j in dp[i]:
                    if j==1:
                        if j+1 in dp[k+i]:
                            dp[k+i][j+1]+=combinations_count(dp[i][j],2)
                            dp[k+i][j+1]%=mod
                        else:
                            dp[k+i][j+1]=combinations_count(dp[i][j],2)
                            dp[k+i][j+1]%=mod
                    else:
                        if j+1 in dp[k+i]:
                            dp[k+i][j+1]+=dp[i][j]
                            dp[k+i][j+1]%=mod
                        else:
                            dp[k+i][j+1]=dp[i][j]
                            dp[k+i][j+1]%=mod

ans=0
for i in dp[s]:
    ans+=(pow(2,n-i,mod)*dp[s][i])
    ans%=mod
print(ans)