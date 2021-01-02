for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input()))
    ans=n
    if 1 not in s:
        print(ans)
        continue
    for i in range(n):
        if s[i]==1:
            ans=max(ans,n*2-i*2)
            break
    for i in range(n-1,-1,-1):
        if s[i]==1:
            ans=max(ans,n*2-(n-1-i)*2)
            break
    print(ans)