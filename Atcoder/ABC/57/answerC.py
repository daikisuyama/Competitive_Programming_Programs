from sys import exit
import math
n=int(input())
l=math.floor(math.sqrt(n))

for i in range(l+1,0,-1):
    if n%i==0:
        a,b=i,n//i
        h=max(a,b)
        k=math.floor(math.log10(h))+1
        print(k)
        exit()
