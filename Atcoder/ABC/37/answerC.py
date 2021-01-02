n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=sum(a[:k])
m=sum(a[:k])
for i in range(n-k):
    m=m-a[i]+a[k+i]
    ans+=m
print(ans)
