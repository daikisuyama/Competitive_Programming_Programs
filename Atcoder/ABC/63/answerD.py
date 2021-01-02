import math
n,a,b=map(int,input().split())
h=[int(input()) for i in range(n)]

def explode(x):
    global n
    c=0
    for i in range(n):
        if h[i]-x*b>0:
            c+=math.ceil((h[i]-x*b)/(a-b))
    return c<=x

l,r=1,10**9
while l+1<r:
    k=(l+r)//2
    if explode(k):
        r=k
    else:
        l=k

print(l if explode(l) else r)
