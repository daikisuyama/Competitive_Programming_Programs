t=int(input())
for _ in range(t):
    l,r=map(int,input().split())
    x,y=l,2*l
    if y<=r:
        print(x,y)
    else:
        print("-1 -1")