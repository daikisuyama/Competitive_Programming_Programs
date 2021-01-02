t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=set(map(int,input().split()))
    for i in a:
        if i in b:
            print("YES")
            print(f"1 {i}")
            break
    else:
        print("NO")