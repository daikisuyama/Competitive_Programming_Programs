n,t=map(int,input().split())
ct=[list(map(int,input().split())) for i in range(n)]
c=10000000000000000
for i in range(n):
    if ct[i][1]<=t:
        c=min(c,ct[i][0])
print(c if c!=10000000000000000 else "TLE")