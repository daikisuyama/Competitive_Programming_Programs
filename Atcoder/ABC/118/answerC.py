n=int(input())
a=list(map(int,input().split()))
while len(a)>1:
    l=len(a)
    a.sort()
    b=[a[0] if i==0 else a[i]%a[0] for i in range(l)]
    a=[b[i] for i in range(l) if b[i]!=0]
print(a[0])
