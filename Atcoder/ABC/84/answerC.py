import math
n=int(input())
csf=[list(map(int,input().split())) for i in range(n-1)]

for j in range(n-1):
    now=0
    for i in range(j,n-1):
        if csf[i][1]>=now:
            now=csf[i][1]+csf[i][0]
        else:
            now=csf[i][1]-((csf[i][1]-now)//csf[i][2])*csf[i][2]+csf[i][0]
    print(now)
print(0)

