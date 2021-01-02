n=int(input())
a=sorted(list(map(int,input().split())))
ans=1
for i in range(n):
    ans*=a[i]
    if ans>10**18:
        print(-1)
        break
else:
    print(ans)