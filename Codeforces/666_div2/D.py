for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if n==1:
        print("T")
    elif max(a) > sum(a)//2:
        print("T")
    else:
        print(["T","HL"][(sum(a)-1)%2])