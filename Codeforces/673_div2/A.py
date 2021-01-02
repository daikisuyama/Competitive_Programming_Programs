for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    m=min(a)
    l=a.index(m)
    ans=0
    for i in range(n):
        if i!=l:
            ans+=(k-a[i])//m
    print(ans)