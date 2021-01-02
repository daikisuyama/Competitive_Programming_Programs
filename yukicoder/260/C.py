from random import randint
x1,x2=map(int,input().split())
def calc(x):
    c=[0,0]
    while x%2==0:
        c[0]+=1
        x//=2
    while x%5==0:
        c[1]+=1
        x//=5
    return c
c1=calc(x1)
c2=calc(x2)
f=True
def dis(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])
for i in range(70):
    if i%2==0:
        if c1[0]<9 and f:
            if dis([c1[0]+1,c1[1]],c2)<dis(c1,c2):
                c1=[c1[0]+1,c1[1]]
                x1*=2
                print(x1,flush=True)
                if x1==x2:break
                continue
        if c1[0]>0 and f:
            if dis([c1[0]-1,c1[1]],c2)<dis(c1,c2):
                c1=[c1[0]-1,c1[1]]
                x1//=2
                print(x1,flush=True)
                if x1==x2:break
                continue
        if c1[1]<9 and not f:
            if dis([c1[0],c1[1]+1],c2)<dis(c1,c2):
                c1=[c1[0],c1[1]+1]
                x1*=5
                print(x1,flush=True)
                if x1==x2:break
                continue
        if c1[1]>0 and not f:
            if dis([c1[0],c1[1]-1],c2)<dis(c1,c2):
                c1=[c1[0],c1[1]-1]
                x1//=5
                print(x1,flush=True)
                if x1==x2:break
                continue
    else:
        x_=int(input())
        if x2>x_:
            f=(x2//x_==2)
        else:
            f=(x_//x2==2)
        x2=x_
        if x1==x2:break