n=int(input())
a=list(map(int,input().split()))
from itertools import accumulate
b=list(accumulate(a))
c=list(accumulate(b,func=max))
d=list(accumulate(b))
ans=[0]+[d[i]+c[i] for i in range(n-1)]+[d[n-1]]
print(max(ans))