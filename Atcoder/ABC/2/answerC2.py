import math
a1,b1,a2,b2,a3,b3=map(int,input().split())
a=math.sqrt((a1-a2)**2+(b1-b2)**2)
b=math.sqrt((a2-a3)**2+(b2-b3)**2)
c=math.sqrt((a3-a1)**2+(b3-b1)**2)
s=(a+b+c)/2
print(math.sqrt(s*(s-a)*(s-b)*(s-c)))
