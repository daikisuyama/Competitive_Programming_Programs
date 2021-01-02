#前から順に詰めてけばいいんじゃないか？
#前から見ていくときに上が先に足されてればいいのでは
#input()ではなくreadline使う
#末尾の改行コードを取り除かねばならない
#intにするときは改行コード取らずにintにできる
#https://qiita.com/kyuna/items/8ee8916c2f4e36321a1c#3-sysstdin
#https://www.lifewithpython.com/2014/05/python-get-stdin-standard-input.html
import sys
n,q=map(int,input().split())
tree=[list(map(int,input().split())) for i in range(n-1)]
#f1は使ったのかどうかを表すフラッグ
#f2はそれまでに出てきたものを表すフラッグ
f1=[0]*(n-1)
f2=[1]

c=[0]*n
for i in range(q):
    p,x=map(int,input().split())
    c[p-1]+=x
#print(tree)
while f1!=[1]*(n-1):
    #print(c)
    for i,t in enumerate(tree):
        if f1[i]==0:
            if t[0] in f2:
                c[t[1]-1]+=c[t[0]-1]
                f1[i]=1
                f2.append(t[1])
            elif t[1] in f2:
                c[t[0]-1]+=c[t[1]-1]
                f1[i]=1
                f2.append(t[0])
            else:
                pass

for i in range(n-1):
    print(c[i],end=" ")
print(c[n-1])
