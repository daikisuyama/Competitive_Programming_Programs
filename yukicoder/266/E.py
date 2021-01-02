n=int(input())
a=list(map(int,input().split()))
a.sort()
from bisect import bisect_left,bisect_right
ans=0
d=dict()
for i in range(n):
    if a[i] in d:
        ans+=d[a[i]]
        continue
    ans_sub=0
    j=i
    while j!=n:
        x=a[j]//a[i]
        b=bisect_left(a,(x+1)*a[i],lo=j)-1
        ans_sub+=(x*(b-j+1)*a[i])
        j=b+1
    d[a[i]]=ans_sub
    ans+=ans_sub
print(sum(a)*n-ans)