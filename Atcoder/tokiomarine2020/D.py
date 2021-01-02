n=int(input())
vw=[list(map(int,input().split())) for i in range(n)]
#vmax=max(i[0] for i in vw)
#前計算用のDPを用意する
#1~2^10までは計算で先に求めておく
dp=[[0]*(10**5+1) for i in range(2**10)]
#前計算
def dfs(i):
    global n,vw,dp
    j=i//2
    for k in range(10**5,-1,-1):
        if dp[j-1][k]!=0 or k==0:
            if k+vw[i-1][1]<=10**5:
                dp[i-1][k+vw[i-1][1]]=max(dp[j-1][k]+vw[i-1][0],dp[i-1][k+vw[i-1][1]])
            dp[i-1][k]=max(dp[j-1][k],dp[i-1][k])
    if i*2<=2**10 and i*2<=n:
        dfs(i*2)
        if i*2+1<=2**10 and i*2+1<=n:
            dfs(i*2+1)
dfs(1)
for i in range(2**10):
    for j in range(10**5):
        dp[i][j+1]=max(dp[i][j],dp[i][j+1])
q=int(input())
for i in range(q):
    #それぞれの部分木をたどる
    #こっちで残りを全探索
    v,l=map(int,input().split())
    cand=[]
    while v>2**10:
        cand.append(v//2)
        v=v//2
    r=len(cand)
    ans=0
    for j in range(2**r):
        v_sub=0
        w_sub=0
        for k in range(r):
            v_sub+=vw[cand[k]-1][0]*(j>>k)&1
            w_sub+=vw[cand[k]-1][1]*(j>>k)&1
        if w_sub>l:
            continue
        else:
            ans=max(ans,dp[v-1][l-w_sub]+v_sub)
    print(ans)


