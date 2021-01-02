#は？打ち間違えた
for _ in range(int(input())):
    r,g,b,w=map(int,input().split())
    if (r+g+b+w)%2==0:
        if r%2==0 and g%2==0 and b%2==0 and w%2==0:
            print("Yes")
        elif r%2==1 and g%2==1 and b%2==1 and w%2==1:
            print("Yes")
        else:
            print("No")
    else:
        x=[r%2,g%2,b%2,w%2]
        if x.count(1)==1:
            print("Yes")
        elif x.count(0)==1 and r>0 and g>0 and b>0:
            print("Yes")
        else:
            print("No")