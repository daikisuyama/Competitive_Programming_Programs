#十字で合流する場合
#if文の位置を間違えていた
n=int(input())
ud=[[[],[]] for i in range(200001)]
rl=[[[],[]] for i in range(200001)]
from bisect import *
cross=[[dict(),dict()] for i in range(4)]
for i in range(n):
    x,y,u=input().split()
    x,y=int(x),int(y)
    if u=="U":
        ud[x][0].append(y)
        if x+y in cross[0][1]:
            cross[0][1][x+y].append(x)
        else:
            cross[0][1][x+y]=[x]
        if x-y in cross[1][1]:
            cross[1][1][x-y].append(x)
        else:
            cross[1][1][x-y]=[x]
    elif u=="D":
        ud[x][1].append(y)
        if x+y in cross[3][1]:
            cross[3][1][x+y].append(x)
        else:
            cross[3][1][x+y]=[x]
        if x-y in cross[2][1]:
            cross[2][1][x-y].append(x)
        else:
            cross[2][1][x-y]=[x]
    elif u=="R":
        rl[y][0].append(x)
        if x+y in cross[0][0]:
            cross[0][0][x+y].append(x)
        else:
            cross[0][0][x+y]=[x]
        if x-y in cross[2][0]:
            cross[2][0][x-y].append(x)
        else:
            cross[2][0][x-y]=[x]
    else:
        rl[y][1].append(x)
        if x+y in cross[3][0]:
            cross[3][0][x+y].append(x)
        else:
            cross[3][0][x+y]=[x]
        if x-y in cross[1][0]:
            cross[1][0][x-y].append(x)
        else:
            cross[1][0][x-y]=[x]

for i in range(200001):
    ud[i][0].sort()
    ud[i][1].sort()
    rl[i][0].sort()
    rl[i][1].sort()

ans=[]
for i in range(200001):
    l1,l2=len(ud[i][0]),len(ud[i][1])
    if l1 and l2:
        for j in ud[i][0]:
            b=bisect_left(ud[i][1],j)
            if b!=l2:
                ans.append(ud[i][1][b]-j)
    l1,l2=len(rl[i][0]),len(rl[i][1])
    if l1 and l2:
        for j in rl[i][0]:
            b=bisect_left(rl[i][1],j)
            if b!=l2:
                ans.append(rl[i][1][b]-j)

for i in range(4):
    for j in range(2):
        for k in cross[i][j]:
            cross[i][j][k].sort()

for i in range(4):
    for j in cross[i][1]:
        if j in cross[i][0]:
            l=len(cross[i][0][j])
            if i%2==1:
                for k in cross[i][1][j]:
                    b=bisect_left(cross[i][0][j],k)
                    if b!=l:
                        ans.append(2*cross[i][0][j][b]-2*k)
            else:
                for k in cross[i][1][j]:
                    b=bisect_right(cross[i][0][j],k)-1
                    if b!=-1:
                        ans.append(2*k-2*cross[i][0][j][b])

if len(ans):
    print(min(ans)*5)
else:
    print("SAFE")