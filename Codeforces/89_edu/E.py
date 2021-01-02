mod=998244353
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=1
i=n-1
for j in range(m-1,-1,-1):
    l,r=-1,-1
    while i!=-1:
        if a[i]<b[j]:
            print(0)
            exit()
        if a[i]==b[j]:
            r=i
            break
        i-=1
    else:
        print(0)
        exit()
    while i!=-1:
        if a[i]<b[j]:
            l=i+1
            if j==0:
                print(0)
                exit()
            break
        i-=1
    else:
        if j!=0:
            print(0)
            exit()
    if j!=0:
        ans*=(r-l+1)
        ans%=mod
    #print(l,r)
print(ans)

