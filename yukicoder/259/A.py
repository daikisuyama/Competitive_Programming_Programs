n,d=map(int,input().split())
x=list(map(int,input().split()))
v=list(map(int,input().split()))
s=sum(v)

def f(k):
    return s*k

l,r=0,1000000000000
while l+1<r:
    k=l+(r-l)//2
    if f(k)>=d:
        r=k
    else:
        l=k
print(r)
