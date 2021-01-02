n=int(input())
a=list(map(int,input().split()))
a.sort()
from collections import deque
b=deque(a[:n//2])
c=deque(a[n//2:])
ans=[]
while len(b) or len(c):
    ans.append(c.popleft())
    if len(b)>0:
        ans.append(b.popleft())
#print(ans)
l=0
for i in range(1,n-1):
    if ans[i-1]>ans[i] and ans[i]<ans[i+1]:
        l+=1
print(l)
print(" ".join(map(str,ans)))