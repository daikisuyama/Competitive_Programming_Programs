for _ in range(int(input())):
    a,b=map(int,input().split())
    x=0
    for i in range(32):
        if ((a>>i)&1):
            if ((b>>i)&1):
                pass
            else:
                x+=(1<<i)
        else:
            if ((b>>i)&1):
                x+=(1<<i)
            else:
                pass
    print(x)