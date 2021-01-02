#11/28 10:40~
k=int(input())
base=[[0]*8 for i in range(8)]
for i in range(k):
    r,c=map(int,input().split())
    base[r][c]=1
#決めるべき行と選択できる列の候補
candr,candc=[],[]
for i in range(8):
    if 1 not in base[i]:
        candr.append(i)
for j in range(8):
    for i in range(8):
        if base[i][j]:
            break
    else:
        candc.append(j)
l=len(candr)
#あるマスをcheckしたときにcheckすべき斜めのマスの候補
checkcand=[[[] for i in range(8)] for j in range(8)]
for i in range(8):
    for j in range(8):
        for x in range(8):
            for y in range(8):
                if abs(i-x)==abs(j-y) and i!=x:
                    checkcand[i][j].append([x,y])
from itertools import permutations
#print(candr,candc)
for p in permutations(candc):
    now=[[base[i][j] for j in range(8)] for i in range(8)]
    #print(p)
    for i in range(l):
        now[candr[i]][p[i]]=1
    #斜めの条件をチェック
    f=True
    for i in range(8):
        for j in range(8):
            if now[i][j]:
                if any(now[x][y] for x,y in checkcand[i][j]):
                    f=False
                    break
        if not f:break
    if f:
        ans=[["Q" if now[i][j] else "." for j in range(8) ] for i in range(8)]
        for i in range(8):
            print("".join(ans[i]))
        break
            


