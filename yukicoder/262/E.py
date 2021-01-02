from math import sqrt
a,b,c=map(int,input().split())
if a<0:
    a,b,c=-a,-b,-c
d=b**2-4*a*c
if d<0:
    print("imaginary")
elif d==0:
    print(-(b/2/a))
else:
    print(-((b+sqrt(d))/2/a),-((b-sqrt(d))/2/a))