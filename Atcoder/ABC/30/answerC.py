import bisect
n,m=map(int,input().split())
x,y=map(int,input().split())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
ma=max(a)
mb=max(b)

#bisect.bisect_right(a, 9)
k=0
t=0
while True:
    if k%2==0:
        if t>ma:
            break
        else:
            l=bisect.bisect_left(a,t)
            t=a[l]+x
    if k%2==1:
        if t>mb:
            break
        else:
            l=bisect.bisect_left(b,t)
            t=b[l]+y
    k+=1
    #print(t)
print(k//2)
