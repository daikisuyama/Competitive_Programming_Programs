n,m,v,p=map(int,input().split())
a=[int(i) for i in input().split()]
a.sort(reverse=True)
a=a[p-1:]
le=len(a)
l,r=0,le-1

def adopt(x):
    global a,n,m,v,p
    b=a[x]+m
    if b<a[0]:
        return False
    al=v*m
    al-=(n-x)*m
    if al<=0:
        return True
    s=x*b-sum(a[:x])
    if al>s:
        return False
    else:
        return True

while l+1<r:
    k=(l+r)//2
    if adopt(k):
        l=k
    else:
        r=k

if adopt(r):
    print(p+r)
else:
    print(p+l)
