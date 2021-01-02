from math import log2
from itertools import accumulate
x=[0]+[log2(i) for i in range(1,10**5+1)]
a=list(accumulate(x))

for _ in range(int(input())):
    n,m,k=map(int,input().split())
    ans=["Flush","Straight"]
    print(ans[a[n]-a[n-k]-a[k]>(a[n-k+1]-a[n-k])+(k-1)*(a[m]-a[m-1])])