n=int(input())
ans=0
for a in range(1,n):
    if n%a==0:
        ans+=(n//a-1)
    else:
        ans+=(n//a)
print(ans)