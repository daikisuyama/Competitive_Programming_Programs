for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if a.count(0)>=n/2:
        print(n//2)
        print(" ".join("0"*(n//2)))
    else:
        #この時、1はn//2+1個以上
        if (n//2)%2==0:
            print(n//2)
            print(" ".join("1"*(n//2)))
        else:
            print(n//2+1)
            print(" ".join("1"*(n//2+1)))