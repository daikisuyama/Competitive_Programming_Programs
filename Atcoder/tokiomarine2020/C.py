#imos法で更新を繰り返す
#log回で終わる
from itertools import accumulate
n,k=map(int,input().split())
a=list(map(int,input().split()))
for _ in range(k):
    b=[0]*n
    for i in range(n):
        b[max(0,i-a[i])]+=1
        if i+a[i]+1<n:
            b[i+a[i]+1]-=1
    a=list(accumulate(b))
    if a==[n]*n:
        break
    print(a)
print(" ".join(map(str,a)))