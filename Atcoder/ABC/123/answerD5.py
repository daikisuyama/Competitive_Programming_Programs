#AC済み
x,y,z,k=map(int,input().split())
a=sorted([int(i) for i in input().split()])
b=sorted([int(i) for i in input().split()])
c=sorted([int(i) for i in input().split()])
ab=sorted([a[i]+b[j] for j in range(y) for i in range(x)],reverse=True)
ab=ab[:k]
l=len(ab)
abc=sorted([ab[i]+c[j] for j in range(z) for i in range(l)],reverse=True)
for i in range(k):
    print(abc[i])
