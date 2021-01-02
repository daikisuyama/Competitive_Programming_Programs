#ソートし忘れてた…
n,p=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
ans=[]
from bisect import bisect_right
for i in range(min(a),max(a)):
    for j in range(n):
        b=bisect_right(a,i+j)-j
        if b<=0:
            break
        elif b%p==0:
            break
    else:
        ans.append(i)
print(len(ans))
print(" ".join(map(str,ans)))