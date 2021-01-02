mod=10**9+7
s=input()[::-1]
l=len(s)
dp=[[0]*13 for i in range(l+1)]
dp[0][0]=1
#累乗が大きすぎるので前計算
p=[0]*l
p[0]=1
for i in range(l-1):
    p[i+1]=(p[i]*10)%13
for i in range(l):
    s_sub=s[i]
    if s_sub=="?":
        for j in range(13):
            for k in range(10):
                dp[i+1][(j+k*p[i])%13]+=dp[i][j]
                dp[i+1][(j+k*p[i])%13]%=mod
    else:
        k=int(s_sub)
        for j in range(13):
            dp[i+1][(j+k*p[i])%13]+=dp[i][j]
            dp[i+1][(j+k*p[i])%13]%=mod
print(dp[l][5])