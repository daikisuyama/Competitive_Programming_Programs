#木の問題と書いてあるが、実際は木の構造がわからなくても解ける
#根の方から順に足していってあげればいい
#aiがbiの親であるとは限らないらしい
#これがある以上、木構造を作るしかない
#辞書で(他の人のコードを参照)親子関係を保持できる、初めて知った
#は？結局他人の使わないやんけ
from copy import deepcopy

n,q=map(int,input().split())
tree1=[list(map(int,input().split())) for i in range(n-1)]
tree2=[i for i in tree1 if i[0]==1]
tree1=[i for i in tree1 if i[0]!=1]

c=[0]*n
for i in range(q):
    p,x=map(int,input().split())
    c[p-1]+=x
l=0
while tree1!=[]:
    for j in tree2[l:][:]:
        #l+=1
        #三項演算子でelseは省略できない
        #print(tree1)
        tree3=[(k if j[1]==k[0] else ([k[1],k[0]] if j[1]==k[1] else None)) for k in tree1]
        #print(tree3)
        tree3=[i for i in tree3 if i is not None]
        l+=len(tree3)
        tree1=[k for k in tree1 if j[1] not in k]
        tree2.extend(tree3)
#print(tree2)
for i in tree2:
    c[i[1]-1]+=c[i[0]-1]

for i in range(n-1):
    print(c[i],end=" ")
print(c[n-1])
