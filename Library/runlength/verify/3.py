#連続した部分が直立or逆立ちとする
#直立→直,逆立ち→逆,として省略
#この時、直でk個選んで逆立ちさせる
#スライドさせて考えれば良い
#一番効率の良いのは"逆…逆"の2k+1個の部分
#全て選べる場合は先に場合分け(1)
#直で始まるor直で終わる場合は場合分け(2)
#これらの場合分けにより逆…逆"の2k+1個の部分を考えるだけ(3)
from itertools import groupby
n,k=map(int,input().split())
s=input()
ans=[[int(key),len(list(group))] for key,group in groupby(s)]
l=len(ans)
x=0
#(1)
if ans[0][0]==0:
    if l<=2*k:
        y=0
        for i in range(l):
            y+=ans[i][1]
        x=max(y,x)
        print(x)
        exit()
else:
    if l<=2*k+1:
        y=0
        for i in range(l):
         y+=ans[i][1]
        x=max(y,x)
        print(x)
        exit()
#(2)
#直で始まる
y=0
for i in range(2*k):
    y+=ans[i][1]
x=max(y,x)
#直で終わる
y=0
for i in range(2*k):
    y+=ans[-1-i][1]
x=max(y,x)
#逆始まり逆終わりに変換する
if ans[0][0]==0:
    ans=ans[1:]
    l-=1
if ans[-1][0]==0:
    ans=ans[:-1]
    l-=1
if l<=2*k+1:
    print(x)
    exit()
#(3)
y=0
for i in range(2*k+1):
    y+=ans[i][1]
x=max(y,x)
for i in range(k,(l-1)//2+1):
    #[2*(i-k),2*i]
    if i==k:continue
    y+=ans[2*i-1][1]
    y+=ans[2*i][1]
    y-=ans[2*(i-k)-2][1]
    y-=ans[2*(i-k)-1][1]
    x=max(y,x)
print(x)