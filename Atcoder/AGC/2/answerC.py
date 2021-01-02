n,l=map(int,input().split())
from itertools import chain
x=list(map(int,input().split()))
for i in range(n-1):
    if x[i]+x[i+1]>=l:
        print("Possible")
        z=[j+1 for j in chain(range(i),range(n-2,i,-1),[i])]
        for i in z:
            print(i)
        break
else:
    print("Impossible")