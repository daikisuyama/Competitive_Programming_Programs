#多めのピザができてもOK
a,b,c,x,y=map(int,input().split())
if a+b<=2*c:
    print(x*a+y*b)
else:
    if x<=y:
        print(min(2*x*c+(y-x)*b,2*y*c))
    else:
        print(min(2*y*c+(x-y)*a,2*x*c))