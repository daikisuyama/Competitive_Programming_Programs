n=int(input())
a=list(map(int,input().split()))
a.sort()

def f(k):
    ans=abs(1-a[0])
    b=1
    for i in range(n-1):
        b=b*k
        ans+=abs(b-a[i])
    return ans

l,r=0,10**9
while l+2<r:
    c1=l+(r-l)//3
    c2=r-(r-l)//3
    if f(c1)<f(c2):
        r=c2
    else:
        l=c1
x=sorted([(f(j),j) for j in range(l,r+1)])[0][0]
print(x)