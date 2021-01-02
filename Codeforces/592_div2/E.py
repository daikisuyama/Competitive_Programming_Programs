inf=10**18
n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
def f(x):
    y=k
    for i in range(x+1):
        y-=a[x]-a[i]
    if y<0:
        return inf
    #j→j-1に動かす(いくつぶんかも)
    for i in range(n-1,x,-1):
        if y>=(n-i)*(a[i]-a[i-1]):
            y-=(n-i)*(a[i]-a[i-1])
        else:
            return (a[i]-y//(n-i))-a[x]
    return 0
#minを動かしたとき0→n-1
l,r=0,n-1
while l+2<r:
    c1=l+(r-l)//3
    c2=r-(r-l)//3
    if f(c1)<f(c2):
        r=c2
    else:
        l=c1
print(sorted([(f(j),j) for j in range(l,r+1)])[0][0])