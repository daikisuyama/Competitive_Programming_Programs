from sys import setrecursionlimit
setrecursionlimit(10**7)
n=int(input())
S=input()
ans=0
for k in range(1,n):
    s,t=S[:k],S[k:]
    dp=[[0]*(len(t)+1) for i in range(len(s)+1)]
    for i in range(len(s)+1):
        for j in range(len(t)+1):
            if i<len(s):
                dp[i+1][j]=max(dp[i+1][j],dp[i][j])
            if j<len(t):
                dp[i][j+1]=max(dp[i][j+1],dp[i][j])
            if i<len(s) and j<len(t):
                dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j]+(s[i]==t[j]))
    ans=max(ans,dp[len(s)][len(t)])
print(n-ans*2)