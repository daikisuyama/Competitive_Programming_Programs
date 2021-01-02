import math
a1,b1,a2,b2,a3,b3=map(int,input().split())
a=math.sqrt((a1-a2)**2+(b1-b2)**2)
b=math.sqrt((a2-a3)**2+(b2-b3)**2)
c=math.sqrt((a3-a1)**2+(b3-b1)**2)
c=(a**2+b**2-c**2)/(2*a*b)
s=math.sqrt(1-c**2)
print(a*b*s/2)
