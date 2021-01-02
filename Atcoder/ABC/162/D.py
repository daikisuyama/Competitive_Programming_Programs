n=int(input())
s=input()
r,g,b=[],[],[]
for i in range(n):
    if s[i]=="R":
        r.append(i)
    elif s[i]=="G":
        g.append(i)
    else:
        b.append(i)
b=set(b)
lb=len(b)
ans=0
for i in r:
    for j in g:
        x,y=min(i,j),max(i,j)
        ans_=lb
        if x-(y-x) in b:
            ans_-=1
        if y+(y-x) in b:
            ans_-=1
        if (x%2==y%2) and (y-x)//2+x in b:
            ans_-=1
        ans+=ans_
print(ans)
