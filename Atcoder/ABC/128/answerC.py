#これも一時間はかかったなあ
#クソコードだけど通ってよかった
#前から順にループ回すだけ
#ループ内の処理は出来るだけしない
import copy
n,m=map(int,input().split())
k=[[] for _ in range(n)]

for i in range(m):
    for j in [int(_) for _ in input().split()][1:]:
        k[j-1].append(i)
#偶数回はFalse、奇数回はTrue
p=[bool(int(i)) for i in input().split()]

p2=[False]*m
c=0
for i in range(2**n):
    l=format(i,"0>10b")[-n:]
    t=copy.deepcopy(p)
    for j in range(n):
        if l[j]=="1":
            for h in k[j]:
                t[h]= not t[h]
    if t==p2:
        c+=1
print(c)
