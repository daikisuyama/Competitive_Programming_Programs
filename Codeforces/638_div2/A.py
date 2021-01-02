for _ in range(int(input())):
    n=int(input())
    a=2**n+sum(2**i for i in range(1,n//2))
    b=sum(2**i for i in range(n//2,n))
    print(a-b)