for _ in range(int(input())):
    n,r=map(int,input().split())
    if r<n:
        print(r*(r+1)//2)
    else:
        print(1+(n-1)*n//2)