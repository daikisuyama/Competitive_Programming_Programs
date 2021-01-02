n,k=map(int,input().split())
xy=[list(map(int,input().split())) for i in range(n)]
x,y=[[xy[i][0],i] for i in range(n)],[[xy[i][1],i] for i in range(n)]
x.sort()
y.sort()
ans=10**18*4
for i1 in range(n):
    i1_sub=n-i1
    x_sub1=x[i1][0]
    for l1 in range(i1_sub,1,-1):
        x_sub2=x[i1+l1-1][0]
        for i2 in range(n):
            i2_sub=n-i2
            y_sub1=y[i2][0]
            x_subsub=x_sub2-x_sub1
            for l2 in range(i2_sub,1,-1):
                y_sub2=y[i2+l2-1][0]
                z=0
                for i in range(n):
                    if x_sub1<=xy[i][0]<=x_sub2 and y_sub1<=xy[i][1]<=y_sub2:
                        z+=1
                    if z>=k:
                        ans=min(x_subsub*(y_sub2-y_sub1),ans)
                        break
                else:
                    break
print(ans)