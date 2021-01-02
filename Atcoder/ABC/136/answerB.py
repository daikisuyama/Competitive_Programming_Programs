import math
n=int(input())
c=0
for i in range(1,n+1):
    if int(math.log10(i))%2==0:
        c+=1
print(c)
