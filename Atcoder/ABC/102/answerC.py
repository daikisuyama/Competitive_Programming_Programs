n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    a[i]-=(i+1)
a.sort()

m,now=sum(a)-2*a[0]+2*a[0]-a[0]*n,sum(a)-2*a[0]+2*a[0]-a[0]*n
for i in range(1,n):
    now=now-(2*(i)*a[i-1]-n*a[i-1])+(-2*a[i]+2*(i+1)*a[i]-n*a[i])
    m=min(now,m)

print(m)