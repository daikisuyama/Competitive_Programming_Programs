for _ in range(int(input())):
    n,m=map(int,input().split())
    r,c=[False]*n,[False]*m
    for i in range(n):
        x=list(map(int,input().split()))
        if not all(k==0 for k in x):
            r[i]=True
        for j in range(m):
            if x[j]==1:
                c[j]=True
    z=min(r.count(False),c.count(False))
    print(["Vivek","Ashish"][z%2])