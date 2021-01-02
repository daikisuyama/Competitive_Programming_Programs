for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    l,r=sum(a[i]%2==1 for i in range(n)),sum(a[i]%2==0 for i in range(n))
    if l==0:
        print("No")
    elif x==n:
        print(["No","Yes"][sum(a)%2])
    elif r==0:
        print(["No","Yes"][x%2])
    else:
        print("Yes")