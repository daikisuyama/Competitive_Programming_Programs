n,m,v,p=map(int,input().split())
a=sorted(list(map(int, input().split())),reverse=True)[p-1:]
l,r=0,n-p
while l+1<r:
    k=(l+r)//2
    b=a[k]+m
    if b<a[0] or (v-(n-k))*m>(k*b-sum(a[:k])): r=k
    else: l=k
b=a[r]+m
print(p+l if(b<a[0] or (v-(n-r))*m>(r*b-sum(a[:r]))) else p+r)
