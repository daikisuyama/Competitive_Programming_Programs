from itertools import accumulate
from bisect import bisect_left,bisect_right
n,m,k=map(int,input().split())
a=[0]+list(accumulate(map(int,input().split())))
b=[0]+list(accumulate(map(int,input().split())))
ans=[0]
for i in range(n+1):
    c=bisect_right(b,k-a[i])-1
    if c!=-1:
        ans.append(c+i)
print(max(ans))