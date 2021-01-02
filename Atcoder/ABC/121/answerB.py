n,m,c=map(int,input().split())
b=list(map(int,input().split()))
ans=0
for i in range(n):
    a=list(map(int,input().split()))
    k=0
    for i in range(m):
        k+=a[i]*b[i]
    ans+=(k+c>0)
print(ans)
