#dpを三次元にやればできそう
n=int(input())
inf=1000000000000000
#最短の長さ、何通りか
dp=[[[inf,0] if i!=j else [0,0] for j in range(n)] for i in range(n)]
a,b=map(int,input().split())
m=int(input())
for i in range(m):
    x,y=map(int,input().split())
    dp[x-1][y-1][0]=1
    dp[x-1][y-1][1]+=1
    dp[y-1][x-1][0]=1
    dp[y-1][x-1][1]+=1

for i in range(n):
    for j in range(n):
        for k in range(n):
            l1=dp[j][i][0]+dp[i][k][0]
            l2=dp[j][k][0]
            if l2==l1:
                dp[j][k][1]+=dp[j][i][1]*dp[i][k][1]
            elif l1<l2:
                dp[j][k][0]=l1
                dp[j][k][1]+=dp[j][i][1]*dp[i][k][1]
print(dp[a-1][b-1][1]%(10**9+7))
