n=int(input())
xy=[list(map(int,input().split())) for i in range(n)]
#xの座標ごとに
x=dict()
for i in range(n):
    if xy[i][0] in x:
        x[xy[i][0]].append(xy[i][1])
    else:
        x[xy[i][0]]=[xy[i][1]]
#yの要素ごとに
y=dict()
for i in range(n):
    if xy[i][1] in y:
        y[xy[i][1]].append(xy[i][0])
    else:
        y[xy[i][1]]=[xy[i][0]]
#マージが上手くいってない
#マージさせる時UnionFind
lattice=[]
#すでに出ていたら数えなければ？
#マージにUnionFind
check=set()
for i in x:
    if len(x[i])>1:
        candy=set()
        candx=set()
        for j in x[i]:
            if len(y[j])>1:
                for k in y[j]:
                    candx.add(k)
        for j in candx:
            if len(x[j])>1: 
                for k in x[j]:
                    candy.add(k)
        for j in candx:
            if j in check:
                break
        else:
            for j in candx:
                check.add(j)
            lattice.append([list(candx),list(candy)])
        for j in candx
#同じのが複数に現れる場合はマージ
if lattice==[]:
    print(0)
    exit()
#出力するもの違った(関係するものを引く)
ans=0
ax,ay=set(),set()
for i in lattice:
    for j in i[0]:
        ax.add(j)
    for j in i[1]:
        ay.add(j)
for i in range(n):
    if xy[i][0] in ax:
        ans-=1
for i in lattice:
    ans+=len(i[0])*len(i[1])
print(ans)