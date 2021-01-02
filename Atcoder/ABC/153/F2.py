import bisect
import math
n,d,a=map(int,input().split())
xh=[list(map(int,input().split())) for i in range(n)]
xh.sort()
x=[xh[i][0] for i in range(n)]
h=[xh[i][1] for i in range(n)]
cnt=0
for i in range(n):
    #print(cnt)
    if h[i]>0:
        m=math.ceil(h[i]/a)
        cnt+=m
        k=bisect.bisect_right(x,x[i]+2*d,lo=i)
        for j in range(i,k):
            h[j]-=(m*a)
print(cnt)
