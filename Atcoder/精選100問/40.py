#14:24
n,k=map(int,input().split())
days=[-1]*n
for i in range(k):
    a,b=map(int,input().split())
    days[a-1]=b-1
mod=10000
dp=[[[0]*2 for i in range(3)] for i in range(n)]
if days[0]==-1:
    dp[0][0][0]=1
    dp[0][1][0]=1
    dp[0][2][0]=1
else:
    dp[0][days[0]][0]=1
for i in range(n-1):
    #どのピザ食ったか
    for j in range(3):
        #何枚食ったか
        for l in range(2):
            #ピザが決まってる場合
            if days[i+1]!=-1:
                if days[i+1]!=j:
                    dp[i+1][days[i+1]][0]+=dp[i][j][l]
                    dp[i+1][days[i+1]][0]%=mod
                else:
                    if l==0:
                        dp[i+1][days[i+1]][l+1]+=dp[i][j][l]
                        dp[i+1][days[i+1]][l+1]%=mod
                continue
            #ピザが決まってない場合
            #どのピザか
            for m in range(3):
                if m!=j:
                    dp[i+1][m][0]+=dp[i][j][l]
                    dp[i+1][m][0]%=mod
                else:
                    if l==0:
                        dp[i+1][m][l+1]+=dp[i][j][l]
                        dp[i+1][m][l+1]%=mod
ans=0
for j in range(3):
    for l in range(2):
        ans+=dp[n-1][j][l]
        ans%=mod
print(ans)