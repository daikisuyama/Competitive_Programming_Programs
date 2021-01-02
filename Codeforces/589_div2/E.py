MOD=10**9+7
n,k=map(int,input().split())
perm=1
for i in range(1,n+1):
    perm*=i
    perm%=MOD
po1=[1]
po2=[1]
for i in range(n):
    po1.append(po1[-1]*(k-1)%MOD)
    po2.append(po2[-1]*(k)%MOD)
ans=1
for i in range(1,n+1):
    ans*=po1[i-1]
    ans*=po2[n-i]
    ans%=MOD
print(ans*perm%MOD)