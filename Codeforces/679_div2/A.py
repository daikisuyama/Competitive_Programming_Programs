for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=[0]*n
    for i in range(n//2):
        b[2*i]=-a[2*i+1]
        b[2*i+1]=a[2*i]
    print(" ".join(map(str,b)))