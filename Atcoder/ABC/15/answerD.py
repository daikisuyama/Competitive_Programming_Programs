w=int(input())
n,k=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]
dp=[[0]*(w+1) for i in range(k+1)]
for i in range(n):
    dp_sub=[[0]*(w+1) for i in range(k+1)]
    for j in range(k):
        for l in range(w+1):
            if (j==0 and l==0) or dp[j][l]!=0:
                if l+ab[i][0]<=w:
                    dp_sub[j+1][l+ab[i][0]]=dp[j][l]+ab[i][1]
    for j in range(k+1):
        for l in range(w+1):
            dp[j][l]=max(dp_sub[j][l],dp[j][l])
ma=0
for j in range(k+1):
        for l in range(w+1):
            ma=max(ma,dp[j][l])
print(ma)