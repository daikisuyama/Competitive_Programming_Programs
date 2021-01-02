n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
from itertools import accumulate
s=list(accumulate([1]+a))[:-1]
from bisect import bisect_right
#print(s)
ans=[]
for i in range(m):
    c=bisect_right(s,b[i])-1
    #print(c)
    ans.append(str(c+1)+" "+str(b[i]-s[c]+1))
for i in range(m):
    print(ans[i])