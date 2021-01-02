for _ in range(int(input())):
    x=list(map(int,input().split()))
    if min(x)==1 or max(x)==2:
        print("YES")
    else:
        print("NO")