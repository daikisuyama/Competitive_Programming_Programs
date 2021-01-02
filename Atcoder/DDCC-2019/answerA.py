x,y=map(int,input().split())
z=[300000,200000,100000]

if x==1 and y==1:
    print(1000000)
else:
    k,l=0,0
    if 1<=x<=3:
         k=z[x-1]
    if 1<=y<=3:
         l=z[y-1]
    print(k+l)
