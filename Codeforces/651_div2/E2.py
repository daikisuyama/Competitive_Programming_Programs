#もっと実装を軽くする！
n=int(input())
s=input()
t=input()
if s.count("1")!=t.count("1"):
    print(-1)
    exit()

#文字列の+の計算量
x=[s[i] for i in range(n) if s[i]!=t[i]]

#vは0スタート
#wは1スタート
#1は合計
#2は余ってるやつ
v1,v2,w1,w2=0,0,0,0
for i in x:
    if i=="0":
        if w2==0:
            if v1==v2:
                v1+=1
            v2+=1
        else:
            w2-=1
    else:
        if v2==0:
            if w1==w2:
                w1+=1
            w2+=1
        else:
            v2-=1
print(v1+w1)
