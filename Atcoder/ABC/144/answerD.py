import math

a,b,x=map(int,input().split())

if 2*x<=a*a*b:
    p1=a*b*b
    p2=2*x
else:
    p1=2*(a*a*b-x)
    p2=a*a*a
    
sit=math.atan(p1/p2)
print(math.degrees(sit))
