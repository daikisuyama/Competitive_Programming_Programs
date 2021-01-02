#実装踏んだ
from itertools import groupby
for _ in range(int(input())):
    n=int(input())
    s=""
    for i in range(n):
        s+=input()
    s=list(s)
    s.sort()
    for i,j in groupby(s):
        if len(list(j))%n!=0:
            print("NO")
            break
    else:
        print("YES")