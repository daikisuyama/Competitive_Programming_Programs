n,m=map(int,input().split())
x=[]
for i in range(m):
    a,b=map(int,input().split())
    if a==1:
        x.append(b)
    if b==n:
        x.append(a)
l=len(x)
if len(set(x))==l:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
