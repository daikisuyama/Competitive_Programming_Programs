#k以上だから引けば0以上か
#部分列DPテーブル
mod=10**9+7
n,k=map(int,input().split())
a=[i-k for i in list(map(int,input().split()))]
dp=[[0]*20001 for i in range(n)]
dp[0][a[0]+10000]=1
for i in range(1,n):
    for j in range(20001):
        dp[i][j]=dp[i-1][j]
    dp[i][a[i]+10000]+=1
    for j in range(20001):
        dp[i][j]%=mod
        if 0<=j+a[i]<=20000:
            dp[i][j+a[i]]+=dp[i-1][j]
#和(マイナスインデックスも)
print(sum(dp[-1][10000:])%mod)