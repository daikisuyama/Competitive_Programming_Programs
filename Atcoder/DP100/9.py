command=[i+j for i in "ABXY" for j in "ABXY"]
#print(command)
n=int(input())
s=input()
inf=100000000000
ans=inf
for i in range(16):
    l=command[i]
    for j in range(16):
        r=command[j]
        dp=[inf]*n
        dp[0]=1
        if n>1:
            if s[0:2]==l or s[0:2]==r:
                dp[1]=1
        for k in range(n):
            if k+1<n:
                dp[k+1]=min(dp[k+1],dp[k]+1)
            if k+2<n:
                if s[k+1:k+3]==l or s[k+1:k+3]==r:
                    dp[k+2]=min(dp[k+2],dp[k]+1)
        #print(dp[n-1])
        ans=min(ans,dp[n-1])
print(ans)