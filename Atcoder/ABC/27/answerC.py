import math
n=int(input())
k=math.floor(math.log2(n))
if k%2==1:
    x=1
    for i in range(k):
        if i%2==0:
            x=2*x
        else:
            x=2*x+1
    if x<=n:
        print("Takahashi")
    else:
        print("Aoki")
else:
    x=1
    for i in range(k):
        if i%2==0:
            x=2*x+1
        else:
            x=2*x
    if x<=n:
        print("Aoki")
    else:
        print("Takahashi")
