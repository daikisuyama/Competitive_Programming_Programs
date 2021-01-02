d=dict()
n=int(input())
for i in range(n):
    s=input()
    if s in d:
        d[s]+=1
    else:
        d[s]=1
d=list(d.items())
d.sort(key=lambda x:x[0])
d.sort(key=lambda x:x[1],reverse=True)
m=len(d)
for i in range(m):
    if d[i][1]==d[0][1]:
        print(d[i][0])
    else:
        break
