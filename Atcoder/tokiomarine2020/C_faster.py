from itertools import accumulate
n,k,*a=map(int,open(0).read().split())
for _ in range(k):
    b=[0]*n
    for i in range(n):
        b[max(0,i-a[i])]+=1
        if i+a[i]+1<n:b[i+a[i]+1]-=1
    a=list(accumulate(b))
    if a==[n]*n:break
print(" ".join(map(str,a)))