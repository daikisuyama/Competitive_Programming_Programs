for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=set()
    for i in range(n):
        s.add((i+a[i%n])%n)
    #print(s)
    print("YES" if len(s)==n else "NO")