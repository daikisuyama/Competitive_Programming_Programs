n,t=map(int,input().split())
a=list(map(int,input().split()))
if n<=21:
    ans=0
    for i in range(2**n):
        x=0
        for j in range(n):
            if (i>>j)&1:
                x+=a[j]
        if x<=t:
            ans=max(ans,x)
    print(ans)
    exit()
from bisect import bisect_right
#以下22以上
n1,n2=20,n-20
a1,a2=a[:20],a[20:]
f1,f2=[],[]
for i in range(2**n1):
    x=0
    for j in range(n1):
        if (i>>j)&1:
            x+=a1[j]
    if x<=t:
        f1.append(x)
for i in range(2**n2):
    x=0
    for j in range(n2):
        if (i>>j)&1:
            x+=a2[j]
    if x<=t:
        f2.append(x)
f1=sorted(list(set(f1)))
f2=sorted(list(set(f2)))
ans=0
#t-i以下での最大をf1から探す
for i in f2:
    e=bisect_right(f1,t-i)-1
    if e==-1:
        continue
    ans=max(ans,f1[e]+i)
print(ans)

