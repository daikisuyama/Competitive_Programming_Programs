#11:43~
#は？ソートしてない
#10分+20分
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
a.sort()
b.sort()
c.sort()
da=[0]*n
db=[0]*n
from bisect import bisect_right
for i in range(n):
    now=bisect_right(c,b[i])
    db[i]=n-now
for i in range(n-1,0,-1):
    db[i-1]+=db[i]
for i in range(n):
    now=bisect_right(b,a[i])
    if now<n:
        da[i]+=db[now]
print(sum(da))