t=int(input())
for i in range(t):
    a,k=map(int,input().split())
    for i in range(k-1):
        ax=str(a)
        l,r=int(min(ax)),int(max(ax))
        if l==0:
            print(a)
            break
        else:
            a+=(l*r)
    else:
        print(a)