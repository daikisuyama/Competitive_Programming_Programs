n,k=map(int,input().split())
a=list(map(int,input().split()))
def f(x):
    global a,n,k
    if x==0:
        return 10**10
    ret=0
    for i in range(n):
        ret+=(-((-a[i])//x)-1)
    return ret

l,r=0,10**10
while l+1<r:
    x=l+(r-l)//2
    if f(x)<=k:
        r=x
    else:
        l=x

print(r)
#print(f(r))