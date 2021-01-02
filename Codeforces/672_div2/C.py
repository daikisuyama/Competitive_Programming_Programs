inf=10**12
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    dp=[[-inf,-inf] for i in range(n)]
    dp[0]=[-inf,a[0]]
    for i in range(n-1):
        dp[i+1][0]=dp[i][0]
        dp[i+1][1]=dp[i][1]
        dp[i+1][0]=max(dp[i+1][0],dp[i][1]-a[i+1])
        dp[i+1][1]=max(dp[i+1][1],dp[i][0]+a[i+1])
        dp[i+1][1]=max(dp[i+1][1],a[i+1])
    print(max(dp[n-1]))
    #print(dp)