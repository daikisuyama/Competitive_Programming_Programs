#わからんわからん(40ふんくらい考えたけど、愚直しか思いつかない)
#合ってて草(ただ、エスパー)
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=[i*(i>0) for i in a]
#正で累積和
from itertools import accumulate
#accumulateのミス、先に書き換えて
aplus=list(accumulate(b))
aac=list(accumulate(a))
ans=[]
for i in range(n-k+1):
    ans_sub,d=0,0
    if i>0:
        ans_sub+=aplus[i-1]
        d-=aac[i-1]
    ans_sub+=aplus[n-1]-aplus[i+k-1]
    d+=aac[i+k-1]
    ans.append(max(d,0)+ans_sub)
print(max(ans))