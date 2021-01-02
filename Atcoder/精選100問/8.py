#11/25 10:23~10:35
n=int(input())
ab=[list(map(int,input().split())) for i in range(n)]
ans=10**30
from itertools import chain
for i in chain.from_iterable(ab):
    for j in chain.from_iterable(ab):
        #入り口:i,出口:j
        x=0
        for k in range(n):
            a,b=ab[k]
            x+=min(abs(a-i)+abs(b-a)+abs(j-b),abs(b-i)+abs(a-b)+abs(j-a))
        ans=min(ans,x)
print(ans)