for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input()))
    a=[x[i] for i in range(n) if i%2==0]
    b=[x[i] for i in range(n) if i%2==1]
    if n%2==1:
        if all(i%2==0 for i in a):
            print(2)
        else:
            print(1)
    else:
        if all(i%2==1 for i in b):
            print(1)
        else:
            print(2)