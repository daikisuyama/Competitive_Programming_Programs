for _ in range(int(input())):
    n,m,k=map(int,input().split())
    x=min(m,n//k)
    y=-((x-m)//(k-1))
    print(max(0,x-y))