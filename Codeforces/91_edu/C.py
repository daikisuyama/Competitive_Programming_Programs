t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=sorted(list(map(int,input().split())),reverse=True)
    now=[100000000000,0]
    for i in range(n):
        now=[min(now[0],a[i]),now[1]+1]
        if now[0]*now[1]>=x:
            d.append(now)
            now=[100000000000,0]
    print(len(d))