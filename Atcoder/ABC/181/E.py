n,m=map(int,input().split())
h=list(map(int,input().split()))
h.sort()
w=list(map(int,input().split()))
#奇偶([0,1] [2,3] … [n-3,n-2])
x=[0]
for i in range((n-3)//2+1):
    x.append(h[2*i+1]-h[2*i])
for i in range((n-3)//2+1):
    x[i+1]+=x[i]
#偶奇([1,2] [3,4] … [n-2,n-1])
y=[0]
for i in range((n-3)//2+1):
    y.append(h[2*i+2]-h[2*i+1])
for i in range((n-3)//2+1):
    y[i+1]+=y[i]
from bisect import bisect_left
ans=10**12
for i in range(m):
    b=bisect_left(h,w[i])
    if b%2==0:
        c=b
    else:
        c=b-1
    ans=min(ans,x[c//2]+(y[-1]-y[c//2])+abs(w[i]-h[c]))
print(ans)