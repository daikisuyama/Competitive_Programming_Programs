n,q=input().split()
n,q=int(n),int(q)
a=[0 for i in range(n)]
for i in range(q):
    l,r,t=input().split()
    l,r,t=int(l)-1,int(r),int(t)
    a[l:r]=[t for i in range(r-l)]

for i in a:
    print(i)
