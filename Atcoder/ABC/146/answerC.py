import math
a,b,x=map(int,input().split())
j,k=1,1000000000

def calc(n):
    return a*n+b*int(math.log10(n)+1)

while j+1<k:
    l=(j+k)//2
    if calc(l)>x:
        k=l
    elif calc(l)<x:
        j=l
    else:
        print(l)
        break
else:
    if calc(k)<=x:
        print(k)
    elif calc(j)<=x:
        print(j)
    else:
        print(0)
