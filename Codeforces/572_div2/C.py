n=int(input())
s=list(map(int,input().split()))
from itertools import accumulate
b=list(accumulate(s))
q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    if l==1:
        x=b[r-1]
    else:
        x=b[r-1]-b[l-2]
    print(x//10)