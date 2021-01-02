from collections import deque
for _ in range(int(input())):
    n=int(input())
    r,p,s=map(int,input().split())
    t=input()
    ans=["" for i in range(n)]
    w=0
    for i in range(n):
        if t[i]=="R":
            if p>0:
                ans[i]="P"
                p-=1
                w+=1
        elif t[i]=="P":
            if s>0:
                ans[i]="S"
                s-=1
                w+=1
        else:
            if r>0:
                ans[i]="R"
                r-=1
                w+=1
    if w<-(-n//2):
        print("NO")
    else:
        ansp=deque()
        for i in range(r):
            ansp.append("R")
        for i in range(p):
            ansp.append("P")
        for i in range(s):
            ansp.append("S")
        for i in range(n):
            if ans[i]=="":
                ans[i]=ansp.popleft()
        print("YES")
        print("".join(ans))