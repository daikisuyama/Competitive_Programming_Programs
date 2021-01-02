n=int(input())
a=[int(i) for i in input().split()]
if n%2==1:
    c=0
    for i in range(n//2):
        c+=abs(a[2*i]-a[2*i+2])
    print(c)
else:
    c,d=abs(a[0]-a[1]),abs(a[-1]-a[-2])
    for i in range(n//2-1):
        #print(c)
        c+=abs(a[2*i+1]-a[2*i+3])
    for i in range(n//2-1):
        d+=abs(a[2*i]-a[2*i+2])
    #print(c)
    #print(d)
    print(min(c,d))
