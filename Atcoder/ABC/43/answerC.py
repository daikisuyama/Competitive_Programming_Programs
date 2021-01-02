n=int(input())
a=[int(i) for i in input().split()]
ans=10000000000000
for i in range(-100,101):
    ans_sub=0
    for j in range(n):
        ans_sub+=(a[j]-i)**2
    ans=min(ans,ans_sub)
print(ans)
