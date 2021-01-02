t=int(input())
for _ in range(t):
    l,r,m=map(int,input().split())
    f=False
    for a in range(l,r+1):
        n1,n2=m//a,-((-m)//a)
        if l-r<=m-n1*a<=r-l:
            for c in range(l,r+1):
                b=m-n1*a+c
                if l<=b<=r:
                    if m+c-b!=0:
                        print(a,b,c)
                        f=True
                        break
        if f:break
        if l-r<=m-n2*a<=r-l:
            for c in range(l,r+1):
                b=m-n2*a+c
                if l<=b<=r:
                    if m+c-b!=0:
                        print(a,b,c)
                        f=True
                        break
        if f:break
