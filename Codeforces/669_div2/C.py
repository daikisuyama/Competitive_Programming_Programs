n=int(input())
from collections import deque
now=deque([i for i in range(n)])
ans=[0]*n
for i in range(n-1):
    if len(now)>=2:
        p=now.popleft()
        q=now.popleft()
        print(f"? {p+1} {q+1}",flush=True)
        a=int(input())
        print(f"? {q+1} {p+1}",flush=True)
        b=int(input())
        if a<b:
            ans[q]=b
            now.append(p)
        else:
            ans[p]=a
            now.append(q)
sub=sorted(ans)[1:]
for i in range(n-1):
    if sub[i]!=i+1:
        ans[ans.index(0)]=i+1
        break
else:
    ans[ans.index(0)]=n
print(f"! {' '.join(map(str,ans))}")