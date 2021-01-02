mod=10**9+7
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    if a<b:
        a,b=b,a
    x=(n-a-b+1)*(n-a-b+2)//2*(n-a+1)*(n-b+1)*4
    y=((n-a-b+1)*(n-a-b+2)//2)**2*4
    if a+b>n:
        print(0)
        continue
    print((x-y)%mod)