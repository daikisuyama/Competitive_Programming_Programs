import math
ans=0
x=int(input())
y=100
while y<x:
    ans+=1
    y=math.floor(1.01*y)
print(ans)