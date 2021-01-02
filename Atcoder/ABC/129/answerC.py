#一時間以上かかった
#一つだけTLE
#そっから30ぷん

import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r)*math.factorial(r))

n,m=[int(i) for i in input().split()]
a1=[int(input()) for i in range(m)]
a1.append(n+1)
c1=1
a2=0
for i in a1:
    a3=i-1-a2
    c2=0
    for j in range(a3//2+1):
        c2+=combinations_count(a3-j,j)
    c1=(c1*c2)%(1000000007)
    a2=i+1
    if c1==0:
        break



print(c1)
