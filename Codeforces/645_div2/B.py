for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    for i in range(n-1,-1,-1):
        if a[i]<=i+1:
            print(i+2)
            break
    else:
        print(1)