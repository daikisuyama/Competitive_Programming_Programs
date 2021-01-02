#桁DPの意識！！！
n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=0
co=[0]*50
check=False
for i in range(49,-1,-1):
    for j in range(n):
        if (a[j]>>i)&1:
            co[i]+=1
    if (k>>i)&1:
        if co[i]>=n-co[i]:
            ans+=(co[i]*(2**i))
            check=True
        else:
            ans+=((n-co[i])*(2**i))
    else:
        if check:
            if co[i]>=n-co[i]:
                ans+=(co[i]*(2**i))
            else:
                ans+=((n-co[i])*(2**i))
        else:
            ans+=(co[i]*(2**i))
print(ans)