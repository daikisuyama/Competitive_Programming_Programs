n=int(input())
vertex=[(n-i+1)*i for i in range(1,n+1)]
side=[0]*(n-1)
for i in range(n-1):
    l,r=list(map(int,input().split()))
    if l>r:
        l,r=r,l
    side[i]=l*(n-r+1)
print(sum(vertex)-sum(side))