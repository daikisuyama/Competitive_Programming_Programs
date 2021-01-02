n=int(input())
s=list(map(int,input()))
t=list(map(int,input()))
s0,t0=s.count(0),t.count(0)
if s0>t0 or s0%2!=t0%2:
    print(-1)
    exit()
sind=[i for i in range(n) if s[i]==0]
tind=[i for i in range(n) if t[i]==0]
ls,lt=len(sind),len(tind)
for i in range(ls-1,-1,-1):
    ch=tind[-(ls-i)]-sind[i]
    if ch<0:
        print(-1)
        exit()
#左から決めていけば一意に決まる
#1を左に運ぶ(ずっと0を右に運ぼうとしたけど、実装めんどい)
#11を00に置き換える
#s_i,s_i+1,t_i,t_i+1をみる
#s_i,t_iを一致させるように(一致しない場合のみ)
#(1,1),(0,0)の時、変えるだけ+1(次は一致する)
#(1,1),(0,1)の時、変えるだけ+1、この時s_i+1は0でt_i+1は1になる
#(1,0),(0,0)もしくは(1,0),(0,1)の時→ないようにしたい
#(0,0),(1,0)もしくは(0,0),(1,1)の時→ないようにしたい
#(0,1),(1,1)の時、変える+1、この時s_i+1は0でt_i+1は1になる
#(0,1),(1,0)の時、変える+1、この時s_i+1は0でt_i+1は0になる