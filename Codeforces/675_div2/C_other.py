mod=10**9+7
s=list(map(int,input()))
n=len(s)
a=[0]*(n+1)
b=[0]*(n+1)
a[0]=1
ans=0
for i in range(n):
    a[i+1]=a[i] * 10
    b[i + 1]=b[i] + (i + 1) * a[i]
for i in range(1,n+1):
    c=s[i-1]
    f=(i-1)*i//2
    ans+=c * f * a[n - i] + c * b[n - i]
print(ans)