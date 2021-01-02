mod=10**9+7
h,w=map(int,input().split())
s=[list(input()) for i in range(h)]
dp=[[0]*w for i in range(h)]
dp[0][0]=1
#外側で列方向を考える
cht=[0]*w
for i in range(h):
    #この中では行方向を考えている
    #変化分を保存しておく
    ch=0
    for j in range(w):
        if s[i][j]=="#":
            dp[i][j]=0
            ch=0
            continue
        #行方向(先に更新,chのぶん)
        #行方向のぶんも
        dp[i][j]+=ch
        if i>0:
            dp[i][j]+=dp[i-1][j]
        if i>0 and j>0:
            dp[i][j]+=dp[i-1][j-1]
        ch+=dp[i][j]
        ch%=mod
        dp[i][j]%=mod
print(dp[h-1][w-1])
print(dp)
