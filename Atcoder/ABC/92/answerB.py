n=int(input())
d,x=map(int,input().split())
a=[int(input()) for i in range(n)]
ans=0
for i in range(1,d+1):
    for j in range(n):
        if a[j]==1:
            ans+=(i%a[j]==0)
        else:
            ans+=(i%a[j]==1)
print(ans+x)