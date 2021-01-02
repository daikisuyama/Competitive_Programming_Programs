import math
a1,b1,a2,b2,a3,b3=map(int,input().split())
a2,b2,a3,b3=a2-a1,b2-b1,a3-a1,b3-b1
print(abs(a2*b3-a3*b2)/2)
