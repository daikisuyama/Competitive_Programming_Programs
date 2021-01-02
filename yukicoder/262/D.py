from math import sqrt
a,b,c,d,e,f=map(int,input().split())
if a<0:
    a,b,c,d,e,f=-a,-b,-c,-d,-e,-f
c/=a
d/=a
e/=a
f/=a
print(sqrt((c**2+d**2)/4-(e-f)))