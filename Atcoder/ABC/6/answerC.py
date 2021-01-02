n,m=map(int,input().split())
if 2*n>m or m>4*n:
    print("-1 -1 -1")
else:
    if m%2==0:
        x=m//2
        print(2*n-x,end=" ")
        print("0",end=" ")
        print(x-n)

    else:
        x=m//2
        print(2*n-x-1,end=" ")
        print("1",end=" ")
        print(x-n)
