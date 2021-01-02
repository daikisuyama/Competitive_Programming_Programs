from collections import deque
n=int(input())
s=input()
d=deque()
ans=n
for i in range(n):
    if s[i]=="f":
        d.append(s[i])
    elif s[i]=="o":
        if len(d)==0:
            continue
        p=d.pop()
        if p!="f":
            d=deque()
        else:
            d.append(p)
            d.append(s[i])
    elif s[i]=="x":
        if len(d)<2:
            d=deque()
            continue
        p1,p2=d.pop(),d.pop()
        if p1=="o" and p2=="f":
            ans-=3
        else:
            d=deque()
    else:
        d=deque()
print(ans)