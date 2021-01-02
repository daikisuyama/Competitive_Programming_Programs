n=int(input())
a=[int(i) for i in input().split()]
s=sum(a)
c=a[0]
mi=abs(s-2*c)
for i in range(1,n):
    c+=a[i]
    mi=min(mi,abs(s-2*c))
print(mi)
