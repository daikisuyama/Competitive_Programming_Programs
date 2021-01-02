for _ in range(int(input())):
    n,k=map(int,input().split())
    if n==k:
        print(0)
    elif n>k:
        if (n+k)%2==0:
            print(0)
        else:
            print(1)
    else:
        print(k-n)