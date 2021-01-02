for _ in range(int(input())):
    x1,y1,z1=map(int,input().split())
    x2,y2,z2=map(int,input().split())
    ans=0
    #まずz1から
    if z1<=y2:
        ans+=(2*z1)
        y2-=z1
        z1=0
    else:
        ans+=(2*y2)
        z1-=y2
        y2=0
        if z1<=z2:
            z2-=z1
            z1=0
        else:
            z1-=z2
            z2=0
            x2-=z1
    #次はy1(x1どうでもいい、どうせゼロなので)
    if y1<=x2+y2:
        print(ans)
    else:
        print(ans-(y1-x2-y2)*2)
