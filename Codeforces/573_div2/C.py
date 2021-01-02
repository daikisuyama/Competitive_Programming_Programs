n,m,k=map(int,input().split())
p=[i-1 for i in list(map(int,input().split()))]
ans=0
now=0
for i in range(n):
while True:
    print(now)
    ad=p[i]-now
    now+=ad//k*k
    now+=k
    num=0
    while i<m:
        if p[i]<now:
            num+=1
            i+=1
        else:
            break
    print(num)
    now-=num
    ans+=1
    if i==m:
        break
    print()
print(ans)