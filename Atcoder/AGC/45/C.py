n,a,b=map(int,input().split())
if a>b:
    a,b=b,a
#a個以上連続する0,b個以上連続する1
dp0=[[0]*(a-1) for i in range(n)]
dp1=[[0]*(b-1) for i in range(n)]
mod=10**9+7
ans=pow(2,n,mod)+mod
dp0[0][0]=1
dp1[0][0]=1
if a==1:
    print(ans)
    exit()
#1がi個連続する中にa個以上連続した**0のみ**を入れることができるのか
#1がi個連続する中にa個未満連続した0が一つでも入っている場合を考える
#ただし両端は1でなければならない
#i番目の要素の下がxで今の要素までがyの場合(xはaまで)
#(x,y)でmapを作る
#むり、再帰で行けそう
g=[[0]*a for i in range(b-1)]
for i in range(b-1):
    if i==0:
        g[i][0]=1
        continue
    g[i][0]=sum(g[i-1])
    for j in range(a-1):
        g[i][j+1]=g[i-1][j]
print(g)
h=[max(2**(i-1),1)-g[i][0]+1 for i in range(b-1)]
print(h)
for i in range(n-1):
    #i文字目が0の時
    #(1)を考える
    for j in range(b-1):
        dp0[i+1][0]+=(dp1[i][j]*h[j])%mod
    #0はa-1個まで連続しうる
    for j in range(a-1-1):
        dp0[i+1][j+1]=dp0[i][j]
    #i文字目が1の時
    for j in range(a-1):
        dp1[i+1][0]+=dp0[i][j]%mod
    #1はb-1個まで連続しうる(そのうちを置き換える)
    #k個(1~b-1)連続する時、そのうちのa(以上)個を置き換える(1)
    #ここでも包除を考える(1)
    for j in range(b-1-1):
        dp1[i+1][j+1]=dp1[i][j]

ans_=sum(dp0[n-1])%mod
for j in range(b-1):
    ans_+=(dp1[n-1][j]*h[j])%mod
print((ans-(ans_%mod))%mod)