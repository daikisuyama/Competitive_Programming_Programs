n=int(input())
a=list(map(int,input().split()))
m=sum(a)
k=0
l=0
for i in range(n):
    k+=a[i]
    if k>m//2:
        l=i
        break
if n==2:
    print(abs(a[1]-a[0]))
else:
    print(min(abs(k-(m-k)),abs(k-a[i]-(m-(k-a[i])))))
