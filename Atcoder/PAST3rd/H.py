n,l=map(int,input().split())
x=[0]*(l+1)
y=list(map(int,input().split()))
for i in range(n):
    x[y[i]-1]=1
t1,t2,t3=map(int,input().split())
inf=100000000000000
dp=[inf]*(l+1)
dp[0]=0
for i in range(l):
    if x[i+1]:
        dp[i+1]=min(dp[i]+t1+t3,dp[i+1])
    else:
        dp[i+1]=min(dp[i]+t1,dp[i+1])
    if i+2>l:
        dp[l]=min(dp[i]+t1//2+t2//2+t3,dp[l])
    else:
        if x[i+2]:
            dp[i+2]=min(dp[i]+t1+t2+t3,dp[i+2])
        else:
            dp[i+2]=min(dp[i]+t1+t2,dp[i+2])
    if i+4>l:
        dp[l]=min(dp[i]+t1//2+(l-i)*t2-t2//2+t3,dp[l])
    else:
        if x[i+4]:
            dp[i+4]=min(dp[i]+t1+3*t2+t3,dp[i+4])
        else:
            dp[i+4]=min(dp[i]+t1+3*t2,dp[i+4])
print(dp[l])
print(dp)
print(x)


