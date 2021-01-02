r1,c1=map(int,input().split())
r2,c2=map(int,input().split())
r,c=abs(r1-r2),abs(c1-c2)
if r==0 and c==0:
    print(0)
    exit()
if r+c<=3 or r==c:
    print(1)
    exit()
if r%2==c%2:
    print(2)
else:
    if abs(r-c)<=3:
        print(2)
    else:
        print(3)