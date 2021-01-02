h,n=map(int,input().split())
a,b=[],[]
for i in range(n):
    a_sub,b_sub=map(int,input().split())
    a.append(a_sub)
    b.append(b_sub)
inf=10000000000000
ma=max(a)
dp=[inf]*(h+1+ma)
dp[0]=0
for i in range(n):
    x=[a[i],b[i]]
    for j in range(h):
        if dp[j]!=inf:
            if j+x[0]<=h+ma:
                dp[j+x[0]]=min(dp[j+x[0]],dp[j]+x[1])
            else:
                break
print(min(dp[h:]))
