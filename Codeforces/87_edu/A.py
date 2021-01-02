t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    if d>=c:
        if b>=a:
            print(b)
        else:
            print(-1)
    else:
        if b>=a:
            print(b)
        else:
            a-=b
            num=-((-a)//(c-d))
            print(b+num*c)