n,k=map(int,input().split())
ans=n*(n-k)
for i in range(k+1,n+1):
    ans-=(k*(n//i))
    ans-=max(0,min(k-1,n%i))
print(ans)