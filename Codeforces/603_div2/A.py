for _ in range(int(input())):
    r,g,b=sorted(list(map(int,input().split())))
    m=g-r
    g-=m
    b-=m
    #print(r,g,b)
    if r+g<=b:
        print(m+r+g)
    else:
        n=b
        r-=n//2
        g-=n//2
        print(m+n//2*2+r)