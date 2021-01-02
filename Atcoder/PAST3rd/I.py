n,q=int(input()),int(input())
x=[i for i in range(n)]
y=[i for i in range(n)]
f=True
for i in range(q):
    q=list(map(int,input().split()))
    if q[0]==1:
        a,b=q[1]-1,q[2]-1
        x[a],x[b]=x[b],x[a]
        #y[a],y[b]=y[b],y[a]
    elif q[0]==2:
        a,b=q[1]-1,q[2]-1
        y[a],y[b]=y[b],y[a]
        #x[a],x[b]=x[b],x[a]
    elif q[0]==4:
        a,b=q[1]-1,q[2]-1
        if f:
            print(n*x[a]+y[b])
        else:
            print(n*y[b]+x[a])
    else:
        f=not f
        x,y=y,x
#print(x)
#print(y)