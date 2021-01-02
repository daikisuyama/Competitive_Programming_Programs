n=int(input())
s=input()
t=input()
if s.count("1")!=t.count("1"):
    print(-1)
    exit()
from collections import deque
check1=deque()
check2=deque()
for i in range(n):
    if s[i]!=t[i]:
        if s[i]=="1":
            check1.append(i)
        else:
            check2.append(i)
ans=0
while len(check1):
    c,d=check1.popleft(),check2.popleft()
    e=deque([c,d])
    if c<d:
        now=0
        while len(check1):
            if now==0:
                c=check1.popleft()
                if c<d:
                    check1.appendleft(c)
                    break
                e.append(c)
                now=1-now
            else:
                d=check2.popleft()
                if d<c:
                    check2.appendleft(d)
                    check1.appendleft(e.pop())
                    break
                e.append(d)
                now=1-now
    else:
        now=1
        while len(check1):
            if now==0:
                c=check1.popleft()
                if c<d:
                    check1.appendleft(c)
                    check2.appendleft(e.pop())
                    break
                e.append(c)
                now=1-now
            else:
                d=check2.popleft()
                if d<c:
                    check2.appendleft(d)
                    break
                e.append(d)
                now=1-now
    ans+=1
print(ans)
