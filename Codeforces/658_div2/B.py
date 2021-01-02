t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=["First","Second"]
    ans=0
    for i in range(n):
        if a[i]!=1:
            ans=i
            break
    else:
        ans=n-1
    print(s[ans%2])