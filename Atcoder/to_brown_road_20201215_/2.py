a,b,c,d=map(int,input().split())
x,y=a+b,c+d
if x==y:
    print("Balanced")
elif x<y:
    print("Right")
else:
    print("Left")