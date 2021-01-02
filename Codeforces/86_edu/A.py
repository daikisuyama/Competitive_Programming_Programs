for _ in range(int(input())):
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    if x>y:
        x,y=y,x
    print((y-x)*a+min(x*b,2*x*a))