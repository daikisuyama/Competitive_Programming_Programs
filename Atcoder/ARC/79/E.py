n=int(input())
a=list(map(int,input().split()))
ans=0
while True:
    b=[0]*n
    for i in range(n):
        b[i]=a[i]//n
    s=sum(b)
    ans+=s
    if s==0:break
    for i in range(n):
        a[i]%=n
        a[i]+=(s-b[i])
print(ans)