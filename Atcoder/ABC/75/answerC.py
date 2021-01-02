n,m=map(int,input().split())
x=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    x[a-1].append(b-1)
    x[b-1].append(a-1)

def size0find():
    global x,n
    next=[]
    for i in range(n):
        if len(x[i])==1:
            next.append(i)
            k=x[i][0]
            x[i].remove(k)
            x[k].remove(i)
    return next

cnt=0
while True:
    y=size0find()
    l=len(y)
    if l==0:
        break
    cnt+=l
print(cnt)