n=int(input())
a,b=[],[]
for i in range(n):
    c,d=map(int,input().split())
    a.append(c)
    b.append(d)
a.sort()
b.sort()
if n%2==0:
    x=[a[n//2-1],a[n//2]]
    y=[b[n//2-1],b[n//2]]
    print(sum(y)-sum(x)+1)
else:
    x=a[n//2]
    y=b[n//2]
    print(y-x+1)