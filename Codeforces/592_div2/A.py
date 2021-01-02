for _ in range(int(input())):
    a,b,c,d,k=map(int,input().split())
    x=-(-a//c)
    y=-(-b//d)
    if x+y>k:
        print(-1)
    else:
        print(x,y)