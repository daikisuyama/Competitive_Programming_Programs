a,b,c,d=map(int,input().split())
xy=dict()
for i in range(a+b,b+c+1):
    f=min(i-a-b+1,b+c-i+1)
    f=min(f,b-a+1,c-b+1)
    xy[i]=f
ans=0
for i in range(a+b,b+c+1):
    if i>d:
        ans+=(xy[i]*(d-c+1))
    elif i<=c:
        continue
    else:
        ans+=(xy[i]*(i-c))
print(ans)