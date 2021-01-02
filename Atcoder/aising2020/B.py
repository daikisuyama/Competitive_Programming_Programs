n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(n):
    ans+=(i%2==0 and a[i]%2==1)
print(ans)