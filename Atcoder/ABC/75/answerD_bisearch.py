n,k=map(int,input().split())
xy=[list(map(int,input().split())) for i in range(n)]
x,y=[[xy[i][0],i] for i in range(n)],[[xy[i][1],i] for i in range(n)]
x.sort()
y.sort()
inf=10**18*4
ans=inf
def upper_k(x_sub1,x_sub2,y_sub1,y_sub2):
    global n,k,xy
    z=0
    for i in range(n):
        if x_sub1<=xy[i][0]<=x_sub2 and y_sub1<=xy[i][1]<=y_sub2:
            z+=1
        if z>=k:return True
    return False

for i1 in range(n):
    i1_sub=n-i1
    x_sub1=x[i1][0]
    for l1 in range(i1_sub,1,-1):
        x_sub2=x[i1+l1-1][0]
        x_subsub=x_sub2-x_sub1
        for i2 in range(n):
            ans_sub=inf
            i2_sub=n-i2
            y_sub1=y[i2][0]
            l,r=2,i2_sub
            if r<l:break
            while l+1<r:
                t=(l+r)//2
                y_sub2=y[i2+t-1][0]
                if upper_k(x_sub1,x_sub2,y_sub1,y_sub2):
                    r=t
                else:
                    l=t
            y_sub2=y[i2+r-1][0]
            if upper_k(x_sub1,x_sub2,y_sub1,y_sub2):
                ans=min(x_subsub*(y_sub2-y_sub1),ans)
            if l!=r:
                y_sub2=y[i2+l-1][0]
                if upper_k(x_sub1,x_sub2,y_sub1,y_sub2):
                    ans=min(x_subsub*(y_sub2-y_sub1),ans)
print(ans)

