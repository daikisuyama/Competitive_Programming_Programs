h,n=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]
ab.sort(reverse=True)
inf=1000000000
ma=ab[0][0]
dp=[inf]*(h+1+ma)
dp[0]=0
for i in range(n):
    x=ab[i]
    for j in range(h):
        if dp[j]!=inf:
            if j+x[0]<=h+ma:
                if j+x[0]>=h:
                    dp[h]=min(dp[h],dp[j]+x[1])
                else:
                    dp[j+x[0]]=min(dp[j+x[0]],dp[j]+x[1])
            else:
                break
print(dp[h])
