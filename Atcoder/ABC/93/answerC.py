a,b,c=map(int,input().split())
if a%2==b%2 and b%2==c%2:
    x=sorted([a,b,c])
    print((x[2]-x[1])//2+(x[2]-x[0])//2)
elif a%2==b%2:
    a+=1
    b+=1
    x=sorted([a,b,c])
    print((x[2]-x[1])//2+(x[2]-x[0])//2+1)
elif b%2==c%2:
    b+=1
    c+=1
    x=sorted([a,b,c])
    print((x[2]-x[1])//2+(x[2]-x[0])//2+1)
else:
    c+=1
    a+=1
    x=sorted([a,b,c])
    print((x[2]-x[1])//2+(x[2]-x[0])//2+1)