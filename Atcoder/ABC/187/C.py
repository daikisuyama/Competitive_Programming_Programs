n=int(input())
t=list(set([input() for i in range(n)]))
n=len(t)
d=dict()
for i in range(n):
    s=t[i]
    if s[0]=="!":
        if s[1:] in d:
            d[s[1:]]+=1
        else:
            d[s[1:]]=1
    else:
        if s in d:
            d[s]+=1
        else:
            d[s]=1
for i in d:
    if d[i]>=2:
        print(i)
        break
else:
    print("satisfiable")