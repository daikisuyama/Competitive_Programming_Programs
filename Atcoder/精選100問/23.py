#12:55~
n,m=map(int,input().split())
p=[int(input()) for i in range(n)]
p=[p[i] for i in range(n) if p[i]<=m]
p.sort()
n=len(p)
#1,2で組み合わせ考えればOK
q=set()
for i in range(n):
    for j in range(n):
        if p[i]+p[j]<=m:
            q.add(p[i]+p[j])
q=list(q)
q.sort()
#1,2の最大
ans=max(p[-1],q[-1])
#3の最大
from bisect import bisect_right
for i in range(n):
    b=bisect_right(q,m-p[i])-1
    if b!=-1:
        ans=max(ans,p[i]+q[b])
#4の最大
for i in q:
    b=bisect_right(q,m-i)-1
    if b!=-1:
        ans=max(ans,i+q[b])
print(ans)