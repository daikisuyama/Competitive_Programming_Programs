def calc():
    global c1,c2,c3,c4,c5,c6,x1,x2,x3,x4,x5,x6
    return x1*c1+x2*c2+x3*c3+x4*c4+x5*c5+x6*c6
for _ in range(int(input())):
    x,y=map(int,input().split())
    c1,c2,c3,c4,c5,c6=map(int,input().split())
    ans=[]
    if x>0 and y>0:
        x1,x2,x3,x4,x5,x6=0,y,0,0,0,x
    elif x>0:
        x1,x2,x3,x4,x5,x6=0,0,0,0,-y,x
    elif y>0:
        x1,x2,x3,x4,x5,x6=0,y,-x,0,0,0
    else:
        x1,x2,x3,x4,x5,x6=0,0,-x,0,-y,0
    ans.append(calc())
    if x>0 and y-x>0:
        x1,x2,x3,x4,x5,x6=x,y-x,0,0,0,0
    elif y-x>0:
        x1,x2,x3,x4,x5,x6=0,y-x,0,-x,0,0
    elif x>0:
        x1,x2,x3,x4,x5,x6=x,0,0,0,x-y,0
    else:
        x1,x2,x3,x4,x5,x6=0,0,0,-x,x-y,0
    ans.append(calc())
    if y>0 and x-y>0:
        x1,x2,x3,x4,x5,x6=y,0,0,0,0,x-y
    elif x-y>0:
        x1,x2,x3,x4,x5,x6=0,0,0,-y,0,x-y
    elif y>0:
        x1,x2,x3,x4,x5,x6=y,0,y-x,0,0,0
    else:
        x1,x2,x3,x4,x5,x6=0,0,y-x,-y,0,0
    ans.append(calc())
    print(min(ans))