n,w=map(int,input().split())
persons=[list(map(int,input().split())) for i in range(n)]
check=[0]*(2*10**5+1)
for i in range(n):
    s,t,p=persons[i]
    check[s]+=p
    check[t]-=p
from itertools import accumulate
d=list(accumulate(check))
if max(d)<=w:
    print("Yes")
else:
    print("No")