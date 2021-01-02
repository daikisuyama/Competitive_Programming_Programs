for _ in range(int(input())):
    n,a,b,da,db=map(int,input().split())
    tree=[[] for i in range(n)]
    for i in range(n-1):
        u,v=map(int,input().split())
        tree[u-1].append(v-1)
        tree[v-1].append(u-1)
    if db<=2*da:
        print("Alice")
    else:
        print("Bob")