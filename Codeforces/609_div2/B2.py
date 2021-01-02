from collections import Counter
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=sorted([list(i) for i in list(Counter(a).items())],key=lambda x:x[0])
d=sorted([list(i) for i in list(Counter(b).items())],key=lambda x:x[0])
n=len(c)
x=0
for i in range(n):
    p=c.pop(-1)
    dp=(d[0][0]+m-p[0])%m
    x+=dp
    c.insert(0,p)
    for j in range(n):
        c[j][0]+=dp
        c[j][0]%=m
    if c==d:
        print(x%m)
        break