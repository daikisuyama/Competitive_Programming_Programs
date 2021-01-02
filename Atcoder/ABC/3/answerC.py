n,k=map(int,input().split())
r=sorted(sorted([int(i) for i in input().split()],reverse=True)[:k])
ans=0
for i in r:
    ans=(ans+i)/2
print(ans)
