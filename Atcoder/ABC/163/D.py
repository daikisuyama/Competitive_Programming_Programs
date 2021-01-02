n,k=map(int,input().split())
ans=0
for i in range(k,n+2):
    ans+=((n-i+1)*i+1)
    ans%=(10**9+7)
print(ans)