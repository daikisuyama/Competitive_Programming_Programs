#できた！！
from itertools import groupby
n=int(input())
a=list(map(int,input().split()))
INF=100000000000000
dp=[[-INF]*61 for i in range(n)]
ans=-INF
for i in range(n):
    #+30を忘れずに
    #ハジメ
    if i==0:
        dp[i][a[i]+30]=0
        continue
    #それを一つ目で選ぶ場合
    dp[i][a[i]+30]=0
    #連続している場合
    for j in range(61):
        if dp[i-1][j]==-INF:
            continue
        if j<=a[i]+30:
            dp[i][a[i]+30]=max(dp[i][a[i]+30],dp[i-1][j]+a[i]-(a[i]+30-j))
        else:
            dp[i][j]=dp[i-1][j]+a[i]
    ans=max(ans,max(dp[i]))
print(max(ans,0))