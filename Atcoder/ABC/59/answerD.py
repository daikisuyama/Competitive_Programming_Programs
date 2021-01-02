#間違えてる
def next_tup(x,y):
    if x==0 or x==1:#xを常にでかく
        x,y=y,x
    k=x//2
    x-=2*k
    y+=k
    return (x,y)

def defeat(tup):
    return tup==(1,1) or tup==(0,1) or tup==(1,0) or tup==(0,0)

X,Y=map(int,input().split())
if defeat((X,Y)):
    print("Brown")
else:
    ans=[]
    x_sub1,y_sub1=X,Y
    f1=0
    while True:
        z=next_tup(x_sub1,y_sub1)
        if defeat(z):
            break
        else:
            x_sub1,y_sub1=z
            if f1==0:
                f1=1
            else:
                f1=0
    ans.append(f1)
    x_sub2,y_sub2=Y,X
    f2=0
    while True:
        z=next_tup(x_sub2,y_sub2)
        if defeat(z):
            break
        else:
            x_sub2,y_sub2=z
            if f2==0:
                f2=1
            else:
                f2=0
    ans.append(f2)
    if 0 in ans:
        print("Alice")
    else:
        print("Brown")
