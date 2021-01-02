t=int(input())
ans=[0]*t
for i in range(t):
    ax,ay,bx,by,cx,cy=map(int,input().split())
    a,b,c=[ax,ay],[bx,by],[cx,cy]
    x,y=[a[0],b[0],c[0]],[a[1],b[1],c[1]]
    x.sort()
    y.sort()
    center=[x[0] if x[0]==x[1] else x[2],y[0] if y[0]==y[1] else y[2]]
    ans[i]=min(abs(i) for i in center)
for i in range(t):
    print(ans[i])