#マジでむずい
#40分程度考えても思いつかず
import itertools
n,a,b,c=map(int,input().split())
l1=[int(input()) for _ in range(n)]

#とりあえず全部並べる？
#並べて近づけてくか
#大きいものをまずは決めるか
#三本になるまで接続していく
#距離が9以下が目安だけど、無理な場合もある
#どの順番で接続すれば良いのか
#順番は関係ない
#近い方にくっつければいいのか
#a→b→cで決めるか
#8なら全部の組み合わせできそう

#ダメだ、難しすぎる
#方法を全て数え上げるのはこの時も有効、なぜならパターンが少ないから
#順番は無視する
#ただし、どのように数えるかがわからなかった
#A,B,Cのどの素材として使うのか、それとも使わないのか考える
#これで4^n通り(最悪6*10^5)なので、簡単に調べられる
x=10**9
#print(list(itertools.product([0,1,2,3], repeat=n)))
for i in list(itertools.product([0,1,2,3], repeat=n)):
    l2=[0]*3
    for j in range(n):
        if i[j]!=3:
            l2[i[j]]+=l1[j]
    l2=sorted(l2)
    if l2[0]!=0:
        l3=(len([_ for _ in i if _<3])-3)*10+abs(c-l2[0])+abs(b-l2[1])+abs(a-l2[2])
        if l3<x:
            x=l3

print(x)
