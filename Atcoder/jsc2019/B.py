from bisect import bisect_right
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=sorted(a)
mod=10**9+7
ans=0
for i in range(n):
    for j in range(n):
        if i<j and a[i]>a[j]:
            ans+=1
ans*=k
#print(ans)
ans%=mod
r=0
for i in range(n):
    r+=(n-bisect_right(b,b[i]))
ans+=(r*(k-1)*k//2)
ans%=mod
print(ans)