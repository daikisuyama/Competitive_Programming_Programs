n=int(input())
d=dict()
for i in range(n):
    s=input()
    if s in d:
        d[s]+=1
    else:
        d[s]=1
m=int(input())
for i in range(m):
    s=input()
    if s in d:
        d[s]-=1
    else:
        d[s]=-1
x=[-10**12,""]
for i in d:
    if d[i]>x[0]:
        x[0]=d[i]
        x[1]=i
print(max(x[0],0))