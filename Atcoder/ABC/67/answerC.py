n=int(input())
a=[int(i) for i in input().split()]
s=sum(a)
c=0
b=[]
for i in range(n-1):
    c+=a[i]
    b.append(c)
mi=abs(s-2*b[0])
for i in range(n-1):
    mi=min(mi,abs(s-2*b[i]))
print(mi)
