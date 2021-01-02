for _ in range(int(input())):
    n,k=map(int,input().split())
    ans=[[0]*n for i in range(n)]
    f=False
    for j in range(n):
        for i in range(n):
            if k==0:
                f=True
                break
            k-=1
            ans[i][(i+j)%n]=1
        if f:
            break
    r=[sum(ans[i]) for i in range(n)]
    mar,mir=max(r),min(r)
    c=[sum([ans[i][j] for i in range(n)]) for j in range(n)]
    mac,mic=max(c),min(c)
    print((mar-mir)**2+(mac-mic)**2)
    for i in range(n):
        print("".join(map(str,ans[i])))