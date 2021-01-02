n,k=map(int,input().split())
a=[int(input())-k for i in range(n)]
from itertools import accumulate,groupby
b=list(accumulate([-k]+a))
b.sort()
c=list([len(list(j)) for i,j in groupby(b)])
print(c)