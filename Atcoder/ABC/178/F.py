n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
from collections import Counter,deque
x,y=Counter(a),Counter(b)
for i in range(1,n+1):
    if x[i]+y[i]>n:
        print("No")
        exit()
ans=b[::-1]
change=deque()
num=-1
now=deque()
for i in range(n):
    if a[i]==ans[i]:
        change.append(i)
        num=ans[i]
    else:
        now.append(i)
if change==[]:
    print("Yes")
    print(" ".join(map(str,ans)))
    exit()
while len(change):
    q=now.popleft()
    p=change.popleft()
    if a[q]!=num and ans[q]!=num:
        ans[q],ans[p]=ans[p],ans[q]
    else:
        change.appendleft(p)

print("Yes")
print(" ".join(map(str,ans)))