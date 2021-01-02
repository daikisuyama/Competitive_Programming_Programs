n=int(input())
h=list(map(int,input().split()))
ans=0
while True:
    l,m=-1,-1
    for i in range(n):
        if h[i]!=0:
            l=i
            break
    if l==-1:
        break
    if l==n-1:
        ans+=h[l]
        break
    r=l
    for i in range(l,n):
        if h[i]==0:
            break
        else:
            r=i
            if m==-1:
                m=h[i]
            else:
                m=min(m,h[i])

    for i in range(l,r+1):
        h[i]-=m
    ans+=m
print(ans)
