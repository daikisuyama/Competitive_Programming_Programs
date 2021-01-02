n=int(input())
a=list(map(int,input().split()))
a.sort()
from collections import deque
b=deque(a)
l=n//2-1 if n%2==0 else n//2
ans=[]
while len(b)>=2:
    ans.append(b.pop())
    ans.append(b.popleft())
if len(b)==1:
    ans.append(b.pop())
print(l)
print(" ".join(map(str,ans)))