n,k=map(int,input().split())
dp=[[0,0,0] for i in range(n)]
janken=list(map(int,input().split()))
t=[0 if i=="r" else 1 if i=="s" else 2 for i in input()]
#直後の手を見て決める
for i in range(n):
    if i<k:
        for j in range(3):
            if (j+1)%3==t[i]:
                dp[i][j]=janken[j]
    else:
        #更新
        for j in range(3):
            #遷移の元
            for l in range(3):
                if j!=l:
                    if (j+1)%3==t[i]:
                        dp[i][j]=max(dp[i][j],janken[j]+dp[i-k][l])
                    else:
                        dp[i][j]=max(dp[i][j],dp[i-k][l])
ans=0
for i in range(n-k,n):
    ans+=max(dp[i])
print(ans)