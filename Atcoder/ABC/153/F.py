import bisect
import math
n,d,a=map(int,input().split())
xh=[list(map(int,input().split())) for i in range(n)]
xh.sort()
x=[xh[i][0] for i in range(n)]
h=[xh[i][1] for i in range(n)]
g=[0]*n
cnt=0
for i in range(n):
    #print(h)
    if h[i]>0:
        m=math.ceil(h[i]/a)
        cnt+=m
        k=bisect.bisect_right(x,x[i]+2*d,lo=i)
        if i!=n-1:
            h[i]-=m*a
            g[i]-=m*a
            if k<n:
                g[k]+=m*a
            g[i+1]+=g[i]
            h[i+1]+=g[i+1]
    else:
        if i!=n-1:
            g[i+1]+=g[i]
            h[i+1]+=g[i+1]
print(cnt)
