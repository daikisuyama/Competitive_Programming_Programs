n,k,m=map(int,input().split())
a=sum(list(map(int,input().split())))
if n*m-a>k:
    print(-1)
else:
    print(max(n*m-a,0))
