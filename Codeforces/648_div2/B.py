for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=sorted(a)
    b=list(map(int,input().split()))
    if a==c:
        print("Yes")
        continue
    if b.count(1)==n or b.count(0)==n:
        print("No")
    else:
        print("Yes")