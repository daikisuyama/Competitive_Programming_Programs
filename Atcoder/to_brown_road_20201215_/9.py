n=int(input())
ans=0
for i in range(1,n+1):
    x=0
    if i%2==0:continue
    for j in range(1,i+1):
        x+=(i%j==0)
    ans+=(x==8)
print(ans)