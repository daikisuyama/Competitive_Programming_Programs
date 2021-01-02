n,a=map(int,input().split())
x=list(map(int,input().split()))
x.sort(reverse=True)
sx=sum(x)
dp=[[0]*(n+1) for i in range(sx+1)]
dp[0][0]=1
for i in range(n):
    dp_sub=[[0]*(n+1) for j in range(sx+1)]
    for j in range(sx+1):
        for k in range(n+1):
            if (j==0 and k==0) or dp[j][k]!=0:
                dp_sub[j+x[i]][k+1]=dp[j][k]
    for j in range(sx+1):
        for k in range(n+1):
            dp[j][k]+=dp_sub[j][k]
cnt=0

for i in range(min(sx//a,n)):
    cnt+=dp[a*(i+1)][i+1]
print(cnt)