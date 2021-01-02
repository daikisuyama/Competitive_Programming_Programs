for _ in range(int(input())):
    n,s,k=map(int,input().split())
    a=set(map(int,input().split()))
    if s not in a:
        print(0)
        continue
    for i in range(1,1001):
        if 0<s-i<=n:
            if s-i not in a:
                print(i)
                break
        if 0<s+i<=n:
            if s+i not in a:
                print(i)
                break