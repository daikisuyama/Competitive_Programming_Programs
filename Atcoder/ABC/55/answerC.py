n,m=map(int,input().split())
if 2*n>=m:
    print(m//2)
else:
    x=m-2*n
    print(n+x//4)
