from collections import deque
n=int(input())
c=input()
r=deque()
lr=0
for i in range(n):
    if c[i]=="R":
        lr+=1
        r.append(i)
ans=0
for i in range(n):
    if lr==0:
        break
    if c[i]=="W":
        if i<r[-1]:
            ans+=1
            r.pop()
            lr-=1
        else:
            break

print(ans)