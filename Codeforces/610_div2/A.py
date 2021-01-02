for _ in range(int(input())):
    a,b,c,r=map(int,input().split())
    if a>b:
        a,b=b,a
    ans=0
    if c+r<a:
        print(b-a)
    elif c+r<=b:
        if c-r<=a:
            print(b-(c+r))
        else:
            print(b-(c+r)+(c-r)-a)
    else:
        if c-r<=a:
            print(0)
        elif c-r<=b:
            print((c-r)-a)
            #print(c-r,b)
        else:
            print(b-a)