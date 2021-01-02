n,a,b=[int(i) for i in input().split()]
x=0
for i in range(n):
    s,d=input().split()
    d=int(d)
    if d<a:
        d=a
    elif d>b:
        d=b
    if s=="West":
        x+=d
    else:
        x-=d

if x>0:
    print(" ".join(["West",str(x)]))
elif x<0:
    print(" ".join(["East",str(-x)]))
else:
    print(0)
