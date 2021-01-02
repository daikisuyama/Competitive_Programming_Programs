n,k=map(int,input().split())
lamps=[list(map(int,input().split())) for i in range(n)]
s=set()
for i in range(n):
    s.add(lamps[i][0])
    s.add(lamps[i][1])
s=sorted(list(s))