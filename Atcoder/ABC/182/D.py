n=int(input())
a=list(map(int,input().split()))
from itertools import accumulate
b=list(accumulate(a))
c=list(accumulate(b,func=max))
ans=[0,b[0]]
now=b[0]
for i in range(1,n):
    ans.append(now+c[i])
    now+=b[i]
ans.append(now)
print(max(ans))