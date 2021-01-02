n,a,b=map(int,input().split())
ans=0
for i in range(1,n+1):
    s=0
    j=i
    while j!=0:
        s+=(j%10)
        j//=10
    if a<=s<=b:ans+=i
print(ans)