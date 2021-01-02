for _ in range(int(input())):
    a,b,n,m=map(int,input().split())
    if m>min(a,b):
        print("No")
    elif n+m>a+b:
        print("No")
    else:
        print("Yes")