t=0
N,T=map(int,input().split())
nt=[int(i) for i in input().split()]
ans=0
for i in range(N):
    if nt[i]>t:
        ans+=T
    else:
        ans+=(T-(t-nt[i]))
    t=nt[i]+T
print(ans)
