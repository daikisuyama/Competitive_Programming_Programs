for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    if a.count(x)==n:
        print(0)
    elif sum(a)==n*x:
        print(1)
    else:
        if a.count(x)>0:
            print(1)
        else:
            print(2)