from itertools import accumulate
from collections import Counter
for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input()]
    s=[0]+list(accumulate(a))
    for i in range(n+1):
        s[i]-=i
    c=Counter(s)
    ans=0
    for i in c:
        ans+=(c[i]*(c[i]-1)//2)
    #print(c)
    print(ans)