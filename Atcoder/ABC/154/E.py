import math
import itertools
n=int(input())
k=int(input())
def comb(n,k):
    return len(list(itertools.combinations(range(n), k)))
x=str(n)
m=len(x)
ans=0
for i in range(1,m):
    ans+=(comb(i-1,k-1)*(9**k))
if k==1:
    for i in range(1,10):
        if i*(10**(m-1))<=n:
            ans+=1
elif k==2:
    for i in range(1,10):
        if i*(10**(m-1))<=n:
            for j in range(m-1):
                for a in range(1,10):
                    if i*(10**(m-1))+a*(10**(j))<=n:
                        ans+=1
                    else:
                        break
        else:
            break
else:
    po=[10**i for i in range(m)]
    for i in range(1,10):
        if i*po[m-1]<=n:
            for j in range(m-1):
                for a in range(1,10):
                    if i*po[m-1]+a*po[j]<=n:
                        for b in range(j):
                            for c in range(1,10):
                                ans+=(i*po[m-1]+a*po[j]+c*po[b]<=n)
                    else:
                        break
        else:
            break
print(ans)
