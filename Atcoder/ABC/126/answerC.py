n,k=map(int,input().split())
ans=0
for i in range(1,n+1):
    j,now=0,i
    while now<k:
        j+=1
        now*=2
    ans+=(2**(-j))
print(ans/n)