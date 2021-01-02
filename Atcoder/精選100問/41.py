#14:40
#連続なので直前わかればいい
#dp[i][j]i日目の最後に着た服がj
d,n=map(int,input().split())
t=[int(input()) for i in range(d)]
cl=[list(map(int,input().split())) for i in range(n)]
inf=10**20
dp=[[-inf]*n for i in range(d)]
for i in range(n):
    if cl[i][0]<=t[0]<=cl[i][1]:
        dp[0][i]=0
for i in range(d-1):
    #何着て
    for j in range(n):
        if dp[i][j]==-inf:continue
        #何着る
        for k in range(n):
            if cl[k][0]<=t[i+1]<=cl[k][1]:
                dp[i+1][k]=max(dp[i+1][k],dp[i][j]+abs(cl[k][2]-cl[j][2]))
print(max(dp[d-1]))