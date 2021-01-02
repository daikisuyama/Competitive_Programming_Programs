n=int(input())
caa,cab,cba,cbb=[input() for i in range(4)]
mod=10**9+7
if n==2:
    print(1)
    exit()
if n==3:
    print(1)
    exit()
ans=1
for i in range(n-3):
    ans*=2
    ans%=mod
if cab=="A":
    if caa=="A":
        print(1)
    else:
        if cba=="B":
            print(ans)
        else:
            dp=[[0,0] for i in range(n-3)]
            dp[0]=[1,1]
            for i in range(n-4):
                dp[i+1][0]=dp[i][0]+dp[i][1]
                dp[i+1][1]=dp[i][0]
                dp[i+1][0]%=mod
                dp[i+1][1]%=mod
            print(sum(dp[n-4])%mod)
else:
    if cbb=="B":
        print(1)
    else:
        if cba=="A":
            print(ans)
        else:
            dp=[[0,0] for i in range(n-3)]
            dp[0]=[1,1]
            for i in range(n-4):
                dp[i+1][0]=dp[i][0]+dp[i][1]
                dp[i+1][1]=dp[i][0]
                dp[i+1][0]%=mod
                dp[i+1][1]%=mod
            print(sum(dp[n-4])%mod)