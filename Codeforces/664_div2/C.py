n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
change=[[a[i]&b[j] for j in range(m)]for i in range(n)]
dp=[[0]*(2**9) for i in range(n)]

for i in range(n):
    if i==0:
        for k in range(m):
            dp[0][change[i][k]]=1
        continue
    for j in range(2**9):
        if dp[i-1][j]==1:
            for k in range(m):
                dp[i][j|change[i][k]]=1

for j in range(2**9):
    if dp[-1][j]==1:
        print(j)
        break