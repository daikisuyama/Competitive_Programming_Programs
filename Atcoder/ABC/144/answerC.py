import math

n=int(input())
n2=int(math.sqrt(n))

minimum=n-1
for i in range(1,n2+1):
    if(n%i==0):
        minimum=min(minimum,(n//i-1)+(i-1))

print(minimum)
