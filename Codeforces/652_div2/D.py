mod=10**9+7
n=2*(10**6)
dp=[[0,0,0] for i in range(n)]
dp[0][0]=1
for i in range(1,n):
    dp[i][0]+=dp[i-1][0]
    dp[i][1]+=dp[i-1][0]
    dp[i][0]+=dp[i-1][1]*2
    dp[i][2]+=dp[i-1][1]
    dp[i][2]+=dp[i-1][2]
    dp[i][0]%=mod
    dp[i][1]%=mod
    dp[i][2]%=mod
ans=[0]*n
for i in range(3):
    #j+3の方に+する
    if i!=0:
        ans[i]+=(mod+dp[i][2]-dp[i-1][2])*4
        ans[i]%=mod
    #range注意
    for j in [k for k in range(n) if k%3==i][:-1]:
        ans[j+3]+=ans[j]
        ans[j+3]+=(mod+dp[j+3][2]-dp[j+2][2])*4
        ans[j+3]%=mod

for _ in range(int(input())):
    print(ans[int(input())-1])