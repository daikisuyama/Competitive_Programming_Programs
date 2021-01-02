n=int(input())
a=[int(i) for i in input().split()]

if sum(a)%n!=0:
    print(-1)
else:
    k1,k2=0,0
    c=0
    for i in range(n):
        k1+=a[i]
        k2+=1
        if k1==k2*(sum(a)//n) or i==n-1:
            c+=(k2-1)
            k1,k2=0,0
        #print(k2)
    print(c)
