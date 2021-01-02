n=int(input())
a=list(map(int,input().split()))
c,d=dict(),dict()
for i in range(n):
    if i+1-a[i] in c:
        c[i+1-a[i]]+=1
    else:
        c[i+1-a[i]]=1
    if i+1+a[i] in d:
        d[i+1+a[i]]+=1
    else:
        d[i+1+a[i]]=1
ans=0
for i in c:
    if i in d:
        ans+=(c[i]*d[i])
print(ans)
