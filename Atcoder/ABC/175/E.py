import sys
input=sys.stdin.readline
r,c,k=map(int,input().split())
item=[[0]*c for i in range(r)]
for i in range(k):
    x,y,z=map(int,input().split())
    item[x-1][y-1]=z
dp=[[[0,0,0,0] for j in range(c)] for i in range(r)]
if item[0][0]>0:
    dp[0][0]=[0,item[0][0],0,0]
for i in range(r):
    for j in range(c):
        for l in range(4):
            if l<3:
                #した行く分にはOK
                if i!=r-1:
                    dp[i+1][j][0]=max(dp[i+1][j][0],dp[i][j][l])
                    if item[i+1][j]>0:
                        dp[i+1][j][1]=max(dp[i+1][j][0],dp[i][j][l])+item[i+1][j]
                #右は？
                if j!=c-1:
                    dp[i][j+1][l]=max(dp[i][j+1][l],dp[i][j][l])
                    if item[i][j+1]>0:
                        dp[i][j+1][l+1]=max(dp[i][j+1][l+1],dp[i][j][l]+item[i][j+1])
            else:
                #した行く分にはOK
                if i!=r-1:
                    dp[i+1][j][0]=max(dp[i+1][j][0],dp[i][j][l])
                    if item[i+1][j]>0:
                        dp[i+1][j][1]=max(dp[i+1][j][0],dp[i][j][l])+item[i+1][j]
                #右は？
                if j!=c-1:
                    dp[i][j+1][l]=max(dp[i][j+1][l],dp[i][j][l])
print(max(dp[r-1][c-1]))
