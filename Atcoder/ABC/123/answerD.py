from bisect import bisect_left
x,y,z,k=map(int,input().split())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
c=sorted([int(i) for i in input().split()])
ab_max=[]
for i in range(x):
    for j in range(y):
        ab_max.append(a[i]+b[j])
ab_max.sort()
def unti(t_sub):
    global x,y,z,k
    ret=0
    for i in range(x*y):
        h=z-bisect_left(c,t_sub-ab_max[i])
        if h==0 or ret>=k:
            return ret
        else:
            ret+=h
    return ret
l,r=0,ab_max[0]+c[-1]
while r>l+1:
    t=(l+r)//2
    if unti(t)>=k:
        r=t
    else:
        l=t
ans=[]
f=False
for i in range(x*y):
    for j in range(z-1,-1,-1):
        u=ab_max[i]+c[j]
        if u>=r:
            ans.append(u)
        else:
            if j==0:f=True
            break
    if f:
        break
ans.sort(reverse=True)
for i in range(k):
    print(ans[i])
