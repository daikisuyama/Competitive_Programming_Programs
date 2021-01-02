n,t=input().split()
n,t=int(n),int(t)

#開き始めと開き終わりを取得して更新する
#開き始めの更新の時にプラスしていく
#TLEシネ
#一旦配列に入れて順に比較したらダメだった
#むずくないか
'''
a=[]
for i in range(n):
    a.append(int(input()))
x=0
for i in range(n):
    x+=min([t,a[1]-a[0]])
    a=a[1:]

print(x+t)
'''
#ループ不変条件（ループ回した時にどのような挙動するかを把握したい）を考える

#前から順に考える
#戻ってとか考えると沼
#配列は作るな
x=0
a=int(input())
for i in range(n-1):
    b=int(input())
    x+=min([t,b-a])
    a=b

print(x+t)
