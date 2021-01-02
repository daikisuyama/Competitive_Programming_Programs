from itertools import accumulate
from collections import Counter
import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n,m=map(int,input().split())
s=list(map(lambda x:x%m,list(accumulate(list(map(int,input().split()))))))
s.append(0)
print(s)
d=Counter(s)
print(d)
ans=0
for i in d:
    if d[i]>=2:
        ans+=combinations_count(d[i],2)
print(ans)

#M人の子供たちに均等に配りたく、l→rがMの倍数
#区間を複数考える場合は累積和が有効
#これを考慮するとA1→ArからA1→Al-1を引けばよく、Mで割った余りが等しければ良い
#これはCounterでできる
#A0も必要なので忘れない