n,w=map(int,input().split())
a=list(map(int,input().split()))
from itertools import accumulate
b=list(accumulate(a))
u,d=max(b),min(b)
ran=[max(0,-d),min(w,w-u)]
print(max(0,ran[1]-ran[0]+1))