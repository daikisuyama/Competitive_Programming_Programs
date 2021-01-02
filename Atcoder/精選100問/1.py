#11/25 7:57~8:00
while True:
    n,x=map(int,input().split())
    if n==0:break
    ans=0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
                ans+=j<x-(i+j)<=n
    print(ans)