mod=10**9+7
h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]
#k:=照明のおけるマス(散らかってないマス)の個数
k=sum(s[i][j]=="." for j in range(w) for i in range(h))
#前計算　po[i]:=2^i
po=[0]*(k+1)
po[0]=1
for i in range(1,k+1):
    po[i]=po[i-1]*2
    po[i]%=mod
from itertools import groupby
#check[i][j]:=(マス(i,j)を照らすことのできるマスの個数)
#そのマスが照らされる照明の置き方の数は(2^k)-(2^(k-check[i][j]))
check=[[0]*w for _ in range(h)]
#行方向
for i in range(h):
    now=0
    for key,group in groupby(s[i]):
        l=len(list(group))
        if key==".":
            for j in range(now,now+l):
                check[i][j]+=l
        now+=l
#列方向
for j in range(w):
    now=0
    for key,group in groupby(s[i][j] for i in range(h)):
        l=len(list(group))
        if key==".":
            for i in range(now,now+l):
                check[i][j]+=l
        now+=l
#場合の数を数える(全てのマスで足し合わせれば良い)
ans=0
for i in range(h):
    for j in range(w):
        if check[i][j]!=0:
            #行方向と列方向でダブルカウントしていることに注意！
            ans+=(po[k]-po[k-check[i][j]+1])
            ans%=mod
print(ans)