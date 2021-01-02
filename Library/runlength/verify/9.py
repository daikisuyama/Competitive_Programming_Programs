#順列より任意の要素が異なるので極大値が存在するとき狭義
from itertools import groupby
for _ in range(int(input())):
    n=int(input())
    p=list(map(int,input().split()))
    #増加する場合はTrue,減少する場合はFalse
    g=[[key,len(list(group))] for key,group in groupby(range(n-1),key=lambda i:p[i+1]-p[i]>0)]
    #極大値が存在するか(T→F)
    now=0
    if len(g)==1:
        print("NO")
    else:
        l=len(g)
        for i in range(l-1):
            now+=g[i][1]
            if g[i][0] and (not g[i+1][0]):
                print("YES")
                print(now,now+1,now+2)
                break
        else:
            print("NO")
