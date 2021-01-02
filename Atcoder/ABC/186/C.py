n=int(input())
check=[1]*n
for i in range(1,n+1):
    if "7" in str(i):
        check[i-1]=0
from itertools import product
p=[1]
for i in range(5):
    p.append(p[-1]*8)
for pr in product(range(8),repeat=6):
    x=0
    for i in range(6):
        x+=pr[i]*p[i]
    if x<=n and 7 in pr:
        check[x-1]=0
print(sum(check))