#木の問題と書いてあるが、実際は木の構造がわからなくても解ける
#根の方から順に足していってあげればいい
#aiがbiの親であるとは限らないらしい
#これがある以上、木構造を作るしかない
#辞書で(他の人のコードを参照)親子関係を保持できる、初めて知った
#は？結局他人の使わないやんけ

n,q=map(int,input().split())
tree1=[list(map(int,input().split())) for i in range(n-1)]
tree2=[i for i in tree1 if i[0]==1]
tree1=[i for i in tree1 if i not in tree2]

c=[0]*n
for i in range(q):
    p,x=map(int,input().split())
    c[p-1]+=x
    
l=0
while tree1!=[]:
    for j in tree2[:][l:]:
        l+=1
        for k in tree1[:]:
            if j[1]==k[0]:
                tree2.append(k)
                tree1.remove(k)
            elif j[1]==k[1]:
                tree2.append([k[1],k[0]])
                tree1.remove(k)



for i in tree2:
    c[i[1]-1]+=c[i[0]-1]

for i in range(n-1):
    print(c[i],end=" ")
print(c[n-1])
